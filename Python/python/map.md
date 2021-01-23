# map, filter

## map

map함수는 반복가능한 iterable객체를 받아서, 각 요소에 함수를 적용해주는 함수

- 메모리 절약 가능(for문 사용보다)

```python
def add_1(n):
  return n+1

target=[1,2,3,4,5]
result=map(add_1, target)
print(list(result))		#[2,3,4,5,6]
```

- 단, 재사용의 목적이 없다면 `lambda 함수` 를 적용하여 불필요한 코드 삭제

  ```python
  target=[1,2,3,4,5]
  result=map(lambda x: x+1, target)
  print(list(result))	#[2,3,4,5,6]
  ```





## filter

filter함수는 특정 조건으로 걸러서 걸러진 요소들로 iterator객체를 만들어서 리턴함

- map함수와 사용방법은 동일하나, 함수의 결과가 참인지 거짓인지에 따라 해당 요소를 포함할지를 결정함

```python
target=[1,2,3,4,5,6,7,8,9,10]
result=[]

def is_even(n):
  return True if n%2==0 else False

#for value in target:
#  if is_even(value):
#    result.append(value)
result=filter(is_even, target)

print(list(result))		# [2,4,6,8,10]
```

- 역시나 함수 재사용할 이유가 없으면, 간결하게 lambda를 이용

  ```python
  target=[1,2,3,4,5,6,7,8,9,10]
  result=filter(lambda x: x%2==0, target)
  print(list(result))		# [2,4,6,8,10]
  ```

  

  