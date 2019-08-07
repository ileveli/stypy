import json

json_str = '{"name":"qiyue", "age":18}'
json_str2 = '[{"name":"qiyue", "age":18,"flags":false}, {"name":"qiyue", "age":18,"flags":true}]'

#反序列化
student = json.loads(json_str)
student2 = json.loads(json_str2)

print(type(student))
print(type(student2))


print(student)
print(student2)

'''
json    python
object  dict
array   list
string  str
number  int
number  float
true    True
flase   Flase
null    None
'''