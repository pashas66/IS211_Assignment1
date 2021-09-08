# Week 1 Assignment - Part 1

# The function returns the number of elements in the numbers list that are divisible by "divide". 

def listDivide(numbers=[], divide=2): #creating a function called listDivide that takes in 2 parameters: numbers & divide (where divide is set to 2)
    divisibilityCount=0 #initializing it to 0 because we always start a # from 0.
    for i in numbers: #this is a for loop to check if the elements are divisible 
        remainder = i % divide #we use mod to find the remainder in this case "%"
        if remainder == 0: #set remainder to 0
            divisibilityCount=divisibilityCount+1 #if it is divisible then increase it by 1 
    return divisibilityCount #then return the function

# A custom exception class called "ListDivideException" to be raised when errors are occured in the program
class ListDivideException(Exception):
    pass

#Creating a another function called "testListDivide"  to performs various tests cases on "listDivide" function
#The listDivide function that does not return anything if the output is valid. However, if the output has an error, it will then raise the exception.

#the test cases are provided from the document

def testListDivide():
    test1 = listDivide([1, 2, 3, 4, 5]) #there are 5 numbers here and 2 is our default value. In the 2nd and 4th spot there is '2' and '4' numbers. 
    if test1 != 2: #since 2 is divisble by 2 and 4 it should return 2 
        raise ListDivideException("Test 1 Error") #if there's an error it will rais an exception and print the following message.
    test2 = listDivide([2,4,6,8,10]) #here all 5 numbers are divisible by 2 
    if test2 != 5: #therefore, we return 5
        raise ListDivideException("Test 2 Error")
    test3 = listDivide([30, 54, 63, 98, 100], divide=10) #here we divide by 10 instead of 2
    if test3 !=2:
        raise ListDivideException("Test 3 Error")
    test4 = listDivide([])
    if test4 != 0:
        raise ListDivideException ("Test 4 Error")
    test5 = listDivide([1,2,3,4,5], 1)
    if test5 != 5:
        raise ListDivideException ("Test 5 Error")

testListDivide()
