#Q:""Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:

#Input: 123
#Output: 321
#"""

#sol:

inp = 123
output = []


def reverse(n):
    while n > 0:
        n1 = n // 10
        n2 = n % 10
        n = n1

        output.append(n2)
        m = map(str, output)
        op = ''.join(m)

    return op


print(reverse(inp))
