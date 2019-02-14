#Q: A Python Program to Extract Regular Expression from a  text file

#input:x:10
#y:11
#z:12
#a:13
#b:14
#c:15
#d:16
#ab:23
#bg:32
#vd:232
#vf:22
#as:33
#abbbbbb:28
#abbbb:13

#sol:

import re
pattern = re.compile(r'ab\W\d*')
with open('p2.txt','r') as f:
	contents = f.read()
matches = pattern.findall(contents)
print(matches)
	for match in matches:
		print(match)	

