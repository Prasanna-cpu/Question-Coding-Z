def reverse_each_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Reverse each word and join them back into a single string
    reversed_words = ' '.join(word[::-1] for word in words)

    return reversed_words


print(reverse_each_word("May I come In"))