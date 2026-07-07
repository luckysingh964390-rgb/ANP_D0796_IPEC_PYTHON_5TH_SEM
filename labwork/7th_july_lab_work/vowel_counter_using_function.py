#Write a Python program that defines a function count_vowels(text).
def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1

    return count


sentence = input("Enter a sentence: ")

result = count_vowels(sentence)

print("Total number of vowels:", result)