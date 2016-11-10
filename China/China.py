import pickle
with open('China.pickle', 'rb') as handle:
  China = pickle.load(handle)

print China
