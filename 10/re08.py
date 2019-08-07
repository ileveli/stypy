#边界匹配
# ^ 起始位置，#结束位置

import re

a = '100001'
#4~8位


r = re.findall('^\d{4,8}$',a)
r01 = re.findall('^000',a)
r02 = re.findall('000$',a)

print(r)
print(r01)
print(r02)