from typing import List

def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)

data1 = [3, 4, 6, 9, 5]
data2 = [1, 10, 2, 6, 5, 2]

print(areDistinct(data1))
print(areDistinct(data2))
