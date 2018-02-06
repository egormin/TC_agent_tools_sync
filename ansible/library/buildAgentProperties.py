
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *


class Analyse:

    def __init__(self, params):
        self.property_file = params["property_file"]
        #self.package = params["package"].split("-")[0] + "-" + params["package"].split("-")[1]
        self.package = params["package"].split("/")[-1]

    def check(self):
        from_file = open(self.property_file, "r")
        line = from_file.readline()
        while line:
            if self.package in line:
                return True
            line = from_file.readline()
        from_file.close()
        return False

    def add_parameter(self):
        with open(self.property_file, 'r') as f:
            lines = f.readlines()

        with open(self.property_file, 'w') as f:
            for i, line in enumerate(lines):
                if line == "# Specific Environment Variables\n":
                    f.write(line)
                    f.write(Analyse.__row_generator(self.package))
                else:
                    f.write(line)

        return "added!"

    @staticmethod
    def __row_generator(var):
        var_inVar = var[::-1].replace('-', '_', 1)[::-1]
        corrected_row = "system.tools."
        for i in range(len(var)):
            corrected_row += var_inVar[i].upper() if var[i].isalpha() else var[i]

        corrected_row += "=/buildspace/buildTools/" + var + "\n"
        print(corrected_row)
        return corrected_row


def main():
    fields = {
        "package": {"required": True, "type": "str"},
        "property_file": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)

    has_changed = False
    if Analyse(module.params).check():
       result = {"params:": "package is already added"}
    else:
       result = Analyse(module.params).add_parameter()
       has_changed = True

    # module.exit_json(changed=has_changed, meta=result)
    module.exit_json(changed=has_changed, meta=result)


if __name__ == "__main__":
    main()
