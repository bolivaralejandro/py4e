try:
    fname = input('Enter a file name: ')
    fhandle = open(fname)
except:
    print('File not found')
    exit()

total = 0
average = 0
count = 0

for line in fhandle:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
         colon_pos = line.find(':')
         extracted_num = float(line[colon_pos+1:])
         total += extracted_num
         count += 1

average = total/count
print('Average spam confidence:',round(average,4))