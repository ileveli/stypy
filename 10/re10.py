# re.sub用于字符串替换
# re.findall用于字符串查找
# 把函数作为参数传递

import re

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'

language = 'PythonC#JavaPHPC#C#'

r = re.sub('C#','GO',language)
lang = language.replace('C#','GO')
r02 = re.sub('C#','GO',language,1)
r03 = re.sub('C#',convert,language)

print(r)
print(r02)
print(lang)
print(r03)