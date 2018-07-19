# Vowels

vowel=['a','e','i','o','u']
count=0
word=input("enter a word:")
for letter in word:
    if letter in vowel:
    	count=count+1               
print(count)

#Pattren:  

count=1
for i in range(0,5):
    for j in range(0,count):
        print("*",end="")
    count=count+1
    print("\r")
    
# BMI Calculator
    
height = float(input("Your height in metres:"))
weight = int(input("Your weight in kilograms:"))
bmi = round(weight/ (height * height), 1)

if bmi <= 18.5:
     print('Your BMI is', bmi, 'which means you are underweight.')

elif bmi > 18.5 and bmi < 25:
     print('Your BMI is', bmi, 'which means you are normal.')

elif bmi > 25 and bmi < 30:
     print('Your BMI is', bmi, 'which means you are overweight.')

elif bmi > 30:
     print('Your BMI is', bmi, 'which means you are obese.')

else:
    print('There is an error with your input')

# Sort a words using split()

sentence=input("enter a words:")
word=sentence.split()
word.sort()
for i in word:
    print(i)
    
# Factorial

n =int(input("enter a number:"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)
