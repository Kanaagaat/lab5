import re

str = input()

x = re.search("ab{2,3}$", str)

if x:
    print("YES")
else:
    print("NO")