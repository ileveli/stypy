#数量字符
# * 匹配*号前面字符0次或者无限多次
# + 匹配*号前面字符1次或者无限多次
# ? 匹配*号前面字符0次或者1次



import re

a = 'pytho0python1pythonn2'

r = re.findall('python*',a)
r01 = re.findall('python+',a)
r02 = re.findall('python?',a)
r03 = re.findall('python{1,2}',a)
r04 = re.findall('python{1,2}?',a)

print(r)
print(r01)
print(r02)
print(r03)
print(r04)