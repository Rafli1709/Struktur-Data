def squares_sum(n):
    sum = 0
    for number in range(0,n):
        sum+=number**2
    return sum

print(squares_sum(3)) 