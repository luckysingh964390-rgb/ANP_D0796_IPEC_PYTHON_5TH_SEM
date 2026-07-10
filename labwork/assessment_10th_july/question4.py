#write a python program that accepts a sentence from the user.

def vowels(s):
    c = 0
    for i in s:
        if i.lower() in "aeiou":
            c += 1
    return c

def consonants(s):
    c = 0
    for i in s:
        if i.isalpha() and i.lower() not in "aeiou":
            c += 1
    return c

def words(s):
    return len(s.split())

def reverse(s):
    return s[::-1]

text = input("Enter Sentence: ")

print("Vowels :", vowels(text))
print("Consonants :", consonants(text))
print("Words :", words(text))
print("Reverse :", reverse(text))