#Using argument to pass the value of variables

from sys import argv
Script,File =argv

text1=open(File)
print "-"*30
print "The requested File is:"
print "-"*30
print text1.read()
print "-"*30

#Using raw input to pass the value of variables

Filename=raw_input("Enter the filename :")
text=open(Filename)
print "-"*30
print "The requested File is :"
print "-"*30
print text.read()
print "-"*30

