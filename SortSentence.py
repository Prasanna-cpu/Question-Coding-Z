def sorted_sentence(sentence:str):
    words=sentence.split()

    word_dict={}

    for word in words:
        number= ''.join(filter(str.isdigit, word))
        actual_word=''.join(filter(str.isalpha,word))

        word_dict[int(number)]=actual_word

    sorted_words = [word_dict[i] for i in sorted(word_dict)]
    sorted_sentence = ' '.join(sorted_words)

    return sorted_sentence


print(sorted_sentence("Li1ke"))
