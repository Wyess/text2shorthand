from ..shugiin.char import ShugiinChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    knot,
    endknot,
    smoothknot,
    tensioncurve,
    controlcurve,
    curve)


class JoshiKaramo(ShugiinChar):
    def __init__(self, name='karamo', kana='からも',
                 model='E9SWR9UNER3', head_type='E', tail_type='SWR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {}

    @classmethod
    def path_ESWRUNER(cls, ta=None, **kwargs):
        #M 247.43012,512.55114 C 254.26421,512.80339 268.95861,512.01784 271.73901,512.6038 280.08844,514.3634 275.51225,526.57522 263.86629,531.19863 261.72633,532.04819 257.71063,532.03128 257.15908,529.81618 256.34653,526.5529 262.29873,521.29149 264.93141,523.38392 266.57347,524.689 264.76781,527.36851 262.11729,529.01215

        z0 = P(0, -0)
        c0 = P(2.41092, -0.0889882)
        c1 = P(7.59477, 0.188136)
        z1 = P(8.57564, -0.0185773)
        c2 = P(11.5211, -0.639325)
        c3 = P(9.90675, -4.94738)
        z2 = P(5.79832, -6.57842)
        c4 = P(5.04339, -6.87813)
        c5 = P(3.62674, -6.87216)
        z3 = P(3.43216, -6.09072)
        c6 = P(3.14551, -4.93951)
        c7 = P(5.24532, -3.0834)
        z4 = P(6.17407, -3.82156)
        c8 = P(6.75335, -4.28197)
        c9 = P(6.11635, -5.22724)
        z5 = P(5.18131, -5.80708)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            endknot(*z5)])


    @classmethod
    def path_ESWRUNERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRUNERswl(cls, ta=None, **kwargs):
        pass
