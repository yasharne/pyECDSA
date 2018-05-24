import math

import Key
import Point
import EC
# Curve P-224
p = 26959946667150639794667015087019630673557916260026308143510066298881

decimal_q = 26959946667150639794667015087019625940457807714424391721682722368061

b = "b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4"
decimal_b = int(b, 16)

gx = "b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21"
decimal_gx = int(gx, 16)

gy = "bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34"
decimal_gy = int(gy, 16)

G = Point.Point(decimal_gx, decimal_gy)


ec = EC.EC(-3, decimal_b, p, decimal_q, G)

key = Key.Key()
B = key.generate_key(ec)
message = b"this is test"
r, s = key.generate_signature(decimal_q, ec, message)

message1 = b"this is test1"
verify = Key.Key.verify_signature(s, r, decimal_q, message, ec, B)
print('verification: ', verify)
