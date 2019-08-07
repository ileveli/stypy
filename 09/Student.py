from People import Human

class Student(Human):
    sum = 0

    def __init__(self,school,name,age):
        super(Student,self).__init__(name,age)
        self.__school = school
    
    def do_homwork(self):
        super(Student,self).do_homwork()
        print('do english homework!')