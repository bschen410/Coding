def match(sec1, sec2, secs, index):
    if sec1 == sec2:
        secs[index] = sec1
        index += 1
    return index

def isConflict(cou1, cou2):
    result = [0, 0]
    secs = [99, 99]
    index = 0
    index = match(cou1[1], cou2[1], secs, index)
    index = match(cou1[2], cou2[1], secs, index)
    if index > 0:
        sections = sorted(secs)
        c_ids = [cou1[0], cou2[0]]
        c_ids = sorted(c_ids)
        result = [c_ids, sections]
    print(result[0])
    print(result[1])

courses = [[202, 11, 22], [101, 22, 55]]
isConflict(courses[0], courses[1])
