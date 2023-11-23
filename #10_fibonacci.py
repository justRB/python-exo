def fibonacci(num):
    list = [0, 1]
    while True:
        penultimate = list[len(list) - 2]
        last = list[len(list) - 1]

        sum = penultimate + last

        if (sum < num):
            list.append(sum)
        else:
            return list

result = fibonacci(37)
print(result)