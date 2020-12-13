from calgrade import calgrade
import unittest

class Test_calGrade(unittest.TestCase):
    def testcalGradeA(self):
        self.assertEqual(calgrade(80),"A")

    def testcalGradeF(self):
        self.assertEqual(calgrade(49),"F")

    def testcalGradeC(self):
        self.assertEqual(calgrade(59),"D")

        # def testMultiplyFunction(self):
        # self.assertEqual(multiply(1,2),2)

        # def testDivideFunction(self)