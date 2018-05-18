import math
import Point
import Utils


class EC(object):

    def __init__(self, a, b, prime, A_prime_order_q, base_point):
        self.a = a
        self.b = b
        self.prime = prime
        self.base_point = base_point
        self.A_prime_order_q = A_prime_order_q

    def addition(self, p, q):
        if p.is_infinite:
            return q
        elif q.is_infinite:
            return p
        elif p != q:
            if (q.x - p.x) == 0:
                point = Point.Point(0, 0)
                point.is_infinite = True
                return point
            s = int(((q.y - p.y) * Utils.Utils.mode_inverse(q.x - p.x, self.prime)) % self.prime)
        xr = int((math.pow(s, 2) - p.x - q.x) % self.prime)
        yr = int(((s * (p.x - xr)) - p.y) % self.prime)
        r = Point.Point(xr, yr)
        return r

    def double(self, p):
        if p.is_infinite:
            return p
        if p.y == 0:
            point = Point.Point(0, 0)
            point.is_infinite = True
            return point
        s = int((((3 * math.pow(p.x, 2)) + self.a) * Utils.Utils.mode_inverse(2 * p.y, self.prime)) % self.prime)
        xr = int((math.pow(s, 2) - p.x - p.x) % self.prime)
        yr = int(((s * (p.x - xr)) - p.y) % self.prime)
        r = Point.Point(xr, yr)
        return r
        pass

    def multiplication(self, p, t):
        bin_t = bin(t)[2:]
        # print('d: ', t)
        # print('bin_b: ', bin_t)
        print('Px: ', p.x)
        print('Py: ', p.y)
        Q = Point.Point(0, 0)
        for i, digit in enumerate(bin_t):
            # print('i: ', i)
            # print('digit: ', digit)
            Q = self.double(Q)
            if digit == '1':
                Q = self.addition(Q, p)
                # print('adding ', Q.x)

            # print("====== ", Q.x)
        return Q
