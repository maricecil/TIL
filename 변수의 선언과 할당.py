a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33 (일반 나눗셈)
print(a % b)   # 1 (나머지)
print(a ** b)  # 1000 (10의 3제곱)
print(a // b)  # 3 (몫, 소수점 이하 버림)


x = 10  # 전역 변수
def my_function():
    print(x)  # 전역 변수 x는 함수 내부에서도 접근할 수 있습니다.
my_function()  # 출력: 10
print(x)  # output: 10




def my_function():
    y = 5  # 지역 변수
    print(y)  # 출력: 5
my_function()  # 출력: 5
print(x)  # 출력: 10
print(y)  # 오류 발생! y는 함수 외부에서 사용할 수 없습니다.

