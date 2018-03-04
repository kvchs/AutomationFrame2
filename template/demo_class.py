# python中默认规则，包名和文件名都是小写，类名称单词首字母大写，函数名称小写，多个字母下划线隔开。
class ClassOne(object):
    string1 = "this is a string"

    def instance_func(self):
        print("this is a instance function")
        print(self)

    @classmethod
    def class_func(cls):
        print("this is a class method")
        print(cls)

    @staticmethod
    def static_fun():
        print("this is a status method")

# 实例对象调用实例方法
test = ClassOne()
test.instance_func()
test.class_func()
test.static_fun()
print(test.string1)

# 类调用实例的方法
ClassOne.instance_func(test)
ClassOne.instance_func(ClassOne)
ClassOne.static_fun()
ClassOne.class_func()