from sys import argv
Script,filename=argv
x=open(filename,'w')
x.truncate()
print "Enter:"
line1=raw_input("Line 1:")
line2=raw_input("Line 2:")
line3=raw_input("Line 3:")
print "Writing......"
x.write(line1)
x.write("\n")
x.write(line2)
x.write("\n")
x.write(line3)
