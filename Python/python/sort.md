# 정렬 sort(), sorted()

## sort()

- 리스트를 정렬된 상태로 변경(오름차순) array.sort()
- 리스트만을 위한 메소드 
- 내림차순: sort(reverse=True)



## sorted()

- 기존의 리스트를 변경하는 것이 아니라 정렬의 새로운 리스트를 반환(오름차순)
- 어떤 이터러블 객체도 받을 수 있음(딕셔너리 등)
- 내림차순 sorted(reverse=True)

```python
>>> sorted({3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'})
[1, 2, 3, 4, 5]
```

### 📝 key 매개변수

sorted와 lambda를 잘 이용하면 강력한 무기! 

- key인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하며 순서대로 정렬
- 오름차순: sorted(a, key=lambda x:x[0])
- 내림차순: sorted(a, key=lambda x:-x[0])
  - 요소가 여러개일 경우, 
    각 요소마다 정렬 기준을 정해줄 수 있음.  sorted(a, key=lambda x:(x[0], -x[1]))

```python
students=[
   ('홍길동', 3.9, 2016303),
   ('김철수', 3.0, 2016302),
   ('최자영', 4.3, 2016301),
]

print(sorted(students, key=lambda x:x[2]))	#인덱스2번 기준으로 정렬
# 오름차순, [('최자영', 4.3, 2016301), ('김철수', 3.0, 2016302), ('홍길동', 3.9, 2016303)]

print(sorted(students, key=lambda x:x[2], reverse=True))
# 내림차순, [('홍길동', 3.9, 2016303), ('김철수', 3.0, 2016302), ('최자영', 4.3, 2016301)]
```



#### dict 일때

```python
alpha = {'a': 10000, 'c': 1010, 'd': 100, 'e': 10, 'b': 1, 'g': 100, 'f': 1}

#key로 비교하고 싶을때1 (key만 다시 담을 때)
print(sorted(alpha, key=lambda x: x[0], reverse=True))	# ['g', 'f', 'e', 'd', 'c', 'b', 'a']

#key 비교2(value함께 담을 때 )
print(sorted(alpha.items(), key=lambda x: x[0], reverse=True))	# [('g', 100), ('f', 1), ('e', 10), ('d', 100), ('c', 1010), ('b', 1), ('a', 10000)]

#value로 비교하고 싶을때 
print(sorted(alpha.items(), key=lambda x: x[1], reverse=True))	# [('a', 10000), ('c', 1010), ('d', 100), ('g', 100), ('e', 10), ('b', 1), ('f', 1)]
```

