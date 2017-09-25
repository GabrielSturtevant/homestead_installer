#!/usr/bin/python3
#
# hi_yaml_tools.py
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

"""
This file is a work in progress. The hope is that this will be integrated into the current tooling to provide
streamlined access to the various yaml files that are used.

Currently used yaml files:
	Homestead.yaml - Default config file for Laravel Homestead

Future yaml files:
	~/.homestead_installer/config.yaml - Config file for this project, homestead_installer
"""

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap as cmap
import os

yaml = YAML()


class HomesteadInstallerConfig:
	"""
	The config file this is meant to configure does not exist yet. Design work will commence shortly.
	"""
	def __init__(self, filepath=os.environ['HOME']+'/.homestead_installer/config.yaml'):
		self._filepath = filepath

	def getFilePath(self):
		return self._filepath

	def setFilePath(self, newPath):
		self._filepath = newPath
		return self._filepath


class HomesteadConfig:
	def __init__(self, filepath=os.environ['HOME']+'/Homestead/Homestead.yaml'):
		self._filepath = filepath
		self._file_contents = self._read_file()
		self._yaml_contents = yaml.load(self._file_contents)

	def _load_file_contents(self):
		self._file_contents = self._read_file()
		self._yaml_contents = yaml.load(self._file_contents)

	def _write_yaml(self):
		contents_file = open(self._filepath, 'w')
		yaml.dump(self._yaml_contents, contents_file)
		contents_file.close()
		self._load_file_contents()

	def _read_file(self):
		contents_file = open(self._filepath, 'r')
		contents = contents_file.read()
		contents_file.close()
		return contents

	def get_file_path(self):
		return self._filepath

	def set_file_path(self, newPath):
		self._filepath = newPath
		return self._filepath

	def get_yaml_contents(self):
		return self._yaml_contents

	def _get_info(self, arg_type):
		info = []
		for x in self._yaml_contents[arg_type]:
			info.append(x['map'])
		return info

	def _get_info_dict(self, arg_type):
		info = []
		for x in self._yaml_contents[arg_type]:
			info.append({x['map']: x['to']})
		return info

	def get_sites_dict(self):
		return self._get_info_dict('sites')

	def get_sites(self):
		return self._get_info('sites')

	def get_folders_dict(self):
		return self._get_info_dict('folders')

	def get_folders(self):
		return self._get_info('folders')

	def add_info(self, arg_type, *args):
		try:
			info = cmap(args)
			self._yaml_contents[arg_type].insert(len(self._yaml_contents[arg_type]), info)
		except KeyError:
			info = [cmap(args)]
			self._yaml_contents.insert(len(self._yaml_contents), arg_type, info)
		self._write_yaml()

	def remove_site(self, site_name):
		"""
		Remove a single specified site from the configuration. Reloads the current yaml info to reflect changes
		:param site_name: url of the website you would like to remove
		:return: None
		"""
		# TODO: Find a more pythonic way of doing this. Use of index values is undesirable.
		sites = self.get_sites()
		if not site_name in sites:
			print('Specified site is not valid. Check: ', self._filepath)
		else:
			for i in range(0, len(sites), 1):
				if sites[i] == site_name:
					del self._yaml_contents['sites'][i]
					self._write_yaml()

	def add_site(self, *args):
		"""
		Adds any number of websites to the Homestead.yaml file
		:param args: Expects tuples in multiples of two. Must be formatted as such:
						example.add_site(('map', '<site name>'), ('to', '<path to public folder of website>'))
						or
						example.add_site(('map', 'gabe.app'), ('to', '/home/vagrant/Code/Personal/gabe/public'))
		"""
		if len(args) %2 == 0:
			self.add_info('sites', *args)
		else:
			print('Key value mismatch')

	def update_memory(self, new_value=1024):
		self._yaml_contents['memory'] = new_value
		self._write_yaml()

	def update_cpus(self, new_value=1):
		self._yaml_contents['cpus'] = new_value
		self._write_yaml()