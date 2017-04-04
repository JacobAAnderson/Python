# .txt template
# This script will create a text file and read and write to the text file
# The read comands return a list object containing the text from the file.s

with open("Desktop/testfile.txt",'w') as file:
    file.write('Hello World\n')
    file.write('This is a test\n')
    file.write('This is line 3\n')
    file.write('This is line 4\n')


with open("Desktop/testfile.txt",'r') as file:
    print file.read()


with open("Desktop/testfile.txt",'r') as file:
    print file.readline(3)


with open("Desktop/testfile.txt",'r') as file:
    words =()
    for line in file:
        print(line)
        words = line.split()
        print words


file.close()


