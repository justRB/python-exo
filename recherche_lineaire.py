def linear_research(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

list = [4, 2, 9, 3, 5, 7, 8, 1]
result = linear_research(list, 81)
print(result)
