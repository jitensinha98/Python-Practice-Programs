def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def multiply(a,b):
    c=a*b
    return c
def divide(a,b):
    c=a/b
    return c

age=add(12,2)
height=sub(14,2)
weight=multiply(2,2)
iq=divide(2,2)

print "Age=%d"%age
print "Height=%d"%height
print "Weight=%d"%weight
print "iq=%d"%iq

p=add(age, sub(height, multiply(weight, divide(iq, 2))))

print "Abnormal=%d"%p
            
