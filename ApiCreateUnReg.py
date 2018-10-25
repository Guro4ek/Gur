#!/usr/bin/env python

import requests

File = open("/home/gurin/gur/CreateUserUnReg.xml", "r")

StringFromFile = File.read()
File.close()

Kek = 4040
port = 5077

while Kek<4042:
    StringFromFileNew = StringFromFile.replace("#$!#$", str(Kek))
    StringFromFileNew1 = StringFromFileNew.replace("#!#", str(port))
    r = requests.post("https://192.168.232.110:8448/mobile_request/get.aspx?admin", data=StringFromFileNew1, verify=False)
    print (StringFromFileNew1)
    Kek += 1
    port += 1

print ("Done!")