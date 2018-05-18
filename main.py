import math

import Key
import Point
import EC
import random
import hashlib
# Curve P-224
p = 26959946667150639794667015087019630673557916260026308143510066298881

n = 26959946667150639794667015087019625940457807714424391721682722368061
# seed = ["bd713447", "99d5c7fc", "dc45b59f", "a3b9ab8f", "6a948bc5"]
# c = [5b056c7e 11dd68f4 0469ee7f 3c7a7d74 f7d12111 6506d031 218291fb]
b = "b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4"
decimal_b = int(b, 16)
# print(decimal_b)

gx = "b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21"
decimal_gx = int(gx, 16)

gy = "bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34"
decimal_gy = int(gy, 16)

G = Point.Point(decimal_gx, decimal_gy)







# p = Point(20, 30)
# q = Point(10, 20)

ec = EC.EC(-3, decimal_b, p, n, G)

key = Key.Key()

# print('d: ', d)

d = random.randint(2, n)
B = key.generate_key(ec, d)
print('Bx: ', B.x)
print('By: ', B.y)
message = b"this is test"
r, s = key.generate_signature(n, ec, message)
print('signature: ',r, '  =====', s)

verify = Key.Key.verify_signature(s, r, n, message, ec, B)
print('verification: ', verify)



# ec2 = EC.EC(-3, 3, 17, 0, Point.Point(0,0))
# p2 = Point.Point(3, 2)
# p3 = ec2.multiplication(p2, 24)
# print(p3.x)
# print(p3.y)