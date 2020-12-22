# -*- coding: utf-8 -*-
# for in list : 코드를 필요한만큼 반복해서 실행(순회할 리스트가 정해져 있을 때)
list = ['a', 'b', 'c']
for i in list:
    print(i)
    # 결과: a
    #      b
    #      c

# for in range : 필요한 만큼의 숫자를 만들어내는 유용한 기능(순회할 횟수가 정해져 있을 때)
for i in range(5):
    print(i)
    # 결과: 0
    #      1
    #      2
    #      3
    #      4


# len 함수 : len(s) 입력값 s의 길이를 리턴하는 함수
len("python")  # 결과: 6
len([1, 2, 3])  # 결과: 3
len((1, 'a'))  # 결과: 2

# for in enumerate
# enumerate 함수 : 리스트가 있을 경우 순서와 값을 전달하는 기능
# -> 반복되는 구간에서 객체가 현재 어느 위치인지 알려주는 인덱스 값 필요할 때 유용함
for i, val in enumerate(['body', 'foo', 'bar']):
    print(i, val)
    # 결과: (0, 'body')
    #      (1, 'foo')
    #      (2, 'bar')
