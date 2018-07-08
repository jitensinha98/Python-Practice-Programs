from sys import argv
Script,Filename=argv
print "\n"
print "We are going to rewrite the content of a file in this program"
print "Press Ctrl+C to terminate OR press any key and hit enter to continue...."
raw_input(">")
print "The current content of the file is :"
print "-"*30
x=open(Filename)
print x.read()
print "-"*30
y=open(Filename,'w')
y.truncate()
print "Please type 3 line to be rewritten :"
line1=raw_input("Line 1:")
line2=raw_input("Line 2:")
line3=raw_input("Line 3:")
print "I am going to write these in the file..."
print "\n"
y.write(line1)
y.write("\n")
y.write(line2)
y.write("\n")
y.write(line3)
print "\n"
print "And finally we close it...."
y.close()
q=raw_input("Press Ctrl+C to terminate OR press any key and hit enter to reveiw the changes in the file :")
print "-"*30
print "The new content of the file is :"
print "-"*30
z=open(Filename)
print "-"*30
print z.read()
print "-"*30
