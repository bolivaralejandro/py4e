# the re way below look for '@' sign then # followed by non blank characters '^ ' the * means
# many of them or 0 or more times
#
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)

# The split method
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
#print(pieces[1])
host = pieces[1]
print(f'The host is {host}')