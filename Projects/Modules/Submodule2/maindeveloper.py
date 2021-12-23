def fact(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num-1
    return result


num = int(input('Enter the number:\t'))
output = fact(num)
print('The factorial of given number is :', output)