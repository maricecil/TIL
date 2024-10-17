x = 10  # 전역 변수
def my_function():
    print(x)  # 전역 변수 x는 함수 내부에서도 접근할 수 있습니다
my_function()  # 출력: 10
print(x)  # output: 10