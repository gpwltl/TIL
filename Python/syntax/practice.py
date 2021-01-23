# 숫자형 자료형
print(5)
print(-10)
print(3.14)
print(10000)
print(5+2)
print(4*3)

# 문자형 자료형
print('풍선')
print("나비")
print("ㅋ"*9)

#불리언(참 / 거짓)
print(5 > 20)
print(True)
print(not False)

# 변수
# 애완동물 소개하기
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "는 "+name+"에요.")
hobby = "공놀이"
# print(name+"는 "+str(age)+"살, "+hobby+"을 좋아해요.")
# +대신 ,를 사용 가능. 이때 str()를 쓰지 않아도 됨.
print(name, "는 ", age, "살, ", hobby, "을 좋아해요.")
print(name+"는 어른일까요? "+str(is_adult))


# 주석
'''
이렇게하면 여러문장을 주석처리 할 수 있어요 
'''

# 연산자
print(1+1)
print(3-2)
print(4*2)
print(10/2)

print(2**3)  # 2^3=8
print(5 % 3)  # 나머지 구하기 2
print(5//3)  # 몫 1

print(10 > 3)  # True
print(4 >= 7)  # False
print(3 == 3)  # True
print(3+4 == 7)  # True
print(1 != 3)  # True
print(not(1 != 3))  # False

print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))  # True
print((3 > 0) or (3 > 5))  # True
print((3 > 0) | (3 > 5))  # True

print(2+3*4)  # 14
print((2+3)*4)  # 20
number = 2+3*4  # 14
print(number)
number = number+2  # 16
# number += 2
print(number)
number *= 2  # 32
print(number)
