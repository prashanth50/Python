#Q:A Python program to rotate the list without for loop

#input = [1,2,3,4,5,6,7]
#k = 5

#sol:

def rotateWF(l, k):

    ctr = 0
    while k > ctr:
        input.insert(0, input.pop())
        ctr += 1

    return input
    print(input)

print(rotateWF(input, k))