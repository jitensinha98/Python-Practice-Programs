cars=['maruti','hyundai','honda','mercedes','bmw']
numbers=[1,2,3,4,5,6]
fruits=['apple','banana','guava']

for car in cars:
    print "Car=%s"%car
    
for number in numbers:
    print "Number=%d"%number
    
for fruit in fruits:
    print "Fruit=%s"%fruit
    
element=[]

for i in range(0,8):
    print "Adding %d to the list"%i
    element.append(i)
    
for num in element:
    print "Element is = %d"%num
