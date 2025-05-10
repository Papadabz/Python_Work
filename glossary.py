programming_words = {'list': 'Stores values that can be changed',
                     'tuple': 'Stores values that cannot be changed',
                     'for loop': 'Used to repeat a process with less code',
                     'if statement': 'Makes it so the code doesnt run without meeting specific requirements',
                     'dictionary': 'Stores values in a list, while also applying more factors than one'}

for word, definition in programming_words.items():
    print(f"{word.title()}: {definition}")
