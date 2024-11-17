isNinthRoundStrike = False
isTenthRoundStrike = False
isNinthRoundSpare = False
isTenthRoundSpare = False

pt = 0

scoreOf91 = int(input())
if scoreOf91 == 10:
    isNinthRoundStrike = True
    pt += 10
if isNinthRoundStrike == False:
    scoreOf92 = int(input())
    if scoreOf91 + scoreOf92 == 10:
        isNinthRoundSpare = True
        pt += 10
    else:
        pt += scoreOf91 + scoreOf92

scoreOf101 = int(input())
if scoreOf101 == 10:
    isTenthRoundStrike = True
    pt += 10
if isTenthRoundStrike == False:
    scoreOf102 = int(input())
    if scoreOf101 + scoreOf102 == 10:
        isTenthRoundSpare = True
        pt += 10
    else:
        pt += scoreOf101 + scoreOf102
if isNinthRoundStrike == True:
    pt += scoreOf101 + scoreOf102
if isNinthRoundSpare == True:
    pt += scoreOf101

if isTenthRoundSpare == True:
    pt += int(input())
if isTenthRoundStrike == True:
    pt += int(input()) + int(input())

print(pt)