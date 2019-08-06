import re

s = 'life is short ,i use python'
s2 = 'life is short ,i use python,i love python'

r = re.search('life(.*)python',s)
r02 = re.search('life(.*)python(.*)python',s2)



print(r.group(0))
print(r.group(1))

print(r02.group(0))
print(r02.group(1))
print(r02.group(2))
print(r02.group(0,1,2))
print(r02.groups)
