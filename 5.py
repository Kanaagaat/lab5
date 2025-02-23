import re

str = input()

x = re.search("a.+b$", str)

if x :
    print("YES")
else:
    print("NO")