# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2017 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""This file mainly exists to allow python setup.py test to work."""

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'weblate.settings_test'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

from django.core.management import execute_from_command_line


def runtests():
    execute_from_command_line(['setup.py', 'test'])
    # We get here only if tests do not fail
    sys.exit(0)


if __name__ == '__main__':
    runtests()
