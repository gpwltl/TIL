# 튜플
from random import *
menu = ("돈가스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") #error

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


# 집합(세트)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "박명수", "양세형"}
python = set(["유재석", "김종국"])

# 교집합(java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))
# 합집합(java도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))
# 차집합(java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java-python)
print(java.difference(python))
# python 할 줄 아는 사람이 늘어남
python.add("하하")
print(python)
# java를 잊어버렸어요
java.remove("양세형")
print(java)


# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


# quiz
users = list(range(1, 21))  # 1부터 20까지 숫자를 생성
shuffle(users)
winners = sample(users, 4)  # 4명 중에서 1명은 치킨, 3명은 커피 (중복 방지를 위해)
chicken = winners[0]
coffee = winners[1:]
print("""--당첨자 발표--
치킨 당첨자: {}
커피 당첨자: {}
--축하합니다--
""" .format(chicken, coffee))
