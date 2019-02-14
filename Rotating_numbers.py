#Q: A Python Program to rotate the numbers in a list to the right by 3 steps:
 

#input = [1, 2, 3, 4, 5, 6, 7]
#n = 3


#output = []

#sol:

def rotateR(l, k):
    for i in range(len(l) - k, len(l)):
        output.append(l[i])

    for i in range(0, len(l)-n):
        output.append(l[i])

    return output


print(rotateR(input, n))
