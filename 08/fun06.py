#默认参数
def print_student_files(name,gender="男",age="18",college="北京大学"):
    print("我叫" + name)
    print("我今年" + age + "岁")
    print("我是" + gender + "生")
    print("我在" + college + "上学")

print_student_files("王崇文","男","25","北京大学")
print("--------------------------------------")
print_student_files("高静",gender="女")
print("--------------------------------------")
print_student_files("高贺",gender="女")