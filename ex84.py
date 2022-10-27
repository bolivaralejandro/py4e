fname = input('Enter file: ')
try:
    fh = open(fname)
except:
    print('No such file',fname,'exists. Program will terminate.')
    quit()

count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        pieces = words[1]
        count = count + 1
        print(pieces)
    else:
        continue
print('Count is:',count)