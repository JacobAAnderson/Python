# This will call an object stored by pickle

import pickle

loadFrom = open('Desktop/objectTest.pkl','rb')

object = pickle.load(loadFrom)

print object['c']

loadFrom.close()
