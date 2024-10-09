def find(path, word):
    line = 1
    found = False
    words = []

    with open(path, 'r') as file:
        textToString = file.read()
        lines = file.readlines()

    for i in range(len(textToString)):

        if textToString[i] == "\n":
            line += 1
            continue
        
        match = True
        
        for j in range(len(word)):
            
            if i + j >= len(textToString) or textToString[i + j] != word[j]:
                break
        
        if match == True:
            found = True
            words.append(word)
        
    if found == False:
        return "No results"
    else:
        return words