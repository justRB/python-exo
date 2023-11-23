def research_sub_chain(chain, sub_chain):
    for i in range(len(chain) - len(sub_chain) + 1):
        if chain[i:i+len(sub_chain)] == sub_chain:
            return i
    return -1

chain = "oui"
result = research_sub_chain(chain, "u")
print(result)
