def is_anagram(word, anagramWord):
    word = word.lower()
    anagramWord = anagramWord.lower()

    for letter in word:
        if letter in anagramWord:
            if anagramWord.count(letter) == word.count(letter):
                word = word.replace(letter, '')
                anagramWord = anagramWord.replace(letter, '')

    if len(word) == 0 and len(anagramWord) == 0:
        return True
    return False


result = is_anagram("BoNjOUR", "juorOBN")
print(result)