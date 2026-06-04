text = input("Enter text for analysis: ")

characters = len(text)
words = len(text.split())

letter_count = {}

for char in text.lower():
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1

print("\nAnalysis Results")
print("Total Characters:", characters)
print("Total Words:", words)

print("\nLetter Frequency:")
for letter, count in sorted(letter_count.items()):
    print(letter, ":", count)