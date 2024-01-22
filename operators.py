#Arithmetic operators

#addition operator
a=1
b=2
c= a+b
print(c)

#subtraction operator

a=4
b=3
c=a-b
print(c)

#multiplication operator

a=3
b=3
c=a * b
print(c)

#Division operator

a=5
b=4
c= a / b
print(c)

#Modulus operator

a=6
b=3

c= a%b
print(c)

#Exponentiation operator

a=2
b=3
c=a**b
print(c)

#Floor division

a=10
b=4
c=a//b
print(c)

#Logical Operator

#AND operator
# Python program to demonstrate 
# logical and operator 
a = 10
b = 10
c = -10
if a > 0 and b > 0: 
	print("The numbers are greater than 0") 
if a > 0 and b > 0 and c > 0: 
	print("The numbers are greater than 0") 
else: 
	print("Atleast one number is not greater than 0")

#OR Operator
	
# Python program to demonstrate 
# logical or operator 
a = 10
b = -10
c = 0
if a > 0 or b > 0: 
	print("Either of the number is greater than 0") 
else: 
	print("No number is greater than 0") 
if b > 0 or c > 0: 
	print("Either of the number is greater than 0") 
else: 
	print("No number is greater than 0")
	

#NOT Operator
	
# Python program to demonstrate 
# logical not operator 
a = 10

if not a: 
	print("Boolean value of a is True") 
if not (a%3 == 0 or a%5 == 0): 
	print("10 is not divisible by either 3 or 5") 
else: 
	print("10 is divisible by either 3 or 5")



#practice for all operators
num1 = 15
num2 = 5
sum = num1 + num2 
difference = num1 - num2 
product = num1 * num2 
quotient = num1 / num2 
remainder = num1 % num2 
print("Sum:", sum) 
print("Difference:", difference) 
print("Product:", product) 
print("Quotient:", quotient) 
print("Remainder:", remainder)



# Python code to demonstrate working of 
# add(), sub(), mul() 

# importing operator module 
import operator 

# Initializing variables 
a = 4

b = 3

# using add() to add two numbers 
print ("The addition of numbers is :",end=""); 
print (operator.add(a, b)) 

# using sub() to subtract two numbers 
print ("The difference of numbers is :",end=""); 
print (operator.sub(a, b)) 

# using mul() to multiply two numbers 
print ("The product of numbers is :",end=""); 
print (operator.mul(a, b)) 


# Python code to demonstrate working of 
# truediv(), floordiv(), pow(), mod() 

# importing operator module 
import operator 

# Initializing variables 
a = 5

b = 2

# using truediv() to divide two numbers 
print ("The true division of numbers is : ",end=""); 
print (operator.truediv(a,b)) 

# using floordiv() to divide two numbers 
print ("The floor division of numbers is : ",end=""); 
print (operator.floordiv(a,b)) 

# using pow() to exponentiate two numbers 
print ("The exponentiation of numbers is : ",end=""); 
print (operator.pow(a,b)) 

# using mod() to take modulus of two numbers 
print ("The modulus of numbers is : ",end=""); 
print (operator.mod(a,b)) 


# Python code to demonstrate working of 
# lt(), le() and eq() 

# importing operator module 
import operator 

# Initializing variables 
a = 3

b = 3

# using lt() to check if a is less than b 
if(operator.lt(a,b)): 
	print ("3 is less than 3") 
else : print ("3 is not less than 3") 

# using le() to check if a is less than or equal to b 
if(operator.le(a,b)): 
	print ("3 is less than or equal to 3") 
else : print ("3 is not less than or equal to 3") 

# using eq() to check if a is equal to b 
if (operator.eq(a,b)): 
	print ("3 is equal to 3") 
else : print ("3 is not equal to 3") 


# Python code to demonstrate working of 
# gt(), ge() and ne() 

# importing operator module 
import operator 

# Initializing variables 
a = 4

b = 3

# using gt() to check if a is greater than b 
if (operator.gt(a,b)): 
	print ("4 is greater than 3") 
else : print ("4 is not greater than 3") 

# using ge() to check if a is greater than or equal to b 
if (operator.ge(a,b)): 
	print ("4 is greater than or equal to 3") 
else : print ("4 is not greater than or equal to 3") 

# using ne() to check if a is not equal to b 
if (operator.ne(a,b)): 
	print ("4 is not equal to 3") 
else : print ("4 is equal to 3") 


# Python code to demonstrate working of 
# setitem(), delitem() and getitem() 

# importing operator module 
import operator 

# Initializing list 
li = [1, 5, 6, 7, 8] 

# printing original list 
print ("The original list is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using setitem() to assign 3 at 4th position 
operator.setitem(li,3,3) 

# printing modified list after setitem() 
print ("The modified list after setitem() is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using delitem() to delete value at 2nd index 
operator.delitem(li,1) 

# printing modified list after delitem() 
print ("The modified list after delitem() is : ",end="") 
for i in range(0,len(li)): 
	print (li[i],end=" ") 

print ("\r") 

# using getitem() to access 4th element 
print ("The 4th element of list is : ",end="") 
print (operator.getitem(li,3)) 


# Python code to demonstrate working of 
# concat() and contains() 

# importing operator module 
import operator 

# Initializing string 1 
s1 = "geeksfor"

# Initializing string 2 
s2 = "geeks"

# using concat() to concatenate two strings 
print ("The concatenated string is : ",end="") 
print (operator.concat(s1,s2)) 

# using contains() to check if s1 contains s2 
if (operator.contains(s1,s2)): 
	print ("geeksfor contains geeks") 
else : print ("geeksfor does not contain geeks") 


# Python code to demonstrate working of 
# and_(), or_(), xor(), invert() 

# importing operator module 
import operator 

# Initializing a and b 

a = 1

b = 0

# using and_() to display bitwise and operation 
print ("The bitwise and of a and b is : ",end="") 
print (operator.and_(a,b)) 

# using or_() to display bitwise or operation 
print ("The bitwise or of a and b is : ",end="") 
print (operator.or_(a,b)) 

# using xor() to display bitwise exclusive or operation 
print ("The bitwise xor of a and b is : ",end="") 
print (operator.xor(a,b)) 

# using invert() to invert value of a 
operator.invert(a) 

# printing modified value 
print ("The inverted value of a is : ",end="") 
print (operator.invert(a)) 

#DATA TYPES

#Numeric
#type() function
a = 5
print("Type of a: ", type(a)) 

b = 5.0
print("\nType of b: ", type(b)) 

c = 2 + 4j
print("\nType of c: ", type(c)) 

#SEQUENCE DATA TYPES
#String

String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ") 
print(String1) 
print(type(String1)) 
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ") 
print(String1) 
print(type(String1)) 

String1 = '''Geeks 
			For 
			Life'''
print("\nCreating a multiline String: ") 
print(String1) 


#LIST

List = [] 
print("Initial blank List: ") 
print(List) 
List = ['GeeksForGeeks'] 
print("\nList with the use of String: ") 
print(List) 
List = ["Geeks", "For", "Geeks"] 
print("\nList containing multiple values: ") 
print(List[0]) 
print(List[2]) 
List = [['Geeks', 'For'], ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List[0][1])

#TUPLE 

Tuple1 = () 
print("Initial empty Tuple: ") 
print(Tuple1) 
Tuple1 = ('Geeks', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 
Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(Tuple1) 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'geek') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 

#Accessing tuple elements

tuple1 = tuple([1, 2, 3, 4, 5]) 
print("First element of tuple") 
print(tuple1[0]) 
print("\nLast element of tuple") 
print(tuple1[-1]) 

print("\nThird last element of tuple") 
print(tuple1[-3]) 


#SETS

set1 = set() 
print("Initial blank Set: ") 
print(set1) 
set1 = set("ChauhanPrrince") 
print("\nSet with the use of String: ") 
print(set1) 
set1 = set(["same", "For", "same"]) 
print("\nSet with the use of List: ") 
print(set1) 
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks',3+4j,'you']) 
print("\nSet with the use of Mixed Values") 
print(set1) 

#Accessing set items
set1 = set(["Geeks", "For", "Geeks"]) 
print("\nInitial set") 
print(set1) 
print("\nElements of set: ") 
for i in set1: 
	print(i, end=" ") 
print("Geeks" in set1) 



#DICTIONARY

Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


#Accessing dict
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
print("Accessing a element using key:") 
print(Dict['name']) 
print("Accessing a element using get:") 
print(Dict.get(3)) 
