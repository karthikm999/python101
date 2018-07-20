True and True
1 == 1 and 2 == 2
#output
True

x = True
y = False
print('x and y is',x and y)
# Output: x and y is False

print('x or y is',x or y)
# Output: x or y is True

print('not x is',not x)
# Output: not x is False

Membership operators

a = True
b = False
print('a and b is',a and b)
#output: a and b is False
print('a or b is',a or b)
#output: a or b is True
print('not a is',not a)
#output: not a is False

#Membership Operators
x = 7
y = 3
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print("Line 1 - x is available in the given list")
else:
   print("Line 1 - x is not available in the given list")
if ( y not in list ):
   print("Line 2 - y is not available in the given list")
else:
   print("Line 2 - y is available in the given list")
   
#output: 
Line 1 - x is not available in the given list
Line 2 - y is available in the given list

Operators Summary:
#Arithmetic Operators
x= 6	
y= 9
print (x + y)
#output:
15

#Comparison Operators
x = 6
y = 9
print('x > y  is:',x>y)
#output: x>y is: True

#Assignment Operators
num1 = 9
num2 = 3
print ("Line 1 - Value of num1 : ", num1)
print ("Line 2 - Value of num2 : ", num2)
#output:
Line 1 - Value of num1 :  9
Line 2 - Value of num2 :  3

#compound assignment operator
num1 = 7 
num2 = 5
res = num1 + num2
res += num1
print ("Line 1 - Result of + is ", res)
#output:
Line 1 - Result of + is  19

#Logical Operators
a = True
b = False
print('a and b is',a and b)
#output: a and b is False
print('a or b is',a or b)
#output: a or b is True
print('not a is',not a)
#output: not a is False

#Identity Operators
x = 20
y = 20
if ( x is y ):
	print "x & y  SAME identity"
y=30
if ( x is not y ):
	print "x & y have DIFFERENT identity"
#output:
x & y  SAME identity
x & y have DIFFERENT identity

#Operator precedence
v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;   
print ("Value of (v+w) * x/ y is ",  z)
#output:Value of (v+w) * x/ y is  36.0