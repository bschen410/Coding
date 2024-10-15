from math import ceil

dic = {
    'A': {'price': 380},
    'B': {'price': 1200},
    'C': {'price': 180}
}
for _ in ['A', 'B', 'C']:
    inp = input()
    dic[_]['value'] = [int(i) for i in inp.split(',')]


# for i in ['A', 'B', 'C']:
#     if dic[i]['value'][0] <= '10':
#         dic[i]['total'] = dic[i]['price'] * dic[i]['value'][0]
#     elif dic[i]['value'][0] <= '20':
#         dic[i]['total'] = ceil(dic[i]['price'] * dic[i]['value'][0] * dic[i]['value'][1] / 100)
#     elif dic[i]['value'][0] <= '30':
#         dic[i]['total'] = ceil(dic[i]['price'] * dic[i]['value'][0] * dic[i]['value'][2] / 100)
#     elif dic[i]['value'][0] >= '31':
#         dic[i]['total'] = ceil(dic[i]['price'] * dic[i]['value'][0] * dic[i]['value'][3] / 100)

# dic = sorted(dic, key=lambda x : dic[x]['total'], reverse=True)
print(dic)
# print(dic['A']['total'] + dic['B']['total'] + dic['C']['total'])
