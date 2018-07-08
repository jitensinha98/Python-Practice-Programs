from sys import argv
from os.path import exists

Script,from_file,to_file=argv

print "Copying From %r to %r"%(from_file,to_file)

x=open(from_file)
y=x.read();

print "The Source file is %r bits long."%len(y)
print "Does the target file exists ? %r."%exists(to_file)
print "Copying Content....."

p=open(to_file,'w');
p.write(y);

p.close()
x.close()

print "Done."
