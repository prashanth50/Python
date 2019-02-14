#Q : A Python Program to extract sub-groups in a pattern using regular expression  

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

sol:

import re
def extractp(s):
    with open('p4.txt','r') as f:
        r = f.readlines()
        x = None
        for i in r:
            matches = re.match("{0}\W(\d+\s*)\W(\w+)\W(\d+)".format(s), i)

            if matches:
                x = matches.groups()
    return x

print(extractp("Wlan Stat"),"Wlan Stat")

