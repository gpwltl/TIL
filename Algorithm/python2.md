## 기본 입출력

1. 표준 입력 방법

- input() : 한 줄의 문자열을 입력받는 함수
- map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

```python
list(map(int, input().split()))     # 공백을 기준으로 구분된 데이터 입력받을 때
a,b,c=map(int, input().split())     # 받는 수가 많지 않을 때
```

- `sys.stdin.readline()` : 입력을 최대한 빠르게 받아야 하는 경우
  - import sys
  - 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 사용할 것

2. 표준 출력 방법

- print() : 변수를 콤마 이용하여 띄어쓰기로 구분해 출력함
- 기본적으로 출력 이후 줄 바꿈을 수행함

  - 원하지 않는다면 'end' 속성 이용 `end=" "`

- f-string : `print(f"정답은 {answer}입니다.")`

## 조건문

### if

`if ~ elif ~ else`

### 비교 연산자

x==y : 서로 같을 때 True
x!=y : 서로 다를 때 True
x>y x<y
x>=y x<=y

### 논리 연산자

x and y : x, y가 모두 True일 때 True
x or y : x, y 중 하나만 True일 때 True
not x : x가 False일 때 True

### 기타 연산자

`x in 리스트` : 리스트 안에 x가 있을 때 True
`x not in 문자열` : 문자열 안에 x가 들어있지 않을 때 True

#### 기타/ 유의할 점

- pass : 아무것도 처리하고 싶지 않을 때 pass 키워드 사용

  > 디버깅에서 조건문의 형태만 만들어놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우

- 코드의 블록을 들여쓰기로 지정
- 조건문에서 실행될 소스코드가 한줄이면, 굳이 줄 바꿈을 하지 않고도 간략하게 표현
- 조건부 표현식은 if ~ else문을 한 줄에 작성함

```python
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)   # Success
```

- 조건문 안에서 수학의 부등식 그대로 사용할 수 있음

```python
x = 15
if 0<x<20: print("x는 0이상 20미만의 수입니다.") # x는 0이상 20미만의 수입니다.
```

## 반복문

### while

- 반복문을 작성한 뒤에는 항상 반복문을 탈출할 수 있는지 확인할 것 `무한 루프`
- continue(진행), break(탈출)

### for문

- for 변수 in 리스트
- range(시작 값, 끝 값+1) : 연속적인 값을 차례대로 순회할 때 사용함 (시작값은 0)
