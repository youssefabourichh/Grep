import find as fw

input = input()

input_words = input.split(" ")  

print(input_words)

# python grep.py text.txt

word = input_words[0]
function_name = input_words[1]
path = input_words[2]

print(fw.find(path, word))