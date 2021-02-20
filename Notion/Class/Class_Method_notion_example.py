class MyClass:
    def sayHello(self):
        print('hello')

    def sayBye(self, name):
        print("%s! see you later!" % name)


obj = MyClass()
obj.sayHello()  # hello
obj.sayBye("mang00")  # mang00! see you later!
