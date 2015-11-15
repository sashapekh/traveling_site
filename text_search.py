__author__ = 'sashapekh'

from lab4.Print_file import result


dec = result()

list = dec['text']


str = b'\xd0\xba\xd0\xb0\xd0\xba\xd0\xbe\xd0\xb9 \xd1\x82\xd0\xbe \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82\n'

str.decode('UTF-8')

print(type(str))

str.encode('UTF-8')
print(str)