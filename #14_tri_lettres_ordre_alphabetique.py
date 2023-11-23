def sort_alphabetically(word):
    list = sorted(word)
    returnWord = ""
    for l in list:
        returnWord += l
    return returnWord

result = sort_alphabetically("deab,ci!hgf")
print(result)