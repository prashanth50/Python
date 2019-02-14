import re 
regex = r'[a-zA-Z0-9]+ '
m = re.findall(regex, "June 24,August 24")
for match in m:
	print(match)






