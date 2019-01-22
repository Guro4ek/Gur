import requests
from lxml.html import etree
import base64
from requests_ntlm import HttpNtlmAuth
import sys
import re


reload(sys)
sys.setdefaultencoding('utf8')

addres ='http://www.satel.local/sites/satel/employees/SitePages/ourteam.aspx'

class Vcard:
    def __init__(self, name, ext, url):
        self.name = name
        self.ext = ext
        self.url = 'http://www.satel.local' + url

response = requests.get(addres,auth=HttpNtlmAuth('gurin', 'QWErty123'))
infa = response.content

parser = etree.HTMLParser()
root = etree.fromstring(infa, parser)
#i = 0
#for photos in root.cssselect('.ForEmployeeTableColoredRightBorderForPhoto img'):
#    ph = photos.get('src')
#    photo = 'http://www.satel.local' + ph
#    Istring = str(i)
#    print  Istring + photo
#    i = i + 1

#j = 0
#for rows in root.cssselect('.ForEmployeeTable tr'):
#    row = rows.cssselect('td')
#    if (len(row) > 0):
#        Jstring = str(j)
#        print Jstring + 'Name: ' + row[1][0].text + "  " + 'EXT: ' + row[5].text
#    j = j + 1
variable = []
employyes = root.cssselect('.ForEmployeeTable tr')
i = 0
while i < len(employyes):
    emp = employyes[i].cssselect('td')
    if ((len(emp) > 0) and (emp[5].text.isdigit())):
        q = emp[5].text
        variable.append(Vcard(emp[1][0].text, emp[5].text, emp[0][0][0].get('src')))
    i += 1

i = 0
file = open('log.txt', 'w')
while i < len(variable):
    #print variable[i].name
    response = requests.get(variable[i].url, auth=HttpNtlmAuth('gurin', 'QWErty123'))
    photo = base64.encodestring(response.content)
    ph1 = re.sub('\n', '', photo)
    ph2 = ph1[0:49] + '\n'
    possision = 49
    while possision <= len(ph1):
        ph2 += ' ' + ph1[possision:possision + 75] + '\n'
        possision += 75
    vcard = 'BEGIN:VCARD\n' \
            'VERSION:3.0\n' \
            'N:{};;;;\n' \
            'ORG:SATEL;\n' \
            'PHOTO;TYPE=JPEG;ENCODING=b:{}' \
            'TEL:{}\n' \
            'END:VCARD'.format(variable[i].name, ph2, variable[i].ext)

    vc= re.sub('\n', '', base64.encodestring(vcard))
    comand = '<commands>' \
             '<authorize>' \
             '<login>support</login>' \
             '<password>Q2w!zer#45t</password>' \
             '</authorize>' \
             '<command name="Create" table="Contact">' \
             '<group_guid>766a92cf-b7f9-4492-872b-7fa0689cb874</group_guid>' \
             '<name>{}</name>' \
             '<number>{}</number>' \
             '<vcard>{}</vcard>' \
             '</command>' \
             '</commands>'.format(variable[i].name, variable[i].ext, vc)
    r = requests.post("https://pbx.lnt.local:8448/mobile_request/get.aspx?admin", data=comand, verify=False)
    file.write(r.content)
    i += 1

file.close()



