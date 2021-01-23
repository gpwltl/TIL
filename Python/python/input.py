# 입출력
import sys

# python,java,javascript?무엇이 더 재밌을까요?
print("python", "java", "javascript", sep=",", end="?")
print("무엇이 더 재밌을까요?")

print("python", "java", file=sys.stdout)  # 표준출력
print("python", "java", file=sys.stderr)  # 표준에러

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")  # 정렬

# 은행 대기순번표
# 001, 002, 003, 004 ...
for num in range(1, 21):
    print("대기번호: "+str(num).zfill(3))


# 표준 입력 input
# answer = input("아무 값이나 입력하세요 >>")
# print(type(answer))  # string 문자열로 값을 받아들임
# print("입력하신 값은 "+answer+"입니다.")


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}" .format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}" .format(500))
print("{0: >+10}" .format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}" .format(500))
# 3자리 마다 콤마 찍어주기
print("{0:,}" .format(10000000000))
# 3자리 마다 콤마 찍어주고, + - 부호도 붙이기
print("{0:+,}" .format(10000000000))
print("{0:-,}" .format(-10000000000))
# 3자리 마다 콤마 찍어주고, 부호도 붙이고, 자릿수(30) 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
print("{0:^<+30,}" .format(10000000000000))
# 소수점 출력
print("{0:f}" .format(5/3))
# 소수점 특정 자리수까지만 표시 (소수점 3째 자리에서 반올림하기)
print("{0:.2f}" .format(5/3))


# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") #write
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")  # append
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")  # read
# print(score_file.read()) # 전체 문장 가져오기
print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")  # read
while True:  # 파일이 몇줄 인지 모를 때
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")  # read
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
