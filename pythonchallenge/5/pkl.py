import pickle, pprint

pkl_file = open('banner.p', 'rb')

data = pickle.load(pkl_file)

for sl in data:
    str = ''
    for (a, b) in sl:
        str += a*b
    print str

pkl_file.close()
