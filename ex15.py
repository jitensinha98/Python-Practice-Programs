from sys import argv
Script,Filename=argv

Veiw=open(Filename)

print "\n"
print "The requested File is :"
print "\n"
print Veiw.read()

text=raw_input("Please enter another filename :")
Veiw1=open(text)
print "\n"
print "The requested file is :"
print "\n"
print Veiw1.read()

