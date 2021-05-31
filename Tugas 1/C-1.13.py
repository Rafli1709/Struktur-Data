def myReverse(data):
    return [data[i] for i in range(len(data)-1, -1, -1)]

print(myReverse([1, 2, 3, 4, 5, 6, 7]))
