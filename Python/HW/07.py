MAX_INT = 9223372036854775807

plan = {
    '183': {
        'price': 183,
        'callInZone': 0.08,
        'callOutZone': 0.139,
        'callHome': 0.135,
        'txtInZone': 1.128,
        'txtOutZone': 1.483,
        'freeBW': 1,
        'buyBndWdth': 250
    },
    '383': {
        'price': 383,
        'callInZone': 0.07,
        'callOutZone': 0.130,
        'callHome': 0.121,
        'txtInZone': 1.128,
        'txtOutZone': 1.483,
        'freeBW': 3,
        'buyBndWdth': 200
    },
    '983': {
        'price': 983,
        'callInZone': 0.06,
        'callOutZone': 0.108,
        'callHome': 0.101,
        'txtInZone': 1.128,
        'txtOutZone': 1.483,
        'freeBW': 5,
        'buyBndWdth': 150
    },
    '1283': {
        'price': 1283,
        'callInZone': 0.05,
        'callOutZone': 0.100,
        'callHome': 0.090,
        'txtInZone': 1.128,
        'txtOutZone': 1.483,
        'freeBW': MAX_INT,
        'buyBndWdth': 0
    }
}

callTimeOfInZone = int(input())
callTimeOfOutZone = int(input())
callTimeOfHome = int(input())
amountOfTxtInZone = int(input())
amountOfTxtOutZone = int(input())
bandwidth = int(input())

cheapestPrice = MAX_INT
cheapestPlan = MAX_INT

for i in ['183', '383', '983', '1283']:
    price = 0.0
    # price = plan[i]['callInZone'] * callTimeOfInZone + plan[i]['callOutZone'] * callTimeOfOutZone + plan[i]['callHome'] * callTimeOfHome + plan[i]['txtInZone'] * amountOfTxtInZone + plan[i]['txtOutZone'] * amountOfTxtOutZone
    price = round(plan[i]['callInZone'] * callTimeOfInZone, 2) + round(plan[i]['callOutZone'] * callTimeOfOutZone, 2) + round(plan[i]['callHome'] * callTimeOfHome, 2) + round(plan[i]['txtInZone'] * amountOfTxtInZone, 2) + round(plan[i]['txtOutZone'] * amountOfTxtOutZone, 2)
    if bandwidth > plan[i]['freeBW']:
        price += (bandwidth - plan[i]['freeBW']) * plan[i]['buyBndWdth']
    if price < plan[i]['price']:
        price = plan[i]['price']
    if price < cheapestPrice:
        cheapestPrice = price
        cheapestPlan = i

print(int(cheapestPrice))
print(cheapestPlan)
