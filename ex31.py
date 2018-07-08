print """
There are two dark rooms.
You have to choose one of the room.
choose----------------------------

1.ROOM 1
2.ROOM 2
\n"""

ch1=raw_input(">")

if ch1=='1' :
    print """
    You Find a Bear in the room.
    You have two choices :
    1.RUN
    2.HIDE\n
    """
    ch2=raw_input(">")
    if ch2=='1':
        print "YOU SURVIVE"
    else:
        print "YOU DIE"
        
elif ch1=='2':
    print """
    You find a shark.
    you have two choices.
    1.RUN
    2.HIDE\n
    """
    ch3=raw_input(">")
    if ch3=='1':
        print "YOU DIE"
    elif ch3=='2':
        print "YOU SURVIVE"
        
else:
    print "WRONG CHOICE!"        
        
        
    
