#概括字符集

#\d 数字
#\D 非数字
#\w 匹配一个单词字符
#\W非单词字符
#\s空白字符
#\S非空白字符
# . 匹配除换行符之外其他所有字符

import re

a = 'python 111\njava678#____php'

r = re.findall('\w',a)
r01 = re.findall('[A-Za-z0-9_]',a)
r02 = re.findall('\W',a)
r03 = re.findall('\s',a)

print(r)
print(r01)
print(r02)
print(r03)