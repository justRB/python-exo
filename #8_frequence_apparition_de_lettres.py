def frequence_caracteres(my_string):
    dictionary = {}
    for letter in my_string:
        if letter not in dictionary:
            dictionary[letter] = 1
        else : 
            dictionary[letter] = int(dictionary[letter] + 1)
    return dictionary

my_string = "Happy Birthday" 
result = frequence_caracteres(my_string)
print(result)

