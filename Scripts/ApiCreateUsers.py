import requests

File = open('C:\CreateUser.xml', 'r')
StringFromFile = File.read()
File.close()

Kek = 120000

while Kek<200000:
    StringFromFileNew = StringFromFile.replace("#$!#$", str(Kek))
    r = requests.post("https://192.168.232.189:8448/mobile_request/get.aspx?admin", data=StringFromFileNew , verify=False)
    Kek += 1

print ("Done!")
