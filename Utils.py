
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
        if a < 0 or m <= a:
            a = a % m

        # From Ferguson and Schneier, roughly:

        c, d = a, m
        uc, vc, ud, vd = 1, 0, 0, 1
        while c != 0:
            q, c, d = divmod(d, c) + (c,)
            uc, vc, ud, vd = ud - q * uc, vd - q * vc, uc, vc

        # At this point, d is the GCD, and ud*a+vd*m = d.
        # If d == 1, this means that ud is a inverse.

        assert d == 1
        if ud > 0:
            return ud
        else:
            return ud + m

        # return pow(a, m - 2, m)
    # @staticmethod
    # def mode_inverse(a, b):
    #     return mod_inverse(a, b)

