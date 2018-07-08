from sys import argv

script,user_name,gender=argv

prompt="Answer-"

print "Hello! %s, from the Script %s. "%(user_name,script)
print "Do you like me %s ?"%user_name
likes=raw_input(prompt)
print "Where do you live %s ?"%user_name
lives=raw_input(prompt)
print "What computer do you use %s ?"%user_name
computer=raw_input(prompt);

print """
So, your name is %s.
You are a %s
You said %r to me liking you.
You live in %s.
You use a %s."""%(user_name,gender,likes,lives,computer)
