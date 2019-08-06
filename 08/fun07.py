#可变参数

def demo(param01,*param, param02=100):
    print(param01)
    print(param)
    print(param02)
    print(type(param))

demo(1, 2, 3, 4, 5, 6)