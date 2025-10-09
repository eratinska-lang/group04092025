#10011010 10011010 10101010 101001010
#101001 011010 101010 101010 101011
#df8g
#11011101 10110100 10110111 10101010

import base64

string = b'hello ** - ()'
encode = base64.b64encode(string)
print(encode)

decoded = base64.b64decode(encode)
print(decoded)