from setuptools import setup, find_packages

setup(name='ninja_ide.contrib.plugins.plugin_creator',
      version='0.1',
      keywords="ninja_ide plugin",
      namespace_packages=['ninja_ide', 'ninja_ide.contrib',
                          'ninja_ide.contrib.plugins'],
      packages=find_packages(),
      )