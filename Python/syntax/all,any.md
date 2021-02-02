# all(), any() 함수

조건 성립 유무에 따라 True, False를 리턴

- 파이썬 빌트인 함수  
- 리스트에서만 적용가능
- 파이썬에서는 `빈 값`, `0`, `None` 은 False로 인식 :smile_cat:



## All

조건이 전부 True면 True 리턴, 하나라도 틀리면 False 리턴

```python
print(all([True, True, True, True]))	#True
print(all([True, True, False, True]))	#False
print(all([False, False, False]))			#False

print(all([8,3,5]))				#True
print(all([8,3,5,0]))			#False
print(all([8,3,5,None]))	#False
```



## Any

조건 중 하나라도 맞으면 True 리턴

```python
print(any([True, True, True, True]))	#True
print(any([True, True, False, True]))	#True
print(any([False, False, False]))			#False

print(any([8,3,5]))				#True
print(any([8,3,5,0]))			#True
print(any([8,3,5,None]))	#True

print(any(['']))		#False
print(any([]))			#False
```

