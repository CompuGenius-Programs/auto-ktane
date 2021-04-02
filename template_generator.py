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

password_groups = []  # A list of lists of letter groups
# (i.e [['rkmdei', 'uyisbl', 'bdkgyo', 'hfgptw', 'blmwtq'], ['rxmdei', 'ugisbl', 'bdkgyp', 'hfgltw', 'blmmtq']])

wires_list = []  # A list of lists of wire colors
# (i.e [["red", "black", "blue"], ["red", "black", "blue", "white", "red"]])


def main():
    import solver

    if len(password_groups) >= 1:
        passwords = solver.passwords(password_groups)
        for password in passwords:
            print("For Password Module %s, enter in \\"%s\\"" % (passwords.index(password) + 1, password.upper()))
        print('\\n')
    if len(wires_list) >= 1:
        wires = solver.wires(wires_list)
        for wire in wires:
            print("For Wire Module %s, cut \\"Wire %s\\"" % (wires.index(wire) + 1, wire))
        print('\\n')
"""


def main():
    file = open('starting_template.py', 'w')
    file.write(template)
    file.close()
