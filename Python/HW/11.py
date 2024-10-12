from math import ceil

total = 0
dic = {
    'A': {'price': 380},
    'B': {'price': 1200},
    'C': {'price': 180}
}
for _ in ['A', 'B', 'C']:
    inp = input()
    dic[_]['value'] = inp.split(',')

for i in ['A', 'B', 'C']:
    if dic[i]['value'][0] <= '10':
        total += dic[i]['price'] * dic[i]['value'][0]
    elif dic[i]['value'][0] <= '20':
        total += dic[i]['price'] * dic[i]['value'][0] * dic[i]['value'][1]
    elif dic[i]['value'][0] <= '20':
        total += dic[i]['price'] * dic[i]['value'][0] * dic[i]['value'][1]
    elif dic[i]['value'][0] <= '20':
        total += dic[i]['price'] * dic[i]['value'][0] * dic[i]['value'][1]

print(dic)
