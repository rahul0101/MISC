name = input('file name: ')

f = open(name)
count = 0
for i in f:
    count += 1

print('Number of lines in file: ',count)