import unittest
import employee

#Test function for Net pay cannot exceed gross pay.
def testNetpayLessEqualGrosspay(self):
    ee = et.Employee(12345,'Green','Joe',37,16,1.5,72,710)
    return_value = ee.computePayment(1,'31/10/2021')
    self.assertLessEqual(return_value['Net Pay'],return_value['Gross Pay'])

#Test function for Overtime pay or overtime hours cannot be negative.
def testOvertimePayOvertimeHoursNotNegative(self):
   ee = et.Employee(12345,'Green','Joe',37,16,1.5,72,710)
   return_value = ee.computePayment(1,'31/10/2021')
   self.assertLessEqual(0, return_value['Overtime Pay'])
   self.assertLessEqual(0, return_value['Overtime Hours Worked'])
   
#Test Function for Regular Hours Worked cannot exceed hours worked
def testRegHoursExceedHourswork(self):
    ee = et.Employee(12345,'Green','Joe',37,16,1.5,72,710)
    return_value = ee.computePayment(1,'31/10/2021')
    self.assertLessEqual(return_value['Regular Hours Worked'],return_value['Hours Worked'])

#Test Function for Higher Tax cannot be negative.
def testHigherTaxCannotNegative(self):
    ee = et.Employee(12345,'Green','Joe',37,16,1.5,72,710)
    return_value = ee.computePayment(1,'31/10/2021')
    self.assertLessEqual(0, return_value['Higher Tax'])

#Test Function for Net Pay cannot be negative.
def testNetPayCannotNegative(self):
    ee = et.Employee(12345,'Green','Joe',37,16,1.5,72,710)
    pi = ee.computePayment(1,'31/10/2021')
    self.assertLessEqual(0, pi['Net Pay'])
unittest.main(argv=['ignored'],exit=False)