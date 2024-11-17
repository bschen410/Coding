d = dict()
d['11'] = {}
d['1a'] = []
d['1a'].append('somecourse')
d['1a'].append('test')
# d['1a'].remove('test')
del d['1a'][0]
print(len(d['1a']))
