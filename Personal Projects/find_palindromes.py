word = input("enter a word: ")
spaceless = word.replace(" ", "")
lowercase = spaceless.lower()
word_backwards = lowercase[::-1]

while not lowercase.isalpha():
    print(f"{word} is invalad")
    word = input("enter a word: ")
    spaceless = word.replace(" ", "")
    lowercase = spaceless.lower()
    word_backwards = lowercase[::-1]

if spaceless == word_backwards:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
