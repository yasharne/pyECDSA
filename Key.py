import random
import hashlib
import Utils

class Key(object):

    def __init__(self):
        pass

    def generate_key(self, ec, d):
        print("generate key called")
        # B = dA
        self.d = d
        point = ec.multiplication(ec.base_point, d)
        print('point x: ', point.x)
        print('point y: ', point.y)
        return point

    def generate_signature(self, q, ec, message):
        ke = random.randint(2, q)
        R = ec.multiplication(ec.base_point, ke)
        # print('random: ', ke)
        r = R.x
        e = hashlib.sha256(message).hexdigest()
        # print('hash: ', int(e, 16))
        # print('self.d * r: ', self.d * r)
        # print('d: ', self.d)
        # print('r: ', r)
        s = ((int(e, 16) + (self.d * r)) * Utils.Utils.mode_inverse(ke, q)) % q
        return r, s
        # return self.generate_key(ec, d)

    @staticmethod
    def verify_signature(s, r, q, message, ec, B):
        w = Utils.Utils.mode_inverse(s, q)
        e = hashlib.sha256(message).hexdigest()
        u1 = w * int(e, 16)
        u2 = (w * r) % q
        P = ec.addition(ec.multiplication(ec.base_point, u1), ec.multiplication(B, u2))
        if  (P.x % q) == (r % q):
            return True
        else:
            return False