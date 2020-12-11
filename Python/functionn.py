# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다." .format(balance+money))
    return balance+money


def withdraw(balance, money):  # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다." .format(balance-money))
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다." .format(balance))


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance-money-commission


balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다." .format(commission, balance))


# 기본값
# 같은 학교, 같은 학년, 같은 반, 같은 수업.
def profile(name, age=17, main_lang="python"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" .format(name, age, main_lang))


profile("유재석")
profile("박명수")


# 키워드 값
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" .format(name, age, main_lang))


profile(name="유재석", main_lang="python", age=20)


# 가변 인자 : 매개변수가 여러개인데 정해지지 않았을 때
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t" .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)
def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t주 사용 언어: " .format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("하하", 22, "java", "python", "c", "c++", "c#", "javascript")
profile("박명수", 24, "Kotlin", "swift")


#지역변수, 전역변수
# 지역변수: 함수내에서만 사용(함수호출 끝나면 사라짐)
# 전역변수: 프로그램 어디서든 사용
gun = 10


def checkpoint(soldiers):
    global gun  # 전역 공간에 있는 gun 사용(밖에 있는 gun=10을 사용하겠다.)
    gun = gun-soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))


def checkpoint_ret(gun, soldiers):  # 위 방법 보다는 이 방법으로 변수를 사용할 것!
    gun = gun-soldiers
    print("[함수 내] 남은 총: {0}" .format(gun))
    return gun


print("전체 총: {0}" .format(gun))
# checkpoint(2)  # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}" .format(gun))


# quiz
def std_weight(height, gender):
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21


height = 175  # cm 단위
gender = '남자'
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height, gender, weight))
