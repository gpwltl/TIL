# 3차원 리스트

리스트= [[[값, 값], [값, 값], [값, 값]],    [[값, 값], [값, 값]]]

**`리스트[높이인덱스][세로인덱스][가로인덱스]`** 	<small>순서주의:star: </small>

![image](https://user-images.githubusercontent.com/44856614/105719297-77bad280-5f65-11eb-994b-96f91f4aceb7.png)

- 3차원 리스트 만들기 

```python
[[[0 for col in range(3)] for row in range(4)] for depth in range(2)]

# [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
```

<br/>

- for, append 이용한 3차원 리스트 만들기

```python
tomato = []
for _ in range(2):
    t = []
    for _ in range(3):
        t.append(list(map(int, input().split())))
    tomato.append(t)
    
# [[[], [], []],  [[], [], []]]
```

