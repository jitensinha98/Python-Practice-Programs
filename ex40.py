from sys import argv
from os.path import exists

Script,from_file,to_file=argv

print "Copying content from %r to %r."%(from_file,to_file)

x=open(from_file)
y=x.read()

print "%r is %r bits long."%(from_file,len(y))
print "Does the target file exists ? %r."%exists(to_file)
print "Press Enter to continue and Ctrl+C to exit...."

raw_input()

print "Copying Files......"

p=open(to_file,'w')
p.write(y);

print "Done."

x.close()
p.close()
