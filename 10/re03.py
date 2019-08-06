#字符集
import re

s = 'abc,acc,adc,aef,afc,ahc'

r = re.findall('a[^fc]c',s)
r02 = re.findall('a[c-f]c',s)

print(r)
print(r02)
