import requests

File = open('C:\DeleteUser.xml', 'r')
StringFromFile = File.read()
File.close()

Kek = 4000
"""
while Kek<4010:
    StringFromFileNew = StringFromFile.replace("#$!#$", str(Kek))
    r = requests.post("https://192.168.232.110:8448/mobile_request/get.aspx?admin", data=StringFromFileNew , verify=False)
    Kek += 1
"""
StringFromFileNew1 = StringFromFile.replace("#$!#$", str(4000))
r1 = requests.post("https://192.168.232.110:8448/mobile_request/get.aspx?admin", data=StringFromFileNew1, verify=False)

StringFromFileNew2 = StringFromFile.replace("#$!#$", str(4001))
r2= requests.post("https://192.168.232.110:8448/mobile_request/get.aspx?admin", data=StringFromFileNew2, verify=False)
print ("Done!")