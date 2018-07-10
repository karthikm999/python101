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