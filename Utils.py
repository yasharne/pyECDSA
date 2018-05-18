

class Utils(object):
    @staticmethod
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = Utils.egcd(b % a, a)
            return g, x - (b // a) * y, y

    @staticmethod
    def mode_inverse(a, m):
        #Not Working with negative values
        # print('a: ', a)
        # print('m: ', m)
        # g, x, y = Utils.egcd(a, m)
        # if g != 1:
        #     raise Exception('modular inverse does not exist')
        # else:
        #     return x % m
        #works for prime modulus
        return pow(a, m - 2, m)