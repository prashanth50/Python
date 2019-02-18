#Q:A Python Program to add 1 at the end of an array
#input = [1,2,9]
#output = [1,2,1,0]


#sol:

def addOne(a):

    n = a[-1]+1
    if n <= 9:
        input.pop()
        input.insert(len(a), n)

    else:
        input.pop()
        n1 = n/10
        a.insert(len(input), n1)
        n2 = n%10
        a.insert(len(input), n2)
    return input

print(addOne(input))
