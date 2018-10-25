import sys
reload(sys)
sys.setdefaultencoding('utf8')

str = 'WWW AAA WWW AAA WWW AAA WWW AAA WWW AAA WWW'

def func (str):
    str1 = str.split(' ')
    str2 = ''
    i = 0
    while i < len(str1):
        str2 += str1[i] + ' '
        i += 2
    return str2

print func(str)