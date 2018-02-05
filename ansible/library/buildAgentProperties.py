
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import os


def register(params):

  os.system(command)
  has_changed = True

  command = "ls"
  meta = {"params:": command}
  return (has_changed, meta)



def main():
    fields = {
        "package": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)
    has_changed, result = register(module.params)
    module.exit_json(changed=has_changed, meta=result)


if __name__ == "__main__":
    main()