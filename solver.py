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


def wires(wires_list):
    if len(wires_list) == 3:
        if "red" not in wires_list:
            return 2
        elif wires_list[-1] == "white":
            return len(wires_list)
        elif wires_list.count("blue") > 1:
            return last_of_instance(wires_list, 'blue')
        else:
            return len(wires_list)

    elif len(wires_list) == 4:
        if wires_list.count("red") > 1 and last_digit_odd():
            return last_of_instance(wires_list, 'red')
        elif wires_list[-1] == 'yellow' and wires_list.count("red") == 0:
            return 1
        elif wires_list.count("blue") == 1:
            return 1
        elif wires_list.count("yellow") > 1:
            return len(wires_list)
        else:
            return 2

    elif len(wires_list) == 5:
        if wires_list[-1] == "black" and last_digit_odd():
            return 4
        elif wires_list.count("red") == 1 and wires_list.count("yellow") > 1:
            return 1
        elif wires_list.count("black") == 0:
            return 2
        else:
            return 1

    elif len(wires_list) == 6:
        if wires_list.count("yellow") == 0 and last_digit_odd():
            return 3
        elif wires_list.count("yellow") == 1 and wires_list.count("white") > 1:
            return 4
        elif wires_list.count("red") == 0:
            return len(wires_list)
        else:
            return 4


def passwords(letter_groups):
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
