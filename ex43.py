def add(x,y):
    z=x+y
    print "Addition of %d and %d is %d."%(x,y,z)
def sub(x,y):
    z=x-y
    print "Subtraction of %d and %d is %d."%(x,y,z)
def multiply(x,y):
    z=x*y
    print "Multiplication of %d and %d is %d."%(x,y,z)
    
x=int(raw_input("Enter a number :"))
y=int(raw_input("Enter another number :"))
add(x,y)
sub(x,y)
multiply(x,y)
