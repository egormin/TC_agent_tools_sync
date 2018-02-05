
import sys
import re


def main():
    file_name = sys.argv[1]
    variable = sys.argv[2].split("-")[0] + "-" + sys.argv[2].split("-")[1]

    if find_variable(variable, file_name):
        print("Present")
    else:
        add_variable(variable, file_name)


    print(file_name)
    print(variable)


def find_variable(var, file_name):
    from_file = open(file_name, "r")
    line = from_file.readline()
    while line:
        if var in line:
            return True
        line = from_file.readline()
    from_file.close()
    return False

def add_variable(var, file_name):
    print("added")
    with open(file_name, 'r') as f:
        lines = f.readlines()

    with open(file_name, 'w') as f:
        for i, line in enumerate(lines):
            if line == "# Specific Environment Variables\n":
                f.write(line)
                f.write(row_generator(var))
            else:
                f.write(line)


def row_generator(var):
    var = var[::-1].replace('-', '_', 1)[::-1]

    corrected_row = "system.tools."
    for i in range(len(var)):
        corrected_row += var[i].upper() if var[i].isalpha() else var[i]

    corrected_row += "=/buildspace/buildTools/" + var + "\n"
    print(corrected_row)
    return corrected_row



if __name__ == "__main__":
    main()
