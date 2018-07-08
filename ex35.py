from sys import exit

def start():
    print"""
    You are in a Dark Room.
    It has three doors.
    The doors are marked as 1,2 and 3.
    Which door do you take ?
    """
    next=int(raw_input(">"))
    
    
    if next==1:
        bear_trap()
    elif next==2:
        ghost_trap()
    elif next==3:
        greed_trap()
    else:
        print "Wrong Choice !"
        
def bear_trap():
    print """
    So you entered a bear's den.
    The bear is sleeping near the door.
    You have three options:-
    1.Run for the door
    2.Distract the bear and then run for the door.
    3.Sneak away to the door
    
    What would you do ?
    """
    num=int(raw_input(">"))
    if num==1 or num==2:
        print """The Bear wakes up.
                 You have two options.
                 1.Run for the door
                 2.Hide from the bear.
                 """
        n=int(raw_input(">"))
        if n==1:
            print "You Escape."
        else:
            print "You never escaped."
    else:
        print "You never escaped"
        
def ghost_trap():
    print """
    There is a ghost in the room.
    Its terryfying.
    You have two options:-
    1.Run
    2.Hide
    3.Confront
    """
    c=int(raw_input(">"))
    if c==1 or c==2:
        print "The ghost comes in front of you."
        print "What should you do?"
        print "1.Run"
        print "2.Confront"
        d=int(raw_input("Choice ?"))
        if d==1 and c==1:
            print "You Die"
        else:
            print "You Live"
    else:
        print "You Survive"
        
def greed_trap():
    print """
    You Find a lot of Gold in the room.
    how much would you pick.
    """
    f=raw_input(">")
    if "0" in f or "1" in f or "2" in f or "3" in f or "4" in f or "5" in f     or "6" in f or "7" in f or "8" in f or "9" in f:
        z=int(f)
    else:
        print "Enter a number man...."
        exit(0)
        
    if z>100:
        print "Greedy Bastard!You Die."
    else:
        print "You are not Greedy.So you live."
    
start()
