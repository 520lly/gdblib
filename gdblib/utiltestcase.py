# 
# GdbLib - A Gdb python library.
# Copyright (C) 2012  Fernando Castillo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import unittest
import os

from gdblib import util

class UtilTestCase(unittest.TestCase):
    def testRemoveFile(self):
        path = os.sep
        path += 'home'
        path += os.sep
        path += 'test'
        path += os.sep
        path += 'a.txt'

        expected = os.sep
        expected += 'home'
        expected += os.sep
        expected += 'test'
        self.assertEquals(expected, util.removeFile(path))


