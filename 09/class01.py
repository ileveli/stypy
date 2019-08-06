#面向对象
#有意义的面向对象代码
#类 = 面向对象
#类、对象
#实例化
#类最基本的特性：封装

class Student():
    num = 36
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.score = 0
        #self.__class__.num +=1
        #print('当前班级学生人数为：' + str(self.__class__.num))

    def DoHomework(self):
        print('Do homework!')
    
    def setScore(self,score):
        if score < 0:
            return '分数不能为负值'
        self.score = score
        print(self.score)
    
    @classmethod
    def plus_sum(cls):
        cls.num += 1
        print(cls.num)
    
    @staticmethod
    def add(x,y):
        print(Student.num)
        print('This is  a static method')

student = Student('WangChongwen',35)
result = student.setScore(-1)
print(result)
#student.add(1,2)
#Student.add(3,4)
#Student.plus_sum()
#print(student.__dict__)
#print(student.name)
#print(Student.__dict__)