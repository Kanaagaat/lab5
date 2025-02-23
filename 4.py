import re

str = input()

x = re.search("[A-Z][a-z]+$", str)

if x:
    print("YES")
else:
    print("NO")