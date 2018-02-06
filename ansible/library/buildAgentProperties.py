
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import os


class Analyse:

    def __init__(self, params):
        self.params = params

    def check(self):

        return True

    def add_parameter(self):
        has_changed = True
        package = params["package"]
        property_file = params["property_file"]
        f = open(property_file, "a")
        f.write(package + "\n")
        f.close()
        meta = {"params:": "Added"}
        return has_changed, meta


def main():
    fields = {
        "package": {"required": True, "type": "str"},
        "property_file": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)
    # obj = Analyse(params)

    has_changed = False
    if Analyse(module.params).check():
        result = {"params:": "ok"}
    else:
        has_changed, result = Analyse(module.params).add_parameter()

    #has_changed, result = Analyse(module.params).check()
    module.exit_json(changed=has_changed, meta=result)


if __name__ == "__main__":
    main()
