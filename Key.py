import random
import hashlib
import Utils


class Key(object):

    def __init__(self):
        pass

    def generate_key(self, ec):
        # B = dA
        self.d = random.randint(2, ec.A_prime_order_q)
        point = ec.multiplication(ec.base_point, self.d)

        return point

    def generate_signature(self, q, ec, message):
        ke = random.randint(2, q)
        R = ec.multiplication(ec.base_point, ke)
        r = R.x
        e = hashlib.sha256(message).hexdigest()
        s = ((int(e, 16) + (self.d * r)) * Utils.Utils.mode_inverse(ke, q)) % q
        return r, s

    @staticmethod
    def verify_signature(s, r, q, message, ec, B):
        w = Utils.Utils.mode_inverse(s, q)
        e = hashlib.sha256(message).hexdigest()
        u1 = (w * int(e, 16)) % q
        u2 = (w * r) % q
        tmp1 = ec.multiplication(ec.base_point, u1)
        tmp2 = ec.multiplication(B, u2)
        if tmp1 == tmp2:
            P = ec.double(tmp1)
        else:
            P = ec.addition(tmp1, tmp2)
        if (P.x % q) == (r % q):
            return True
        else:
            return False