from setuptools import setup, find_packages

setup(name='ninja_ide.contrib.plugins.plugin_creator',
      version='0.1.1',
      keywords="ninja_ide plugin",
      url="www.ninja-ide.org",
      download_url="www.ninja-ide.org",
      license="GPLv3",
      author='Horacio Duran',
      author_email='perrito@ninja-ide.org',
      maintainer='Horacio Duran',
      maintainer_email='perrito@ninja-ide.org',
      description="Plugin To help create ninja plugins",
      long_description="""This plugin provides a "plugin type" that helps you bootstrap plugin folders creating all the structure and required files to add your own extension to ninja""",
      namespace_packages=['ninja_ide', 'ninja_ide.contrib',
                          'ninja_ide.contrib.plugins'],
      packages=find_packages(),
      )

"""
Metadata-Version: 1.1
Name: ninja_ide.contrib.plugins.plugin_creator
Version: 0.1
Author: Horacio Duran
Author-email: perrito at ninja-ide org
Maintainer: Horacio Duran
Maintainer-email: perrito at ninja-ide org
Home-page: www.ninja-ide.org
Download-url: http://www.ninja-ide.org
Summary: Plugin To help create ninja plugins
License: GPL-V3
Description: This plugin provides a "plugin type" that helps you bootstrap plugin folders creating all the structure and required files to add your own extension to ninja
Keywords: ninja_ide plugin
Platform: NinjaIDE
"""