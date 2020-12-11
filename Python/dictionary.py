cabinet = {3: "유재석", 100: "박명수"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5])  # error
print(cabinet.get(5, "사용가능"))  # 값이 없으면 '사용가능'이라는 문구를 띄움

print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet = {"a-3": "유재석", "b-100": "박명수"}
print(cabinet["a-3"])
print(cabinet["b-100"])

# 새 손님
print(cabinet)
cabinet["a-3"] = "김종국"
cabinet["c-30"] = "조세호"
print(cabinet)
# 간 손님
del cabinet["a-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
