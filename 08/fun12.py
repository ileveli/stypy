c = 1

def func01():
    #c = 2
    def fun02():
        #c = 3
        print(c)
    fun02()
#作用域链，链式特性
func01()