# https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-rs256-rsa

import jwt

key = "thisissecret"
encoded = jwt.encode({"some": "payload","like":"user_id"}, key, algorithm="HS256")
print(encoded)

decoded = jwt.decode(encoded, key, algorithms="HS256")
print(decoded)