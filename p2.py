import re
pattern = re.compile(r'ab\W\d*')
with open('p2.txt','r') as f:
	contents = f.read()
matches = pattern.findall(contents)
print matches
#for match in matches:
#	print(match)	

