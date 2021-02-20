class MyClass:
    var = "hello"

    def __init__(self):
        self.param2 = "hi"

    def sayHello(self):
        param1 = "hello~!"
        print(param1)
        print(self.var)


obj = MyClass()
print(obj.var)
obj.sayHello()
# obj.param1()
