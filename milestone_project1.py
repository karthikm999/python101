# Vowels
def vowel(str):
    str="I LikE PythOn"
    vowel=['a','e','i','o','u' or 'A','E','I','O','U']
    count=0
    for i in str:
        if i in vowel:
           count+=1
    print("No. of vowels:",count)
vowel(str)

#output: 
No. of vowels: 4

# if the word is "HellO wOrld"
#output:
No. of vowels: 3

#Pattren:  

def pattern(num):
    for i in range(0,num):
        for j in range(0,i+1):
            print(" *",end="")
        print("\n")
num=5
pattern(num)

#output:

 *

 * *

 * * *

 * * * *

 * * * * *

# if the num is 9
#output:
 *

 * *

 * * *

 * * * *

 * * * * *

 * * * * * *

 * * * * * * *

 * * * * * * * *

 * * * * * * * * *
    
# BMI Calculator
    
def bmi(height,weight):
    bmi = round(weight/ (height * height), 1)
    if bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi, 'which means you are normal.')
    elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi, 'which means you are overweight.')
    elif bmi > 30:
        print('Your BMI is', bmi, 'which means you are obese.')
    else:
        print('your weight is underweight')
height=5.3
weight=72
bmi(height,weight)

#output:your weight is underweight

# Sort a words using split()

def sort(sentence):   
    word.sort()
    for i in word:
        print(i)
sentence=("hi to the python world")
word=sentence.split() 
sort(sentence)

#output:
hi
python
the
to
world

    
# Factorial

def factorial(n):
    factorial = 1
    if n<0:
       print("factorial number doesnot exits")
    elif n==0:
       print("the factorial of 0 is 1")
    else:
       for i in range(factorial,n+1):
           factorial = factorial * i
    print("the factorial number of",n,"is:",factorial)
n = 7
factorial(n)

#output:
#the factorial number of 7 is: 5040

# reverse

def reverse(s):
    str = ""
    for i in word:
        str = i + str
    return str
word = ("hello world")
print(reverse(word))

#output:
# dlrow olleh

# remove punctuation

def punct(str):
    punct= '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
    no_punct=""
    for i in str:
        if i not in punct:
           no_punct=no_punct+i
    print(no_punct)
str=("Hello! #$ Wor*l@d")
punct(str)

#output:
Hello  World
