#re.I 忽律大小写
#re.S 改变 . 识别行为，支持识别换行符

import re

language = 'PythonC#\nJavaPHP'

r = re.findall('c#',language,re.I)
r02 = re.findall('c#.{1}',language,re.I)
# | 表示且的关系
r03 = re.findall('c#.{1}',language,re.I | re.S)

print(r)
print(r02)
print(r03)