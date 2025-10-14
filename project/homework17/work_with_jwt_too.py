from asyncio import sleep

import jwt
import datetime

JWT_SECRET= 'my_secret'

payload = {
    "sub" : "9345",
    'user_name' : "Zhenya",
    'age' : 13,
    'my_favorite_city' : "Ternopil",
    'iat' : datetime.datetime.now(datetime.timezone.utc),
    'exp' : datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=500)
}

encode_jwt = jwt.encode(payload=payload, key= JWT_SECRET, algorithm='HS256')
print(encode_jwt)
sleep(15)

decode = jwt.decode(
    jwt = encode_jwt,
    key= JWT_SECRET,
    algorithms=['HS256'],
    options={'verify_signature': False}
)
print(decode)