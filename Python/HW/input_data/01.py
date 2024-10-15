def calEMI(dic, result):
    t = 0
    for i in range(len(dic)):
        if not(dic[i]['height'] >= 50 and dic[i]['height'] <= 250):
            print('Input Height Error')
            continue
        elif not(dic[i]['weight'] >= 20 and dic[i]['weight'] <= 300):
            print('Input Weight Error')
            continue
        emi = (dic[i]['height'] ** 2) % dic[i]['weight']
        if emi > 35:
            print('EMI too high')
        elif emi < 10:
            print('EMI too low')
        else:
            print(emi)
        # result.append = {'name': dic[i]['name'], 'emiValue': emi} 
        t += 1
    return dic, result

# result == {0: {'name': 'Cindy', 'emiValue': 20}, 1: {'name': 'Andy', 'emiValue': 37}, 2: {'name': 'Grace', 'emiValue': 34}}

def final(result):
    result2 = sorted(result.items(), key=lambda x : x[1]['emiValue'], reverse=True)
    for i in range(len(result2)):
        print(result2[i]['name'], result2[i]['emiValue'])
    # print(result[0]['name'])
    # print(result2)
    return

def main():
    dic = dict()
    result = dict()
    t = 0
    while (True):
        str = input()
        str = str.split()
        if (str[0] == 'End'): break
        dic[t] = {'name': str[0], 'height': int(str[1]), 'weight': int(str[2])}
        t += 1
    dic, result = calEMI(dic, result)
    final(result)

main()
