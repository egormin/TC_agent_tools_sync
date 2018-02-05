
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import os


def register(params):

  package = params["package"]
  property_file = params["property_file"]

  has_changed = True

  command = os.system("ls")

  f = open(property_file, "a")
  f.write(package + "\n")
  f.close()

  meta = {"params:": command}
  return (has_changed, meta)



def main():
    fields = {
        "package": {"required": True, "type": "str"},
        "property_file": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)
    has_changed, result = register(module.params)
    module.exit_json(changed=has_changed, meta=result)


if __name__ == "__main__":
    main()