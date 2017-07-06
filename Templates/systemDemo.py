# This is an example of how to accept inputs from the commandline
# Call this scrip in the command line as: python /filepath/systemDemo.py input1 input2 etc..

import sys

sum = int(sys.argv[1])+ int(sys.argv[2])


# Uncomment these lines if you want to see the results
# comment thses lines if you just want the script to return the fianl value
#print("Argv[0] ", sys.argv[0])     # This will return the name of the script
#print("length ",len(sys.argv))     # This will return the number of input arguments, including the name of the script
#print("String " ,str(sys.argv))    # This will return the input arguments as a string

#print("add ", sum)                 # Display the result of the equation above

sys.stdout.write(str(sum))
