import sys

print('Arguments:', len(sys.argv))
print('List:', str(sys.argv))

if sys.argv < 2:
    print('To few arguments, please specify a filename')

filename = sys.argv[1]
print('Filename:', filename)

#output
$ python ex13.py
Arguments: 1
List: ['ex13.py']

$ python ex13.py karthik
Arguments: 2
List: ['ex13.py', 'karthik']
   
