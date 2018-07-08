boys=int(raw_input("Print the number of boys :"))
girls=int(raw_input("Print the number of girls :"))
homos=int(raw_input("Print the number of homos :"))

if boys>=girls:
    print "The number of boys are greater than girls."
    
if boys<=girls:
    print "The number of girls are greater than boys."
    
if girls>=homos:
    print "The number of girls are greater than homos."
  
if homos>=girls:
    print "The number of homos is greater than girls."
    
if boys>=homos:
    print "The number of boys is greater than homos."

if homos>=boys:
    print "The number of homos is greater than boys."
    
