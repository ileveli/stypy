#数量字符


import re

a = 'python 111\njava678#____php'

r = re.findall('[a-z]{3,6}',a)

print(r)