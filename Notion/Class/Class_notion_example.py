class MyClass:
    var = "hello"

    def sayHello(self):
        print(self.var)


# MyClass 인스턴스 객체 생성
obj = MyClass()
# "hello" 가 출력됨
print(obj.var)
# "hello" 가 출력됨
obj.sayHello()
