# A Trial IReporter plugin that gathers code-coverage information.

from twisted.trial.reporter import TreeReporter, VerboseTextReporter
from twisted.scripts.trial import getTestModules
import os

import figleaf
figleaf.start()


def percent(a, b):
    return int((float(a) / float(b)) * 100)


class TreeCoverageReporter(TreeReporter):

    def __init__(self, *args, **kwargs):
        TreeReporter.__init__(self, *args, **kwargs)
        self.trouchedMap = {}
        self.moduleFilenameMap = {}
        
    def _gatherFiles(self, coverageMap):
        """Gather information about what files belongs to which test
        modules.
        """
        for filename, lines in coverageMap.iteritems():
            if filename in self.trouchedMap:
                continue
            self.trouchedMap[filename] = True
            # gather test modules for the file.
            try:
                for module in getTestModules(filename):
                    if not module in self.moduleFilenameMap:
                        self.moduleFilenameMap[module] = list()
                    self.moduleFilenameMap[module].append(
                        filename
                        )
            except IOError:
                continue

    def _getFileCoverage(self, filename, coverageMap=None):
        """Return coverage information about file specified by
        filename.
        """
        if coverageMap is None:
            coverageMap = figleaf.get_info()
        num_total, num_covered = 0, 0,
        lines = figleaf.get_lines(open(filename))
        for i, line in enumerate(open(filename)):
            if (i + 1) in coverageMap[filename]:
                num_total += 1
                num_covered += 1
            elif (i + 1) in lines:
                num_total += 1
        return num_covered, num_total

    def _getModuleCoverage(self, module):
        """Yield coverage for files that belongs to module.
        """
        coverageMap = figleaf.get_info()
        self._gatherFiles(coverageMap)
        if module in self.moduleFilenameMap:
            for filename in sorted(self.moduleFilenameMap[module]):
                try:
                    yield filename, self._getFileCoverage(filename,
                                                          coverageMap)
                except IOError:
                    continue
        # done

    def printCoverageSummary(self, testModule):
        """Print coverage summary for test module.  
        """
        root = os.path.abspath('.')
        if root.endswith('_trial_temp'):
            root = root[:-12]
        linesCovered, linesTotal, files = 0, 0, 0
        printedBanner = False
        for file, (c, t) in self._getModuleCoverage(testModule):
            if not printedBanner:
                self._write('  Test Coverage:\n')
                printedBanner = True
            if file.startswith(root):
                file = file[len(root) + 1:]
            self._write('    %s ...' % file)
            color = 'green'
            if c == t:
                coverage = 'OK'
            else:
                pcnt = percent(c, t)
                coverage = '%2d%%' % pcnt
                if pcnt < 90:
                    color = 'blue'
                if pcnt < 50:
                    color = 'red'
            self.endLine('[%s]' % coverage, color)
            linesCovered += c
            linesTotal += t
            files += 1
        if linesCovered or linesTotal:
            self._write('  In total %d%% covered of %d file%s\n' % (
                percent(linesCovered, linesTotal), files, files > 1 and 's' or '')
                       )

    def _testPrelude(self, test):
        """Print prelude to a test.
        """
        if self._lastTest:
            segments = self._getPreludeSegments(test)
            if segments[0] != self._lastTest[0]:
                # print test coverage for last test module.
                self.printCoverageSummary(str(self._lastTest[0]))
        TreeReporter._testPrelude(self, test)

    def _printErrors(self):
        """Print errors.
        """
        # Also print test coverage for the final test module, if any
        # tests has been executed.
        if self._lastTest:
            self.printCoverageSummary(str(self._lastTest[0]))
        TreeReporter._printErrors(self)

    def _printSummary(self):
        figleaf.stop()
        return TreeReporter._printSummary(self)
        

