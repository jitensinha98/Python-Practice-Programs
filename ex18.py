def print_two(*args):
    arg1,arg2=args
    print "arg1=%r , arg2=%r"%(arg1,arg2)
    
def print_two_directly(arg1,arg2):
    print "arg1=%r , arg2=%r"%(arg1,arg2)

def print_one(arg1):
    print "arg1=%r"%arg1
    
def print_none():
    print "Nothing is there."
    
print_two("Jiten","Sinha")
print_two_directly('Jiten','Sinha')
print_one('Jiten')
print_none()

