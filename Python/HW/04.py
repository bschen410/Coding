h = float(input())
w = int(input())
bmi = int(w / (h * h) * 1000)
t = bmi % 10
if t == 5:
    tmp = bmi // 10
    if (tmp % 10) % 2 == 1:
        bmi += 10
else:
    bmi = round(bmi, -1)
# print(round(bmi, 2))
bmi = bmi // 10
print('%.2f'%(bmi / 100))
