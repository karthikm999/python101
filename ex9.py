import cmath
a= float(input('enter a: '))
b= float(input('enter b: '))
c= float(input('enter c: '))
d= (b**2)-(4*a*c)
res1 =(-b-cmath.sqrt(d))/(2*a)
res2 =(-b+cmath.sqrt(d))/(2*a)
print('the solution are {0} and {1}'.format(res1,res2))

