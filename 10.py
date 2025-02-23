import re

str = input()


x = re.sub("([A-Z])", lambda s: '_'+s.group(), str )

print(x)