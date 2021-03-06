from com.scripts.script_01 import *
from com.scripts.script_03 import *
from com.scripts.script_02 import *

import HTMLTestRunner

class Suite(unittest.TestCase):

    def test_main(self):
        logging.info('Inside test suite')
        self.suite = unittest.TestSuite([unittest.defaultTestLoader.loadTestsFromTestCase(Men),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Sports),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Women),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(Kids),
                                         unittest.defaultTestLoader.loadTestsFromTestCase(SignIn)])

        outputfile = open("D:\Work_Space\Framework_Jabong\Reports\HTML Report\TestReport.html", "w")
        runner = HTMLTestRunner.HTMLTestRunner(stream=outputfile,title='Execution Report',description='Suite Run')
        runner.run(self.suite)

#import unittest
#if __name__=="__main__":
#    unittest.main