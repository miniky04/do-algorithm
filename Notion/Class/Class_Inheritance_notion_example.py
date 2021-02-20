class Add:
    def add(self, n1, n2):
        return n1 + n2


class Calculator(Add):
    def sub(self, n1, n2):
        return n1 - n2


obj = Calculator()
print(obj.add(1, 2))  # 3
print(obj.sub(1, 2))  # -1


# 다중상속을 이용한 변형 코드
class Add:
    def add(self, n1, n2):
        return n1 + n2


class Multiply:
    def multiply(self, n1, n2):
        return n1 * n2


class Calculator(Add, Multiply):
    def sub(self, n1, n2):
        return n1 - n2


obj = Calculator()
print(obj.add(1, 2))  # 3
print(obj.multiply(3, 2))  # 6
