#Accept a sentence from the user and create a dictionary that stores the frequency of each word.
sentence = input ("enter a sentence: ")
#split the sentence into words
words = sentence.split()
#create a dictionary to store the frequency of each word
word_frequency = {}
#iterate through the words and count their frequency
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

        #display the word frequency dictionary
        print("\nword frequency dictionary:")
        print(word_frequency)
        