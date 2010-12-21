txcovreport
===========

This is a simple reporter plugin for Twisted's trial unittest tool.
Provided that you have "test-case-name" meta-variables in your files,
like Twisted do, you can get per-file coverage reports.

Tested with twisted 10.0


See the transcript below for more information:


$ head -2 xkaron/wsgi.py
# -*- test-case-name: xkaron.test.test_wsgi -*-

$ trial --reporter=tree-coverage xkaron.test
xkaron.test.test_wsgi
  WSGIGatewayTestCase
    test_bad_request_method ...                                            [OK]
  Test Coverage:
    xkaron/wsgi.py ...                                                    [29%]
  In total 29% covered of 1 file

-------------------------------------------------------------------------------
Ran 1 tests in 0.024s

PASSED (successes=1)


