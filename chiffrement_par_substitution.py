# def chiffre_substitution(chain, offset):
#     word = ""

#     for c in chain:
#         if 'A' <= c <= 'Z':
#             word += chr((ord(c) - ord('A' ) + offset) % 26 + ord('A'))
#         else:
#             word += c
    
#     return word

# def dechiffre_substitution(chain, offset):
#     word = ""

#     for c in chain:
#         if 'A' <= c <= 'Z':
#             word += chr((ord(c) - ord('A' ) - offset) % 26 + ord('A'))
#         else:
#             word += c
    
#     return word

# chain = "HELLO"
# offset = 3

# texte_chiffre = chiffre_substitution(chain, offset)
# texte_dechiffre = dechiffre_substitution(texte_chiffre, offset)

# print(texte_chiffre)
# print(texte_dechiffre)  