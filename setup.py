#!/usr/bin/env python

import sys
from distutils.core import setup

try:
    import twisted
except ImportError:
    raise SystemExit("twisted not found.  Make sure you "
                     "have installed the Twisted core package.")


def refresh_plugin_cache():
    from twisted.plugin import IPlugin, getPlugins
    list(getPlugins(IPlugin))


setup(name='covreport',
      version='0.0',
      description='Trial Reporter that prints some coverage rports',
      author='Johan Rydberg',
      author_email='johan.rydberg@gmail.com',
      url='http://www.edgeware.tv/',
      packages=['covreport', 'twisted.plugins'],
      package_data={'twisted': ['plugins/figleaf_plugin.py']}
     )
refresh_plugin_cache()
