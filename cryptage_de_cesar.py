def cesar(chain, offset):
    word = ""
   
    for c in chain:
        if 'A' <= c <= 'Z':
            word += chr((ord(c) - ord('A' ) + offset) % 26 + ord('A'))
        elif 'a' <= c <= 'z':
            word += chr((ord(c) - ord('a' ) + offset) % 26 + ord('a'))
        else:
            word += c
    
    return word

chain = "Bonjour le monde"
result = cesar(chain, 3)
print(result)  
