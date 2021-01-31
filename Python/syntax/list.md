# List

## 1. 다양한 기능

- list.index( value ) : 값을 이용하여 위치를 찾는 기능
- list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가 (‘+’연산자 보다 성능이 좋음)
- list.insert( index, value ) : 원하는 위치에 값을 추가
- list.sort( ) : 값을 순서대로 정렬
- list.reverse( ) : 값을 역순으로 정렬

```python
list1 = ['a', 'b', 'q', 'f']
list1.index('b')	# 1

list2 = [1, 2, 3]
list1.extend(list2)	# list1: ['a', 'b', 'q', 'f', 1, 2, 3]

list1.insert(1, 'hi')	# list1: ['a', 'hi', 'b', 'q', 'f', 1, 2, 3]

list1.sort()	# list1: [1, 2, 3, 'a', 'b', 'f', 'hi', 'q']

list1.reverse()	# list1: ['q', 'hi', 'f', 'b', 'a', 3, 2, 1]
```

<br/>

## 2. list와 string 

```python
list3 = [1, 9, 8, 5, 0, 6]
string1 = 'hello world'

print(5 in list3)		# True
print('e' in string1) 	# True
```

### .split() 

`list=str.split() `: 문자열 => 리스트, 공백시 스페이스 기준

```python
char = list('hello')	#['h', 'e', 'l', 'l', 'o']

words = 'python is good progamming language'
words_list = words.split()
print(words_list)		#['python', 'is', 'good', 'programming', 'language']

time_str = '10:35:24'
time_str.split(':')
print(time_str)		#['10', '35', '24']
```



### .join()

`"".join(list)`	: 리스트에서 문자열로

```python
time_list = ['10', '35', '24']
print(":".join(time_list))		#'10:35:24'
```



### slice

- slicing: 리스트나 문자열에서 값을 여러개 가져오는 기능	`list[시작: 끝]`
- 시작은 포함되지만 끝 값은 포함되지 않음
  - list[2: ]	2~끝까지
  - list[ :2]    처음부터 1번째까지 
  - list[ : ]     처음부텉 끝까지 (리스트 복사해둘때 유용)

```python
text='hello world'
print(text[1:5])	#'ello'

list=[ 0, 1, 2, 3, 4, 5 ]
print(list[1:3])	#[1,2]
print(list[:4])		#[0,1,2,3]
```





### step

- slice한 값의 범위에서 step값을 주어 그 값만큼 건너뛰어 가져오는 기능	`list[시작값:끝값:step]`

```python
list1= list(range(20))
# list1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(list1[5:15:3])		# [5, 8, 11, 14]
print(list1[15:5:-1])		# [15, 14, 13, 12, 11, 10, 9, 8, 7, 6]
print(list1[::3])				# [0, 3, 6, 9, 12, 15, 18]
print(list1[::-3])			# [19, 16, 13, 10, 7, 4, 1]
```



<br/>

## 3. slice 리스트 수정하기

#### 삭제

- del list[ :5]	처음부터 5번째까지 삭제	`del 객체` 
- *자체함수라서 모든 자료형 사용 가능



#### 수정

- 기본 형식)  list[1:3] = [77, 88]	
- 더 많은 개수로 변환)  list[1:3]=[77,88,99]
- 더 적은 개수로 변환)  list[1:4]=[8]

```python
numbers=list(range(10))
del numbers[:5]		#numbers: [5,6,7,8,9]

numbers[1:3] = [66, 77]		#numbers: [5, 66, 77, 8, 9]
numbers[3:4] = [0]		#numbers: [5, 66, 77, 0]
```

