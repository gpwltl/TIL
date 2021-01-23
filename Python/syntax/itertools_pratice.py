from itertools import product
from itertools import permutations
from itertools import combinations

_list = [1, 3, 5]

# 조합
# 결과 : [(1, 3), (1, 5), (3, 5)]
combi = list(combinations(_list, 2))
print(combi)

# 조합을 개수마다 만들 수 있도록
# 결과 : [(1,), (3,), (5,)]
#       [(1, 3), (1, 5), (3, 5)]
#       [(1, 3, 5)]
ans = []
for i in range(1, len(_list)+1):
    print(list(combinations(_list, i)))
    # 조합만들어진 것에서 합 구하기
    # 결과 : [[1, 3, 5], [4, 6, 8], [9]]
    a = list(map(sum, combinations(_list, i)))
    ans.append(a)
print(ans)

# 순열
# 결과 : [(1, 3), (1, 5), (3, 1), (3, 5), (5, 1), (5, 3)]
perm = list(permutations(_list, 2))
print(perm)

# product
# 결과 : [('0', 'a', '!'), ('0', 'a', '@'), ('0', 'a', '#'), .... ('2', 'c', '#')]
_list = ['012', 'abc', '!@#']
pd = list(product(*_list))
print(pd)
