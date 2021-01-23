# 숫자 처리 함수
from random import *
from math import *

# 절대값
print(abs(-5))
# 제곱
print(pow(4, 2))  # 4^2=16
#최대값, 최소값
print(max(5, 12))  # 12
print(min(5, 12))  # 5
# 반올림
print(round(3.15))  # 3
print(round(4.99))  # 5

print(floor(4.99))  # 내림. 4
print(ceil(3.15))  # 올림. 4
print(sqrt(16))  # 제곱근. 4

print(random())  # 0.0~1.0미만의 임의의 값 생성
print(random()*10)  # 0.0~10.0미만의 임의의 값 생성
print(int(random()*10))  # 0~10미만의 임의의 값 생성
print(int(random()*45)+1)  # 1~45이하의 임의의 값 생성
print(randrange(1, 46))  # 1~45이하의 임의의 값 생성
print(randint(1, 45))  # 1~45이하의 임의의 값 생성


# quiz
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 ", date, " 일로 선정되었습니다.")
