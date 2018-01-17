#!/usr/bin/env python

import sys
sys.path.append("modules")
import requests

artifactory_url = "http://35.192.120.104"
user = "__myUser__"
passwrd = "__myPassword__"

url = artifactory_url + "/artifactory/api/storage/Tools/"
getdata = (requests.get(url, auth=(user, passwrd))).json()

fh = open("ToolsList.txt", "a")
fh.seek(0)
fh.truncate()

for i in range(0, len(getdata["children"])):
    url_child = artifactory_url + "/artifactory/api/storage/Tools" + getdata["children"][i]["uri"]
    getChilddata = (requests.get(url_child, auth=(user, passwrd))).json()
    for j in range(0, len(getChilddata["children"])):
        tool = getChilddata["children"][j]["uri"]
        print(tool)
        fh.write(tool[1:] + "\n")

fh.close
