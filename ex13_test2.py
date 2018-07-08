from sys import argv

Script_name,Name, Sec, Roll, Class = argv 

Marks=float(raw_input("Enter the Marks:"));
Grade=raw_input("Enter the Grade:");

print "\n"
print "Script_name=",Script_name
print "Name=",Name
print "Section=",Sec
print "Roll=",Roll
print "Class=",Class
print "Marks=%r"%Marks
print "Grade=%s"%Grade
