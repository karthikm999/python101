Creating a tuple 
# An empty tuple
empty_tuple = ()
print (empty_tuple)
#output: ()

# Creating non-empty tuples

# One way of creation
tup = 'python', 'course'
print(tup)
#output: ('python', 'course')

# Another for doing the same
tup = ('python', 'geeks')
print(tup)
#output:('python', 'course')
	
Length of a Tuple
tuple2 = ('python', 'course')
print(len(tuple2))
#output:2

Concatenation of Tuples
# Code for concatenating 2 tuples

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'course')
print(tuple1 + tuple2)
#output: ('python', 'course', 0, 1, 2, 3)

Nesting of Tuples
# Code for creating nested tuples

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'course')
tuple3 = (tuple1, tuple2)
print(tuple3)
#output: (('python', 'course'), (0, 1, 2, 3))
	
Repetition in Tuples
# Code to create a tuple with repetition

tuple3 = ('python',)*3
print(tuple3)
#output: ('python', 'python', 'python')
tuple4 = ('python')*3
print(tuple4)
#output: pythonpythonpython
	
Immutable Tuples
#code to test that tuples are immutable

tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)
#output:
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-72-f091b5671c3e> in <module>()
----> 1 tup1[0]=4

TypeError: 'tuple' object does not support item assignment
---------------------------------------------------------------------------
	
Slicing in Tuples
# code to test slicing

tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
#output: (1,2,3)
print(tuple1[::-1])
#output: (3, 2, 1, 0)
print(tuple1[2:4])
#output: (2, 3)

Deleting a Tuple
# Code for deleting a tuple

tuple3 = ( 0, 1)
del tuple3
print(tuple3)

#Lets see how to delete a tuple
myTup = tuples = [('a', 9), ('b', 8), ('c', 7), ('d', 6), ('e', 5), ('f', 4), ('g', 3), ('h', 2), ('i', 1), ('j', 0)]
     

Converting list to a Tuple
# Code for converting a list and a string into a tuple

list1 = [0, 1, 2]
print(tuple(list1))
#output: (0, 1, 2)
print(tuple('python')) # string 'python'
#output: ('p', 'y', 't', 'h', 'o', 'n')