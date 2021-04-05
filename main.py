import solver


ordinal = solver.ordinal
_split = lambda x: x.split(', ') if ' ' in x else x.split(',')

indicators = {
    'SND': False,
    'CLR': False,
    'CAR': False,
    'IND': False,
    'FRQ': False,
    'SIG': False,
    'NSA': False,
    'MSA': False,
    'TRN': False,
    'BOB': False,
    'FRK': False
}

serial = input("Serial number? ")
battery_count = int(input("Battery count? "))

lit_indicators = input("Enter lit indicators separated by a comma: ").upper()
lit_indicators = _split(lit_indicators)

for indicator in lit_indicators:
    indicators[indicator] = True

while True:
    module_name = input("Module name? ").lower()

    if module_name == 'done':
        break

    elif module_name == "wires":
        wires_list = input("Enter the wires' colors separated by a comma: ").lower()
        wires_list = _split(wires_list)

        print("Cut the \"%s Wire\"" % ordinal(solver.wires(wires_list, serial)))

    elif module_name == "button":
        color = input("Button's color? ")
        text = input("Button's text? ")

        print("%s" % solver.button({"color": color, "text": text}, battery_count, indicators).upper())

    elif module_name == "simon says":
        solver.simon_says(serial)

    elif module_name == "passwords":
        letter_groups = input("Enter the letter groups separated by a comma: ").lower()
        letter_groups = _split(letter_groups)

        print("Enter in \"%s\"" % solver.password(letter_groups))

    elif module_name == "memory":
        solver.memory()
