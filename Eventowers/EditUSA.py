import pickle
with open('USA.pickle', 'rb') as handle:
    country = pickle.load(handle)

country[43].append(41)

with open('USA.pickle', 'wb') as handle:
    pickle.dump(country, handle)
