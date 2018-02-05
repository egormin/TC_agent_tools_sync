
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *
import os


def main():
    fields = {
        "package": {"required": True, "type": "str"},
    }


if __name__ == "__main__":
    main()