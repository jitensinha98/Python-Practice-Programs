numbers=[]
p=int(raw_input("Enter Limit:"))
c=int(raw_input("Enter incrementation:"))

def input(x,counter):
   # i=0
   # while i<x:
    #    numbers.append(i)
     #   i=i+c
    for i in range(0,x,counter):
        numbers.append(i)
       

input(p,c)    
print "Displaying the Numbers :"
for num in numbers:
    print num
   
