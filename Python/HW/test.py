from itertools import combinations

lst = ['12', '23', '45']

for i in combinations(lst, 2):
    print(i[0][0])

