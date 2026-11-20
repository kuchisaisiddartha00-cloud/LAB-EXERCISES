# Program 10: Frequency Counter Using Dictionaries

text = input("Enter a sentence or text: ")
frequency = {}

for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print("\nCharacter frequencies:")
for character, count in sorted(frequency.items()):
    print(repr(character), ":", count)
