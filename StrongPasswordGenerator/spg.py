# strong password generator
# a strong password:
# has at least 15 characters
# has uppercase letters
# has lowercase letters
# has numbers
# has symbols such as ` ! " ? $ % ^ & * ( ) _ - + { [ ] } : ; @ ' # | \ < , > .
# is not like your previous password
# is not your login
# is not your name
# is not your friends's name
# is not your family members's name
# is not a dictionary word
# is not a common name
# is not a keyboard pattern such as qwerty, asdfghjkl, or 12345678

import random

charset = """
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+{}[]\|/><,.:;'"?
"""
charset = charset[1:-1]
length = len(charset)
print 
pwd_len = int(raw_input("Please specify the length of your password: "))
print "----- ----- ----- -----"
print "There are {0} characters in total:".format(length)
print charset
print "----- ----- ----- -----"
print "Generating password:"
for i in range(10):
    print "#{0}".format(i+1),
    pwd = []
    for i in range(pwd_len):
        pwd.append(charset[random.randint(0, length-1)])
    print "".join(pwd)

