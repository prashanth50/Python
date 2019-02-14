#Q: A Python program to extract subgroup with numbers from a text file using regular expression


#input:
#Tx Stat:200:Werwerwer:1122
#Tx End:200:wewerew:213232
#Wlan Stat:500 :ffff:121323
#ffg
#dszs
#qwe:eg
#zfsdgd

#xsdsgdsg


#sdsfsdg
#sdgsdg
#sdgsdgdsdsteqwq 

#sol:

import re
def extractp(l):
		with open('p4.txt','r') as f:
			r = f.readlines()
		x=None
		for i in r:		
			matches= re.match("{0}\W(\d+)".format(l),i)
						
			if matches:
				x=matches.group(1)
		return x

print (extractp("Tx Stat"),"Tx Stat")
