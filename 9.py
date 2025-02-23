import re

str = input()

x = re.sub("[A-Z]", lambda s: " "+s.group(), str)

print(x)

