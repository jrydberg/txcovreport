#!/usr/bin/env python

import sys
from distutils.core import setup

setup(name='covreport',
      version='0.0',
      description='Trial Reporter that prints some coverage rports',
      author='Johan Rydberg',
      author_email='johan.rydberg@gmail.com',
      url='http://www.edgeware.tv/',
      packages=['txcovreport', 'twisted.plugins'],
      package_data={'twisted': ['plugins/figleaf_plugin.py'],},
      install_requires=['Twisted', 'figleaf'],
     )
