from sys import argv
Script,x=argv

f=open(x)

def print_all(f):
   print f.read()

def print_one_line(line_count,f):
    print line_count,f.readline();

def rewind(f):
    f.seek(0)
    
print_all(f)

rewind(f)

current_line=0
print_one_line(current_line,f)

current_line=current_line+1
print_one_line(current_line,f)

current_line=current_line+1
print_one_line(current_line,f)


