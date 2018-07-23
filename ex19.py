# empty list
my_list_1 = []
print(my_list_1)
#output: []

# list of integers
my_list_2 = [1, 2, 3]
print(my_list_2)
#output: [1,2,3]

# list with mixed datatypes
my_list_3 = [1, "Hello", 3.4]
print(my_list_3)
#output: [1, 'hello', 3.4]

# nested list
my_list_4 = ["mouse", [8, 4, 6], ['a']]
print(my_list_4)
#output: ['mouse', [8, 4, 6], ['a']]

#accessing elements in the list

my_list = ['p','y','t','h','o','n']
print(my_list[0])
print(my_list[2])
print(my_list[4])
#output:
p
t
o

# Error! Only integer can be used for indexing
my_list[4.0]
#output:
p
t
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-11-471e06ae0776> in <module>()
      2 print(my_list[0])
      3 print(my_list[2])
----> 4 print(my_list[4.0])

TypeError: list indices must be integers or slices, not float
---------------------------------------------------------------------------

# Nested List
n_list = ["Happy", [2,0,1,5]]
# Nested indexing
print(n_list[0][1])    
print(n_list[1][3])
#output:
a
5

#Negative indexing
my_list = ['p','y','t','h','o','n']
print(my_list[-1])
print(my_list[-5])
#output:
n
y

my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])
#output:
['o', 'g', 'r']
['p', 'r', 'o', 'g']
['a', 'm', 'i', 'z']
['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']


#add or change values
# mistake values
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

# Output: [1, 4, 6, 8]
print(odd)
# Output: [1, 3, 5, 7]

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  
print(odd)   


#use list functions 
odd.append(7)
print(odd)
odd.extend([9, 11, 13])
print(odd)
print(my_list.pop(1))
# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'm'
print(my_list.pop())
# Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()


#Concatenation and repitation
odd = [1, 3, 5]
# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])
#Output: ["python", "python", "python"]
print(["python"] * 3)

#delete or remove elements from a list
my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)

# delete multiple items
del my_list[1:5]  
# Output: ['p', 'm']
print(my_list)
# delete entire list
del my_list2       
print(my_list2) # see whats the output
#output:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-23-7d351bb30efc> in <module>()
----> 1 my_list2

NameError: name 'my_list2' is not defined
---------------------------------------------------------------------------
