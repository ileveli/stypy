#贪婪与非贪婪，默认贪婪


import re

a = 'python 111\njava678#____php'

r = re.findall('[a-z]{3,6}',a)
r01 = re.findall('[a-z]{3,6}?',a)

print(r)
print(r01)