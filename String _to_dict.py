#Q: A python program to convert a string of values to dictionary 


#input
#f = "x:10,y:11,z:12,a:13,b:14,c:15,d:16"

#sol:

f1 = dict(x.split(':') for x in f.split(','))
print(f1)
print(f1["a"])
print(f1.keys())
print(f1.values())





