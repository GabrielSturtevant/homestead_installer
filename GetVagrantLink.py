#!/usr/bin/python3
#
# homestead_installer
# Copyright (C) 2017, Gabriel Sturtevant <gabriel@gabrielsturtevant.com>
#
# This file is part of homestead_installer.
#
# homestead_installer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# homestead_installer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with homestead_installer.  If not, see <http://www.gnu.org/licenses/>.
#
# Contributor(s):
# Gabriel Sturtevant <gabriel@gabrielsturtevant.com>
from bs4 import BeautifulSoup
import requests
import sys

url = "https://www.vagrantup.com/downloads.html"

request = requests.get(url)

data = request.text

soup = BeautifulSoup(data, 'lxml')

for link in soup.find_all('a'):
    linkText = link.get('href')
    if 'deb' in linkText and 'x86_64' in linkText:
        print(linkText)
        sys.exit(0)
