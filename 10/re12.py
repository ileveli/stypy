import re

#re.match
#re.search 
#re.findall
#re.sub


s = 'A8C3721D86'

#match从字符串的首字母开始匹配,只匹配一次
r = re.match('\d',s)
#search搜索整个字符串,只匹配一次
r02 = re.search('\d',s)


r03 = re.findall('\d',s)

print(r)
print(r02)
print(r02.span())
print(r02.group())
print(r03)

