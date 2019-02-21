list_1 = [2,3,1,4,2,3,5,6,8,5,8,9,10,9,6]
s = set(list_1)
list_2 = list(s)
#print(list_2)
n = 3
l = len(list_1)
#print(l)
b = int((len(list_2)/n))

s1 = list_2.__getslice__(0, b)
s2 = list_2.__getslice__(len(s1), len(s1)+b)


#l1 = list(enumerate(s1, 1))
#l2 = list(enumerate(s2, 1))

print(s1,s2)
#print(l1, l2)


