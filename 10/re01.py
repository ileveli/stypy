import re

a = 'C|C++|JAVA|GO|PYTHON|JAVASCRIPT|C#|OJECT-C'

r = re.findall('PYTHON',a)

if len(r) > 0:
    print('字符串中包含PYTHON字符')

print(r)

 