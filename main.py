def passwords(*letter_groups):
    words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn',
             'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their',
             'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']

    possible_words = []
    impossible_words = []

    for letter_group in letter_groups:
        for word in words:
            if word[letter_groups.index(letter_group)] in letter_group:
                if word not in possible_words and word not in impossible_words:
                    possible_words.append(word)
            else:
                if word in possible_words:
                    possible_words.remove(word)
                impossible_words.append(word)

    return possible_words


password = passwords('', '', '', '', '')
