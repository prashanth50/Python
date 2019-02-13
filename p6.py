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

