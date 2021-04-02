import starting_template


def last_of_instance(list_of_elements, instance):
    return next(i for i in reversed(range(len(list_of_elements))) if list_of_elements[i] == instance) + 1


def last_digit_odd():
    possible_digits = []
    for letter in starting_template.serial:
        if letter.isnumeric():
            possible_digits.append(int(letter))
    if len(possible_digits) >= 1:
        if possible_digits[-1] % 2 != 0:
            return True
    return False


def wires(wires_group):
    wires_list = []

    for wires_group in wires_group:
        if len(wires_group) == 3:
            if "red" not in wires_group:
                wires_list.append(2)
            elif wires_group[-1] == "white":
                wires_list.append(len(wires_group))
            elif wires_group.count("blue") > 1:
                wires_list.append(last_of_instance(wires_group, 'blue'))
            else:
                wires_list.append(len(wires_group))

        elif len(wires_group) == 4:
            if wires_group.count("red") > 1 and last_digit_odd():
                wires_list.append(last_of_instance(wires_group, 'red'))
            elif wires_group[-1] == 'yellow' and wires_group.count("red") == 0:
                wires_list.append(1)
            elif wires_group.count("blue") == 1:
                wires_list.append(1)
            elif wires_group.count("yellow") > 1:
                wires_list.append(len(wires_group))
            else:
                wires_list.append(2)

        elif len(wires_group) == 5:
            if wires_group[-1] == "black" and last_digit_odd():
                wires_list.append(4)
            elif wires_group.count("red") == 1 and wires_group.count("yellow") > 1:
                wires_list.append(1)
            elif wires_group.count("black") == 0:
                wires_list.append(2)
            else:
                wires_list.append(1)

        elif len(wires_group) == 6:
            if wires_group.count("yellow") == 0 and last_digit_odd():
                wires_list.append(3)
            elif wires_group.count("yellow") == 1 and wires_group.count("white") > 1:
                wires_list.append(4)
            elif wires_group.count("red") == 0:
                wires_list.append(len(wires_group))
            else:
                wires_list.append(4)

    return wires_list


def passwords(letter_groups):
    words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn',
             'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their',
             'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']

    passwords_list = []

    for groups in letter_groups:
        possible_words = []
        impossible_words = []

        for letter_group in groups:
            for word in words:
                if word[groups.index(letter_group)] in letter_group:
                    if word not in possible_words and word not in impossible_words:
                        possible_words.append(word)
                else:
                    if word in possible_words:
                        possible_words.remove(word)
                    impossible_words.append(word)

        passwords_list.append(possible_words[0])

    return passwords_list
