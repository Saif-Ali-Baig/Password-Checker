# password check thing
import re

def check_pass(p):
    stuff = []
    s = 0
    #length check
    if len(p)>7:
        s=s+1
        stuff.append("ok length")
    else:
        stuff.append("too short!!")
    
    #upper case check
    if re.search("[A-Z]",p):
        s+=1
        stuff.append("has big letters")
    else:
        stuff.append("no big letters")
    
    if s>1:
        return "good",stuff
    else:
        return "bad",stuff

# main thing
password=input("gimme password: ")
strength,comments=check_pass(password)
print("strength is",strength)
for c in comments:
    print(c)