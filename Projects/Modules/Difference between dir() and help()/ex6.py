# print(__name__)
# print(__file__)
# print(__doc__)
# print(__loader__)
# print(__package__)
# print(__annotations__)
# print(__builtins__)
# print(__cached__)
# print(__spec__)

# def printValidPar(left, right, out):
#     if right == 0:
#         return
#
#     elif left == 0:
#         print(out + right * ")")
#
#     elif left == right:
#         printValidPar(left - 1, right, out + "(")
#
#     else:
#         printValidPar(left - 1, right, out + "(")
#         printValidPar(left, right - 1, out + ")")
#
#     # driver function
#
#
# def validPar(n):
#     printValidPar(n, n, "")
#
#
# n = int(input("Enter the value: "))
# print(validPar(n))


from itertools import permutations
str1 = '()'
n = int(input("Enter the number: "))
str2 = str1*n

li1 = [i for i in str2]

list2 = permutations(li1)
list3 = []
for i in list2:
    a = "".join(i)
    list3.append(a)


li4 = []
for i in list3:
    if i in li4:
        pass
    else:
        li4.append(i)
li5 = []
for value in (li4):
    if value.startswith(')') or value.endswith('('):
        pass
    else:
        li5.append(value)

print(li5)