import re
def extractp(s):
    with open('p4.txt','r') as f:
        r = f.readlines()
        x=None
        for i in r:
            matches = re.match("{0}\W(.*)".format(s),i)

            if matches:
                x = matches.group(1)
    return x


print(extractp('Tx Stat'),'Tx Stat')