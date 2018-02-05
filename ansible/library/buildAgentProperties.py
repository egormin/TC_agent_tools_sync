
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import os

class XX:

    def register(self, params):
        command = os.system("ls")
        has_changed = True



        #f = open(property_file, "a")
        #f.write(package + "\n")
        #f.close()
        XX.add_parameter(self, params)

        meta = {"params:": command}
        return (has_changed, meta)

    def add_parameter(self, params):
        package = params["package"]
        property_file = params["property_file"]
        f = open(property_file, "a")
        f.write(package + "\n")
        f.close()

def main():
    fields = {
        "package": {"required": True, "type": "str"},
        "property_file": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)
    obj = XX()
    has_changed, result = obj.register(module.params)
    module.exit_json(changed=has_changed, meta=result)


if __name__ == "__main__":
    main()