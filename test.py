import Utils
import EC
import Point
p = 6277101735386680763835789423207666416083908700390324961279

n = 26959946667150639794667015087019625940457807714424391721682722368061

q = "3045ae6fc8422f64ed579528d38120eae12196d5"
decimal_q = int(q, 16)
print('decimal q: ', decimal_q)

b = "64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1"
decimal_b = int(b, 16)
print('b decimal: ', decimal_b)

gx = "188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012"
decimal_gx = int(gx, 16)
print('decimal gx: ', decimal_gx)

gy = "07192b95ffc8da78631011ed6b24cdd573f977a11e794811"
decimal_gy = int(gy, 16)
print('decimal gy: ', decimal_gy)

# G = Point.Point(decimal_gx, decimal_gy)

# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return g, x - (b // a) * y, y
#
# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m

# # gg = Point.Point(0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21, 0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34)
# gg = Point.Point(decimal_gx, decimal_gy)
# c = ec.multiplication(gg, n)
#
# print('x: ', (c.x))
# print('y: ',(c.y))
# print(c.is_infinite)

# ec.addition_or_double(p,q)

# if (p == q):
#     print("same")

# print(Utils.Utils.mode_inverse(-10, 17))

# y = pow(x, p-2, p)
# y = pow(-10, 17-2, 17)
# print(y)

# ec = EC.EC(-3, decimal_b, p, decimal_q, G)
# # px = 19277929113566293071110308034699488026831934219452440156649784352033
# # py = 19926808758034470970197974370888749184205991990603949537637343198772
# # # px = 0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21
# # # py = 0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34
# # p = Point.Point(px, py)
# #
# # p1 = ec.multiplication(p, 3)
# # print('p1x: ', p1.x)
# # print('p1y: ', p1.y)
# # print(p1.is_infinite)

# def inverseMod(a, m):
#     for i in range(1,m):
#         if ( m*i + 1) % a == 0:
#             return ( m*i + 1) // a
#     return None
# print(inverseMod(410291456034409057173047955134865183764572981289, 1081523794096538032233653362262598443316043615173))
#

# aaa = 26959946667150639794667015087019625940457807714424391721682722368061


# print(Utils.Utils.mode_inverse(410291456034409057173047955134865183764572981289, 1081523794096538032233653362262598443316043615173))