people= int(input('enter people: '))
cats= int(input('enter cats: '))
dogs= int(input('enter dogs: '))

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")