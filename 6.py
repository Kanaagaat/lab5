import re

pattern = "[ ,.]"
str = input()

x = re.sub(pattern, ":", str)

print(x)