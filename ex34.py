lists=['1.Tiger','2.Lions','3.Elephants','4.Zebras']
print "The List is :"
for i in lists:
    print i
    
print "Enter the index to print that element"
j=int(raw_input())

print "The element at %d position is -----"%j
print lists[j-1]
