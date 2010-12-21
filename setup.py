#!/usr/bin/env python

import sys
from distutils.core import setup

try:
    import twisted
except ImportError:
    raise SystemExit("twisted not found.  Make sure you "
                     "have installed the Twisted core package.")

setup(name='covreport',
      version='0.0',
      description='Trial Reporter that prints some coverage rports',
      author='Johan Rydberg',
      author_email='johan.rydberg@gmail.com',
      url='http://www.edgeware.tv/',
      packages=['txcovreport', 'twisted.plugins'],
      package_data={'twisted': ['plugins/figleaf_plugin.py']}
     )
