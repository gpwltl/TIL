from itertools import product
from itertools import permutations
from itertools import combinations

_list = [1, 2, 3]
combi = list(combinations(_list, 2))
print(combi)

for i in range(1, len(_list)+1):
    print(list(combinations(_list, i)))

perm = list(permutations(_list, 2))
print(perm)

_list = ['012', 'abc', '!@#']
pd = list(product(*_list))
print(pd)
