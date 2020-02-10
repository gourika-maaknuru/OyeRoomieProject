__author__ = 'Gourika Maaknuru'

import sys
import os
sys.path.append(os.path.abspath('../../'))

from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_Oyeroomie_HomePage import Oyeroomie_HomePage
from Test.Scripts.test_Oyeroomie_PostAdPage import Oyeroomie_PostAdPage
import testtools as testtools
import HtmlTestRunner

if __name__ == '__main__':

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(Oyeroomie_HomePage),
        loader.loadTestsFromTestCase(Oyeroomie_PostAdPage)
      ))


# Run Tests Sequentially #

    #runner = TextTestRunner(verbosity=2)
    #runner.run(suite)

 #run test parallel using concurrent_suite, but output result data gets overlapped
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())
