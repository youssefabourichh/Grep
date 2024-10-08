def find_word(path, word):
    line = 1
    found = False

    with open(path, 'r') as file:
        textToString = file.read()

    for i in range(len(textToString)):

        if textToString[i] == "\n":
            line += 1
            continue
        
        match = True
        
        for j in range(len(word)):
            if i + j >= len(textToString) or textToString[i + j] != word[j]:
                match = False
                break
        
        if match == True:
            found = True
            return word
        
    if found == False:
        return "No results"

# Exemple d'utilisation
path = "C:\\Users\\az03808\\OneDrive - Alliance\\Bureau\\2024 - 2025\\Renault\\1 Projet Grep\\text.txt"

print(find_word(path, "computer"))         
print(find_word(path, "qdgdzgih"))
print(find_word(path, "sun"))
print(find_word(path, "trees"))