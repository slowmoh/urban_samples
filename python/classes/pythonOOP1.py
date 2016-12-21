# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:23:27 2016
https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
@author: Ben
"""

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '_@company.com'
      
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
#emp_1 = Employee()
emp_2 = Employee('adam', 'curry', 50000)

#print(emp_1)
print(str(emp_2.first))
print(emp_2.fullname())
print(Employee.fullname(emp_2))

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

#emp_1.first = 'Coprey'
#emp_1.last = 'Scafer'
#emp_1.email = 'curey.schafer'
#emp_1.pay = 40000