# -*- coding: utf8 -*-
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Sync Server
#
# The Initial Developer of the Original Code is the Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Tarek Ziade (tarek@mozilla.com)
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice

# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
"""
Runs the Application. This script can be called by any wsgi runner that looks
for an 'application' variable
"""
import os
from logging.config import fileConfig
from ConfigParser import NoSectionError

# setting up the egg cache to a place where apache can write
os.environ['PYTHON_EGG_CACHE'] = '/tmp/python-eggs'

# the ini file is grabbed at its production place
# unless force via an environ variable
ini_file = os.path.join('/etc', 'demoapp', 'production.ini')
ini_file = os.path.abspath(os.environ.get('INI_FILE', ini_file))

# running the app using Paste
if __name__ == '__main__':
    # setting up logging
    try:
        fileConfig(ini_file)
    except NoSectionError:
        pass

    from paste.deploy import loadapp
    application = loadapp('config:%s' % ini_file)
