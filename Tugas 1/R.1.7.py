def odd_squares_sum(n):
    return sum(x*x for x in range(1,n) if x%2==1)


print(odd_squares_sum(6))