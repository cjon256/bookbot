from collections import Counter

path_to_file = "books/frankenstein.txt"

with open(path_to_file) as f:
    file_contents = f.read()

print(f"--- Begin report of {path_to_file} ---")
words = file_contents.split()
print(len(words))

# probably more obscure than it needs to be
letter_frequency = Counter(
    map(lambda c: c.lower(), filter(lambda c: c.isalpha(), [*file_contents])))
for letter, count in letter_frequency.most_common():
    print(f"The '{letter}' character was found {count} times.")
