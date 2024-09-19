def single_root_words(root_word, *other_words):
    same_words = []
    d_ = root_word.upper()
    for i in other_words:
        j_ = i.upper()
        if d_ in j_ or j_ in d_:
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
