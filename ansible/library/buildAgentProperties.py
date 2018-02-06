
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import os


class Analyse:

    def __init__(self, params):
        self.params = params
        self.has_changed = False

    def check(self):
        command = os.system("ls")

        add_parameter(self, params)

        meta = {"params:": command}
        return has_changed, meta

    def add_parameter(self):
        has_changed = True
        package = params["package"]
        property_file = params["property_file"]
        f = open(property_file, "a")
        f.write(package + "\n")
        f.close()
        return has_changed, meta


def main():
    fields = {
        "package": {"required": True, "type": "str"},
        "property_file": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)
    #obj = Analyse(params)
    has_changed, result = Analyse(params).check()
    module.exit_json(changed=has_changed, meta=result)


if __name__ == "__main__":
    main()
