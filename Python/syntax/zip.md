# zip

동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수

```python
Number=[1,2,3,4]
Name=['hong', 'gil', 'dong', 'nim']
dic={}

for num, name in zip(Number, Name):
  dic[number]=name

print(dic)	# {1: 'hong', 2:'gil', 3:'dong', 4:'nim'}
```

<br/>

- 글자 비교 가능 

```python
a='hit'
b='hot'

for x,y in zip(a,b):
  if x != y:
    print('다르다')
  else: 
    print('같다')
    	
# '다르다' if x!=y else '같다' 
      
# 같다		#('h', 'h')
# 다르다		#('i', 'o')
# 같다 		#('t', 't')
```



> 프로그래머스_단어변환(bfs) 문제중, **알파벳이 하나만 다른 단어를 찾기 위해 사용한다면?**
>
> > transistable=lambda a,b: sum((1 if x!=y else 0) for x,y in zip(a,b))==1
> >
> > : a와 b를 zip을 이용하여 각 알파벳을 비교
> >
> >   -> 각 알파벳이 비교될 때 두개가 다르다면 1, 같으면 0을 받아 더한다.
> >
> >   -> 더한값이 1이여만 하나만 다른 단어임을 알 수 있음(==1) -> true일때만 리턴
