#!/usr/bin/env python3
# Student ID: [seneca_id]

def function1():
    global schoolName
    schoolName = 'SICT'  # Modify the global variable
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'  # Modify the global variable
    print('print() in function2 on schoolName:', schoolName)

# Global scope
schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)

