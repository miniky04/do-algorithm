# 함수 인자 이해하기 #
def add_txt(t1, t2="python"):
    print(t1 + ' : ' + t2)


add_txt("best")  # best : python
add_txt(t2="korea", t1="1등")  # 1등 : korea

'''
함수를 정의할 때 인자의 개수가 불명확한 경우가 있다.
이 경우 가변인자를 활용하여 함수를 선언하면 된다. 
가변인자는 *args와 같이 인자 이름 앞에 *를 붙인다.
args는 함수 내부에서 튜플로 처리된다. func1은 가변인자인 args를 출력하는 함수이다.
'''


def func1(*args):
    print(args)


'''
키워드 인자가 불명확한 경우가 있따.
func2를 정의할 때 width 와 height 는 명확하지만, 차후 어떤 키워드 인자가 필요한지
확정되지 않은 경우 **kwargs 와 같이 인자를 정해주면 된다.
kwargs 는 함수 내부에서 사전으로 처리 된다. 
func2는 미정 키워드 인자 kwargs 를 출력하는 함수이다.
'''


def func2(width, height, **kwargs):
    print(kwargs)


func1()  # ()
func1(3, 5, 1, 5)  # (3, 5, 1, 5)

'''
func2에 width 와 height 에 해당하는 값인 10, 20만 전달하여 호출하면 **kwargs 에 전달되는
값이 없으며, kwargs 는 함수 내부에서 빈 사전 자료가 된다.
func2 에 width, height 외에 키워드 인자로 depth = 50, color = 'blue' 를 추가하여 호출하면
**kwargs 는 depth = 50, color = 'blue' 를 전달받고, func2 함수 내부에서 kwargs 는 
{'depth':50, 'color':'blue'} 와 같은 사전 자료가 된다. 
'''
func2(10, 20)  # {}
func2(10, 20, depth=50, color="blue")  # {'depth': 50, 'color': 'blue'}

'''
def add_txt(t1="python", t2):
-> SyntaxError: non-default argument follows default argument

add_txt("best") 는 add_txt 함수의 첫번째 인자인 t1에 'best' 가 대입되는데 t2에 아무런
값이 지정되지 않았으므로 기본 값으로 지정된 'python' 이 t2에 적용된다.
'''

# 지역 변수와 전역변수 이해하기 (global) #
'''
param 과 str_data 를 각각 10, '전역변수' 로 선언
'''
param = 10
str_data = "전역변수"

'''
지역변수는 함수 내에서만 유효한 변수,
전역변수는 코드 전반에 걸쳐 유효한 변수이다.

따라서 지역변수를 선언하는 위치는 함수 내부가 되며,
전역변수를 선언하는 위치는 함수 바깥이 됩니다.

지역변수는 함수를 벗어나면 더 이상 유효하지 않습니다.
함수의 인자로 선언된 변수는 함수 내에서만 유효한 지역변수이다.

함수 내에서 선언한 지역변수가 함수 바깥에서 선언된 전역변수와 이름이 같을 경우,
함수 내에서는 지역변수가 우선이기 때문에 지역변수로 취급되고 처리된다.

함수 내부에서 바깥에서 선언한 전역변수를 사용하려면 'global' 키워드를 이용해
전역변수를 사용한다고 명시하면 된다.
'''


def func1():
    str_data = "지역변수"
    print(str_data)


'''
func2() 는 param이라는 이름의 인자를 한 개 가지고 있습니다.
인자 이름 param은 전역변수와 이름이 같지만 func2() 내에서만
유효한 지역변수로 취급되고 처리된다.
따라서 func2() 내에서 param에 값을 대입해도 전역변수 param 에 영향을 주지 않습니다.
'''


def func2(param):
    param = 1


'''
func3() 내부에서 global param 으로 전역변수로 선언된 param 을 사용할 것임을 명시했습니다.
이제 func3() 내에서 param 은 전역변수 param 을 이용하는 것이며 
이 값을 변경하게 되면 전역변수 param의 값이 변경되는 것입니다.
'''


def func3():
    global param
    param = 50


func1()  # 지역변수
print(str_data)  # 전역변수
print(param)  # 10
func2(param)
print(param)  # 10
func3()
print(param)  # 50

# 함수 리턴값 이해하기(return) #
'''
reverse() 는 3개의 인자를 가지고 있으며, 이 함수는 인자의 순서를 바꾸어 리턴합니다.
따라서 reverse()의 리턴값은 3개입니다.
'''


def reverse(x, y, z):
    return z, y, x


'''
숫자 1, 2, 3을 reverse()의 인자로 전달하여 호출하고 그 결과값을 ret으로 둡니다.
ret 을 출력하면 튜플(3, 2, 1)이 표시됩니다.
'''

ret = reverse(1, 2, 3)
print(ret)  # (3, 2, 1)

'''
리턴값이 여러 개인 경우 튜플 형식으로 리턴값이 만들어지므로 튜플의 요소 개수만큼
나누어서 리턴값을 개별적으로 받을 수도 있습니다.
r1, r2, r3에 각각 'c', 'b', 'a'가 리턴값을 대입된다.
'''

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1)  # 'c'
print(r2)  # 'b'
print(r3)  # 'a'
