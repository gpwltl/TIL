# python

## 자료형

### 수 자료형

1. 정수형
   정수를 다루는 자료형(양의 정수, 음의 정수, 0)
2. 실수형
   소수점 아래의 데이터를 포함하는 수 자료형(변수에 소수점 붙인 수)
   .7 = 0.7  
   5. = 5.0
   - round() 함수를 이용하여 반올림 : round(123.456, 2) -> 123.46
3. 지수 표현 방식
   e(E) 다음에 오는 수는 10의 지수부
   1e9 = 10의 9제곱(1,000,000,000)
   - 최단 경로 알고리즘에서는 도달할 수 없는 노드에 대하여 최단거리를 무한(INF)로 설정함

\*\*연산

- 나누기 연산자(/) : 실수형 반환
- 나머지 연산자(%) : 홀짝, 배수 체크시 - 정수형 반환
- 몫 연산자(//) : 정수형 반환

### 리스트 자료형

1. 리스트 `[]` or `list()`
   데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형(index: 0 부터 시작)
   - 인덱싱: 리스트의 특정한 원소에 접근하는 것(음의 원소를 넣으면 원소를 뒤에서부터 접근함)
     ```python
     a=[1,2,3,4,5,6]
     print(a[-1]) # 6
     print(a[1:4]) # [2,3,4]
     ```

\*\*리스트 컴프리헨션

```python
arr=[i for i in range(5)]
print(arr)  # [0,1,2,3,4]

arr=[i for i in range(10) if i%2==1]
print(arr)  # [1,3,5,7,9]

arr=[i*i for i in range(1, 6)]
print(arr)  # [1, 4, 9, 16, 25]
```

- 2차원 리스트를 초기화할 때 효과적으로 사용됨
- n*m 크기의 2차원 리스트 한번에 초기화할 때 매우 유용
  `arr=[[0]*m for i in range(n)]`
  ( i 대신 \_ (언더바: 반복을 위한 변수의 값을 무시하고자 할 때) 사용 가능)
- 관련 메서드
  - arr.append()
  - arr.sort()
  - arr.sort(reverse=True) or arr.reverse()
  - arr.insert()
  - arr.count()
  - arr.remove()

### 문자열, 튜플 자료형

1. 문자열
   `''` `""`
   전체 문자열을 큰따옴표로 구성되면 내부적으로 작은따옴표 사용 가능(반대도 가능) or \ 사용

\*\*연산

- \+ : 문자열을 더해져서 연결
- 문자열 \* 양의 정수 : 여러번 더해짐
- 인덱싱, 슬라이싱 이용 가능 (특정 인덱스 값은 변경 불가)

2. 튜플 `()`

- 한 번 선언된 값을 변경할 수 없음
- 공간 효율적(적은 메모리 사용)

> 사용하면 좋은 경우
>
> - **서로 다른 성질**의 데이터를 묶어서 관리할 때
> - 최단 경로 알고리즘에서 자주 사용
> - **해싱**의 키 값을 사용할 때
> - 메모리를 효율적으로 사용할 떄

### 사전, 집합 자료형

**순서가 없기 때문에** 인덱싱으로 값을 얻을 수 없고, 키 or 집합의 원소를 이용해 O(1)의 시간복잡도로 조회함

1. 사전

- 키와 값의 쌍을 데이터로 가지는 자료형(순차 저장x)
- 변경 불가능한 자료형을 키로 사용할 수 있음
- 해시테이블을 이용해 데이터 조회/수정에 있어서 O(1) 시간 처리 가능
  - dic.keys() : 키만 뽑아서 리스트로 이용할 때
  - dic.values() : 값만 뽑아서 리스트로 이용할 때

2. 집합

- 중복 허용x
- 순서x
- 리스트 혹은 문자열로 초기화 가능 `set()`
- 데이터 조회/수정에 있어서 O(1)이 시간 처리 가능
- 합집합, 교집합, 차집합 사용 가능
- 관련함수
  - 원소 추가: data.add()
  - 원소 여러개 추가: data.update()
  - 원소 삭제: data.remove()

```python
a=set([1,2,2,3,4,4,5])
print(a) # {1,2,3,4,5}
```
