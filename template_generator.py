template = """serial = ""
battery_count = 0

indicators = {
    'SND': 0,
    'CLR': 0,
    'CAR': 0,
    'IND': 0,
    'FRQ': 0,
    'SIG': 0,
    'NSA': 0,
    'MSA': 0,
    'TRN': 0,
    'BOB': 0,
    'FRK': 0
}

password_groups = []
wires_list = []


def main():
    import solver

    if len(password_groups) == 5:
        password = solver.passwords(password_groups)
        print('Set password to "' + password[0].upper() + '"')
    if len(wires_list) >= 3:
        wire = solver.wires(wires_list)
        print("Cut wire #" + str(wire))
"""


def main():
    file = open('starting_template.py', 'w')
    file.write(template)
    file.close()
