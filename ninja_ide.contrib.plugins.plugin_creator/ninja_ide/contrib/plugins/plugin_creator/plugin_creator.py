# -*- coding: utf-8 -*-
#
# This file is part of NINJA-IDE (http://ninja-ide.org).
#
# NINJA-IDE is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# NINJA-IDE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NINJA-IDE; If not, see <http://www.gnu.org/licenses/>.
import os

from ninja_ide.core.nenvironment.encapsulated_env.nenvironment import BasePlugin
from ninja_ide.core.template_registry.bundled_project_types import PythonProject


BASE_NAME = r"ninja_ide.contrib.plugins.%s"
BASE_SETUP = \
    r"""from setuptools import setup, find_packages

setup(name='%s',
      version='%s',
      namespace_packages=['ninja_ide','ninja_ide.contrib',
          'ninja_ide.contrib.plugins'],
      packages=find_packages(),
      )
"""
BASE_INIT = \
    r"""import pkg_resources
pkg_resources.declare_namespace(__name__)"
"""
BASE_PLUGIN_INIT = \
    r"""#You should import the module here and add it to __all__
from .<plugin_file> import <exported_api>
__all__ = ["<exported_api>",]
def activate():
    print("Here add activation process from you module")
"""


class NinjaPluginProjectType(PythonProject):

    type_name = "Ninja Plugin"
    layout_version = "0.1"
    category = "Ninja"
    description = "This is the base layout for creating ninja plugins"

    def __init__(self):
        super(NinjaPluginProjectType, self).__init__()
        PluginCreatorPlugin.register()

    def create_layout(self):
        """
        ninja_ide/
            __init__.py
            contrib/
                __init__.py
                plugins/
                    __init__.py
                    yourpluginname/
                        __init__.py
                        yourcode.py
        """
        deeper_path = os.path.join("ninja_ide", "contrib", "plugins",
                                   self.name)
        self._create_path(deeper_path)

        filepath = os.path.join("ninja_ide", "setup.py")
        rendered_name = BASE_NAME % self.name
        rendered_setup = BASE_SETUP % (rendered_name, "0.1")
        self._create_file(filepath, rendered_setup)

        filepath = os.path.join("ninja_ide", "__init__.py")
        self._create_file(filepath, BASE_INIT)
        filepath = os.path.join("ninja_ide", "contrib", "__init__.py")
        self._create_file(filepath, BASE_INIT)
        filepath = os.path.join("ninja_ide", "contrib", "plugins",
                                "__init__.py")
        self._create_file(filepath, BASE_INIT)

        filepath = os.path.join("ninja_ide", "contrib", "plugins",
                                self.name, "__init__.py")
        self._create_file(filepath, BASE_PLUGIN_INIT)


class PluginCreatorPlugin(BasePlugin):

    def __init__(self):
        super(PluginCreatorPlugin, self).__init__()

    def activate(self):
        NinjaPluginProjectType.register()

