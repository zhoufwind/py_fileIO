import time
import fileinput

for line in fileinput.input('f1.txt',inplace=1,backup='.bak'):
	line = line.replace('replace content','haha+++')
	print line,

"""
f = file('f1.txt')
file_content = f.readlines()
print file_content,
"""

"""
f = file('f1.txt','w')

for line in range(10):
	time.sleep(1)
	f.write("This is line: %s!\n" % line)
	f.flush()

f.close()
"""
