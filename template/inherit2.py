from template.inherit1 import ClassOne


class ClassTwo(ClassOne):
    def verify_inherit(self):
        self.open_baidu()


test = ClassTwo()
test.verify_inherit()