import re

str = input()

x = re.search("^a.*b$" , str)

if x :
    print("Yes")
else:
    print("NO")
