y=int(raw_input("Enter the starting element:"))
z=int(raw_input("Enter the ending element:"))
element=[]
for i in range(y,z+1):
    element.append(i)
    print "All elements are stored in the list."
print "Do you want to veiw the list :"
raw_input()

print "All elements in the list are :"
for numbers in element:
    print "Numbers=%d"%numbers
    
p=int(raw_input("Enter the interval:"))
for i in element:
    print "Numbers=%d"%i
