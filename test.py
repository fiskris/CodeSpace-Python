# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
#checking order of numbers
x = int(input("Input first number:"))
y = int(input("Input second number:"))
z = int(input("Input third number:"))
if x < y and y < z :
 print("Increasing order")  # Press Ctrl+F8 to toggle the breakpoint.
elif x > y and y > z :
    print("Decreasing order")
else:
    print("Neither increasing or decreasing order")
"""
"""
# Fibonacci series between 0 to 50
a = 0
b = 1
print(a)
print(b)
while b <51:
    x = b
    b += a
    a = x
    if b>=50:
        break
    print(b)
"""

"""
#multiplication table
a = int(input("Input a number:"))
for x in range(1, 11):
  print("%d x %d = %d" % (a, x, a*x))
"""
"""
#Activity 5.1 - sum of the lists elements
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y=0
for x in myList:
    y+=x
print(y)
"""
"""
#Activity 5.2 - average value of a list elements
myList1 = [20, 30, 25, 35, -16, 60, -100]
y=0
for x in myList1:
    y+=x
print(y)
print("Average value of the list elements is : %.1f" % (y / (len(myList1))))
"""
"""
fname = input("What's your first name?")
sname = input("What's your surname?")
print(fname +" " + sname)
"""
"""
#Activity 5.3 -  program to find the maximum and minimum value of a list

myList2 = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
print("Original List:  %s " % myList2)
myList2.sort(reverse=False)
print("Sorted List:  %s " % myList2)
print("Maximum value for the above list:  %d " % (myList2[len(myList2)-1]))
print("Minimum value for the above list:  %d " % (myList2[0]))
"""
"""
#Activity 6.1 -  2 Python functions to show the list content & find the max value in the list
def my_function(lista):
 # for x in lista:
    print("The content of the list is: %s" % lista)
def max_function(lista):
    lista.sort(reverse=True)
    print("The max value in the list: %d" % lista[0])
myList3 =  [10, 2, 3, 4, 7]
my_function(myList3)
max_function(myList3)
"""

"""
#Activity 6.2 - function to calculate the factorial of a number
def factorial_function(num):
    if num < 0:
        print ("Factorial can be calculated only for positive numbers" )
    elif num == 0:
        print("the factorial of %d is 1" % num)
    else:
        factor=1
        for x in range(1, num+1):
            factor *=x
        print( "Factorial of %d: %d! = %d" % (num, num, factor))
x = int(input("Input a number:"))
factorial_function(x)

"""
"""
#adding 2 numbers
numOne = float(input("podaj liczbe:"))
numTwo = float(input("podaj druga liczbe:"))
suma = numOne + numTwo
print("wynik dodawania: %f.4 + %.4f = %.4f" % (numOne, numTwo, suma))
"""
"""
#Activity 6.3 - function that check if the number is prime or not
def checkprime(check_no):
 if check_no < 1:
     print("Your number: %d. It is not a prime number" % check_no)
 elif check_no == 1:
     print("your no: %d.  It is a prime number" % check_no)
 else:
     i = 2
     while check_no%i != 0 and i < check_no:
         i +=1
     print("next after 1 factor of %d is %d" % (check_no, i))
     if i == check_no:
         print("your no: %d.  It is a prime number" % check_no)
     else:
         print("Your number: %d. It is not a prime number" % check_no)

x = int(input("your number? "))
checkprime(x)
"""

# Generate random list of 5 values between 1 and 30

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
