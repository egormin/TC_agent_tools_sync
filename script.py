
import sys


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
    f = open(file_name, "r")
    lines = f.readlines()
    print(len(lines))
    for i in range(len(lines)):
        print(lines[i])
        if lines[i].startswith("# Specific Environment"):
            lines[i] = lines[i] + "Include below\n"
            #lines.insert(i + 1, "Inserted text")  # Before the line three lines after this, i.e. 2

        f.write(lines)
    f.close()


if __name__ == "__main__":
    main()
