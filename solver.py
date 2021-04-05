import re


def last_of_instance(list_of_elements, instance):
    return next(i for i in reversed(range(len(list_of_elements))) if list_of_elements[i] == instance) + 1


def last_digit_odd(serial):
    possible_digits = []
    for letter in serial:
        if letter.isnumeric():
            possible_digits.append(int(letter))
    if len(possible_digits) >= 1:
        if possible_digits[-1] % 2 != 0:
            return True
    return False


def wires(wires_list, serial):
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
        if wires_list.count("red") > 1 and last_digit_odd(serial):
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
        if wires_list[-1] == "black" and last_digit_odd(serial):
            return 4
        elif wires_list.count("red") == 1 and wires_list.count("yellow") > 1:
            return 1
        elif wires_list.count("black") == 0:
            return 2
        else:
            return 1

    elif len(wires_list) == 6:
        if wires_list.count("yellow") == 0 and last_digit_odd(serial):
            return 3
        elif wires_list.count("yellow") == 1 and wires_list.count("white") > 1:
            return 4
        elif wires_list.count("red") == 0:
            return len(wires_list)
        else:
            return 4


def button(press_button, battery_count, indicators):
    color = press_button["color"]
    text = press_button["text"]

    if color == "blue" and text == "abort":
        return releasing_held_button()
    elif battery_count > 1 and text == "detonate":
        return "press and immediately release button"
    elif color == "white" and indicators['CAR']:
        return releasing_held_button()
    elif battery_count > 2 and indicators['FRK']:
        return "press and immediately release button"
    elif color == "yellow":
        return releasing_held_button()
    elif color == "red" and text == "hold":
        return "press and immediately release button"
    else:
        return releasing_held_button()


def releasing_held_button():
    color = input("What is the color of the strip after holding the button? ")

    if color == "blue":
        return "release when the countdown timer has a \"4\" in any position"
    elif color == "white":
        return "release when the countdown timer has a \"1\" in any position"
    elif color == "yellow":
        return "release when the countdown timer has a \"5\" in any position"
    else:
        return "release when the countdown timer has a \"1\" in any position"


def simon_says(serial):
    vowels = re.compile("[AEIOUaeiou]")

    inputted_colors = []

    while True:
        new_color = input("Newest flashing color? ")

        if new_color == 'done':
            break

        inputted_colors.append(new_color)

        strike_count = int(input("Strike count? "))

        output_colors = []

        for color in inputted_colors:
            if bool(vowels.search(serial)):
                if strike_count == 0:
                    if color == "red":
                        output_colors.append("blue")
                    elif color == "blue":
                        output_colors.append("red")
                    elif color == "green":
                        output_colors.append("yellow")
                    elif color == "yellow":
                        output_colors.append("green")

                elif strike_count == 1:
                    if color == "red":
                        output_colors.append("yellow")
                    elif color == "blue":
                        output_colors.append("green")
                    elif color == "green":
                        output_colors.append("blue")
                    elif color == "yellow":
                        output_colors.append("red")

                elif strike_count == 2:
                    if color == "red":
                        output_colors.append("green")
                    elif color == "blue":
                        output_colors.append("red")
                    elif color == "green":
                        output_colors.append("yellow")
                    elif color == "yellow":
                        output_colors.append("blue")

            else:
                if strike_count == 0:
                    if color == "red":
                        output_colors.append("blue")
                    elif color == "blue":
                        output_colors.append("yellow")
                    elif color == "green":
                        output_colors.append("green")
                    elif color == "yellow":
                        output_colors.append("red")

                elif strike_count == 1:
                    if color == "red":
                        output_colors.append("red")
                    elif color == "blue":
                        output_colors.append("blue")
                    elif color == "green":
                        output_colors.append("yellow")
                    elif color == "yellow":
                        output_colors.append("green")

                elif strike_count == 2:
                    if color == "red":
                        output_colors.append("yellow")
                    elif color == "blue":
                        output_colors.append("green")
                    elif color == "green":
                        output_colors.append("blue")
                    elif color == "yellow":
                        output_colors.append("red")

        print("Press the following colors in order: \"%s\"" % ' - '.join(output_colors).upper())


def password(groups):
    words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn',
             'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their',
             'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']

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

    return possible_words[0]
