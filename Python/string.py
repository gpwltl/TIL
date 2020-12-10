# 문자열
sentence = "나는 소년입니다."
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"
print("성별: "+jumin[7])
print("연: "+jumin[0:2])  # 0부터 2직전까지 (0-1)
print("월: "+jumin[2:4])  # 2부터 4직전까지 (2-3)
print("생년월일: "+jumin[:6])  # 처음부터 6직전까지 (0-5)
print("뒤 7자리: "+jumin[7:])  # 7부터 끝까지 (7-13)
print("뒤 7자리(뒤에부터) "+jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지(7-13)

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())  # True (0번째가 대문자인가?)
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")  # 첫번째 n의 위치를 찾아줌
print(index)  # 5
index = python.index("n", index+1)  # 두번째 n의 위치를 찾아줌
print(index)  # 15
print(python.find("Java"))  # 없으면 -1 출력
# print(python.index("Java"))  #없으면 아예 에러처리

print(python.count("n"))  # n의 개수


# 문자열 포맷
# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A")
# %s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))  # 나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))  # 나는 빨간색과 파란색을 좋아해요.

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color="빨간", age=20))  # 동일한 결과

# 방법4 (v3.6이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출 문자
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
# \"\' : 문장 내에서 따옴표 사용
print("저는 \"나도코딩\"입니다.")
# \\ : 문장 내에서 \ 사용
print("C:\\User\\python")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")  # PineApple
# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")  # RedApple
# \t : 탭
print("Red\tApple")


# quiz
site = "http://naver.com"
password = site.replace("http://", "")
index = password.index(".")
password = password[:index]
print(site+"의 생성된 비밀번호: "+str(password[:3]) +
      str(len(password))+str(password.count("e"))+"!")
