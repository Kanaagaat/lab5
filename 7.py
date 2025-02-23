import re

str = input()


x = re.sub("_([a-zA-z])", lambda s: s.group(1).upper(), str )
x.capitalize()
print(x)