fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])