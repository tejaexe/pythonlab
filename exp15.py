def sum_digits(num):
    sum = 0
    while num !=0:
        ele = num%10
        sum += ele
        num = num//10
    return sum
print(sum_digits(6757))
    