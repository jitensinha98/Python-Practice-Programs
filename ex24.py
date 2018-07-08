from os.path import exists

print 'You\'d know about escape sequences by now//'

x= """
\nYou Brought me Sunshine
when I only saw rain.
You brought me laughter
when I only felt pain.\n
\t -Jiten Sinha\n
"""

print "-"*30
print x
print "-"*30

five=1+3+1

print "Five=%d"%five

def secret(quantity):
    chese=quantity/2
    cakes=quantity*4
    candy=quantity-(quantity/2)
    return chese,cakes,candy
  
startpoint=1000
chese,cakes,candy=secret(startpoint)

print "Cheese=%d\nCakes=%d\nCandy=%d"%(chese,cakes,candy)

print "Reducing quantity by half"
startpoint=startpoint/2

chese,cakes,candy=secret(startpoint)

print "Cheese=%d\nCakes=%d\nCandy=%d\n"%(chese,cakes,candy)

print "Another cool thing is i can open edit and copy files in this program "
print "Press Ctrl+c to exit OR ENTER to continue...."
raw_input("\n")

file1=raw_input("Enter File name to veiw the file :")
x=open(file1)
p=x.read()

print "The content of %r is..\n"%file1
print p

file2=raw_input("Enter another file to copy the contents of the previous file : ")
y=open(file2,'w')
y.truncate()
y.write(p)

x.close()
y.close()

print"\n Done"





