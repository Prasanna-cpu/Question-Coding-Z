def reverse_words(sentence:str):
    if len(sentence.split())<=1:
        return sentence

    words=sentence.split(' ',1)
    return reverse_words(words[1])+" "+words[0]

print(reverse_words("I am a boy"))