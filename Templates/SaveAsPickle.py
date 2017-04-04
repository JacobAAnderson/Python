# Using pickle


import pickle
print ('\npickle protocol: ' + str(pickle.HIGHEST_PROTOCOL)+'\n')

# Set up dictionary--------------------------------

state = {'a': 'line Conter',
         'b': 1,
    'c': None }


print state['a']

# Open / Create file to be saved to ---------------------
saveTo = open('Desktop/objectTest.pkl','wb')
# Pickle it!! -------------------------------------------
pickle.dump(state,saveTo,pickle.HIGHEST_PROTOCOL)

saveTo.close()
