with open('tom.txt') as infile:
    words = 0
    characters = 0
    for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)

print('слов',words)
print('символов',characters)