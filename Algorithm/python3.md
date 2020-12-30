## 함수

특정한 작업을 하나의 단위로 묶어놓은 것

- 불필요한 소스코드의 반복을 줄일 수 있음
- 내장 함수 : 파이썬이 기본적으로 제공하는 함수
- 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

```python
def add(a, b):
    return a+b
print(add(3, 7))    # 10
```

- 파라미터의 변수를 직접 저장할 수 있음(순서가 달라도 상관 없음)

```python
def add(a, b):
    print('함수의 결과: ', a+b)

add(b=3, a=7)  # 10
```

- global 키워드 : 함수 바깥에 선언된 변수를 바로 참조함 (전역변수 참조 가능)

```python
a=0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)    # 10
```

- 반환 값 : 여러 개의 반환 값을 가질 수 있음

```python
def operator(a, b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add, sub, mul, div

a, b, c, d = operator(7, 3)
print(a, b, c, d)   # 10 4 21 2.3333
```

- 람다 표현식 : 특정한 기능을 수행하는 함수를 한 줄로 작성 가능

```python
print((lambda a, b: a+b)(3, 7)) # 10
```

```python
arr=[('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]
print(sorted(arr, key=my_key)) # [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

print(sorted(arr, key=lambda x: x[1])) # [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
```

```python
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result)) # [7,9,11,13,15]
```

## 표준 라이브러리

1. 내장 함수
2. itertools : 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공 (순열, 조합 - 완전탐색)
3. heapq : 힙 자료구조 제공 (우선순위 큐 - 최단 경로(다익스트라))
4. bisect : 이진탐색 기능 제공
5. collections : 덱, 카운터 자료구조에 포함
6. math : 필수적인 수학적 기능 제공 (팩토리얼, 제곱근, 최대공약수, 삼각함수 등)

### 1. 내장 함수

- sum(리스트)
- min()
- max()
- eval() : 계산하는 식의 결과 출력 `eval("(3+5)*7")` #결과: 56
- sorted() : 오름차순 정렬
- sorted( , reverse=True) : 내림차순 정렬
- sorted() with key
  ```python
  arr=[('홍길동', 35), ('이순신', 75), ('아무개', 50)]
  result = sorted(arr, key=lambda x: x[1], reverse=True)
  print(result) # [('이순신', 75), ('아무개', 50), ('홍길동', 35)]
  ```

### 2. itertools(순열과 조합)

- 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열

```python
from itertools import permutations
data=['A', 'B', 'C']
result=list(permutations(data, 3))  # 모든 순열 구하기
```

- 중복 순열

```python
from itertools import product
data=['A', 'B', 'C']
result=list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복 허용)
```

- 조합: 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것

```python
from itertools import combinations
data=['A', 'B', 'C']
result=list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
```

- 중복 조합

```python
from itertools import combinations_with_replacement
data=['A', 'B', 'C']
result=list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기(중복 허용)
```

### 5. collections

##### Counter

등장 횟수를 세는 기능 제공

- 리스트 같은 반복 가능한 객체일 때 **내부의 원소가 몇 번씩 등장했는지** 파악가능

```python
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # blue가 등장한 횟수 출력 -> 3
print(counter['green']) # green이 등장한 횟수 출력 -> 1
print(dict(counter)) # 사전 자료형으로 반환 -> {'red': 2, 'blue': 3, 'green': 1}
```

### 6. math

- 최대 공약수 : gcd()
- 최대 공배수 : lcm()

```python
import math

print(math.gcd(21, 14)) # 최대 공약수 계산
print(lcm(21, 14)) # 최대 공배수 계산
```
