import Utils

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
y = pow(-10, 17-2, 17)
print(y)