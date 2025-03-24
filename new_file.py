print("Hello, this is a new file!") 
def print_m():
    pattern = [
        "*       *",
        "**     **",
        "* *   * *",
        "*  * *  *",
        "*   *   *",
        "*       *",
        "*       *"
    ]
    return pattern

def print_a():
    pattern = [
        "   ***   ",
        "  *   *  ",
        " *     * ",
        " ******* ",
        " *     * ",
        " *     * ",
        " *     * "
    ]
    return pattern

def print_h():
    pattern = [
        "*     *",
        "*     *",
        "*     *",
        "*******",
        "*     *",
        "*     *",
        "*     *"
    ]
    return pattern

def print_e():
    pattern = [
        "*******",
        "*      ",
        "*      ",
        "****** ",
        "*      ",
        "*      ",
        "*******"
    ]
    return pattern

def print_n():
    pattern = [
        "*     *",
        "**    *",
        "* *   *",
        "*  *  *",
        "*   * *",
        "*    **",
        "*     *"
    ]
    return pattern

def print_d():
    pattern = [
        "*****  ",
        "*    * ",
        "*     *",
        "*     *",
        "*     *",
        "*    * ",
        "*****  "
    ]
    return pattern

def print_r():
    pattern = [
        "****** ",
        "*     *",
        "*     *",
        "****** ",
        "*   *  ",
        "*    * ",
        "*     *"
    ]
    return pattern


# Store the letter patterns in a list
letters = [print_m(), print_a(), print_h(), print_e(), print_n(), print_d(), print_r(), print_a()]

# Print the pattern line by line
for i in range(7):  # Since each letter has 7 rows
    for letter in letters:
        print(letter[i], end="  ")  # Print each row of all letters side by side
    print()  # Move to the next line


name = "MAHENDRA"
pattern = {
    "M": ["*   *", "** **", "* * *", "*   *", "*   *"],
    "A": [" *** ", "*   *", "*****", "*   *", "*   *"],
    "H": ["*   *", "*   *", "*****", "*   *", "*   *"],
    "E": ["*****", "*    ", "*****", "*    ", "*****"],
    "N": ["*   *", "**  *", "* * *", "*  **", "*   *"],
    "D": ["**** ", "*   *", "*   *", "*   *", "**** "],
    "R": ["**** ", "*   *", "**** ", "*  * ", "*   *"],
    "A": [" *** ", "*   *", "*****", "*   *", "*   *"]
}

# Printing the pattern
for i in range(5):  # Each letter has 5 rows
    for letter in name:
        print(pattern[letter][i], end="  ")
    print()

name = "MAHENDRA"
for row in range(7):
    for col in range(len(name)):
        if (col == 0 or col == len(name) - 1) or (row == 0 or row == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


def print_M():
    for row in range(7):
        for col in range(7):
            if col == 0 or col == 6 or (row == col and col <= 3) or (row + col == 6 and col >= 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_A():
    for row in range(7):
        for col in range(7):
            if col == 0 or col == 6 or (row == 3):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_H():
    for row in range(7):
        for col in range(7):
            if col == 0 or col == 6 or row == 3:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_E():
    for row in range(7):
        for col in range(7):
            if col == 0 or row == 0 or row == 3 or row == 6:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_N():
    for row in range(7):
        for col in range(7):
            if col == 0 or col == 6 or row == col:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_D():
    for row in range(7):
        for col in range(7):
            if col == 0 or (col == 6 and row != 0 and row != 6) or (row == 0 or row == 6) and col < 6:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_R():
    for row in range(7):
        for col in range(7):
            if col == 0 or (row == 0 or row == 3) and col < 6 or (col == 6 and row != 0 and row != 3) or (row > 3 and row == col):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_name():
    print_M()
    print()
    print_A()
    print()
    print_H()
    print()
    print_E()
    print()
    print_N()
    print()
    print_D()
    print()
    print_R()
    print()
    print_A()

print_name()


def print_mahendra():
    pattern = [""] * 7  # Creating a list to store each row of the pattern

    # M
    for row in range(7):
        pattern[row] += "*   *   " if row == 0 else ("** **   " if row == 1 else ("* * *   " if row == 2 else "*   *   "))

    # A
    for row in range(7):
        pattern[row] += "  *    " if row == 0 else (" * *   " if row == 1 else ("*****  " if row == 2 else "*   *  "))

    # H
    for row in range(7):
        pattern[row] += "*   *  " if row != 3 else "*****  "

    # E
    for row in range(7):
        pattern[row] += "*****  " if row in [0, 3, 6] else "*      "

    # N
    for row in range(7):
        pattern[row] += "*   *  " if row == 0 else ("**  *  " if row == 1 else ("* * *  " if row == 2 else "*  **  " if row == 3 else "*   *  "))

    # D
    for row in range(7):
        pattern[row] += "****   " if row in [0, 6] else "*   *  "

    # R
    for row in range(7):
        pattern[row] += "****   " if row == 0 else ("*   *  " if row == 1 else ("****   " if row == 2 else "*  *   " if row == 3 else "*   *  "))

    # A
    for row in range(7):
        pattern[row] += "  *    " if row == 0 else (" * *   " if row == 1 else ("*****  " if row == 2 else "*   *  "))

    # Printing the pattern
    for row in pattern:
        print(row)

print_mahendra()
