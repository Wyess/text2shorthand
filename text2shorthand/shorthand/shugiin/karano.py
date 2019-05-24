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


class JoshiKarano(ShugiinChar):
    def __init__(self, name='karano', kana='からの',
                 model='E9SWR9NE3F', head_type='E', tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {}

    @classmethod
    def path_ESWRNEF(cls, ta=None, **kwargs):
        #M 314.72093,404.54721 C 321.88025,404.80857 337.47594,403.47755 340.18663,404.60177 348.4417,408.02538 348.35439,418.34006 333.04023,422.8395 330.71308,423.52323 323.86461,424.25335 325.4865,422.50868 326.6751,421.23013 329.26028,418.94349 331.09669,417.6196

        z0 = P(0, -0)
        c0 = P(2.52565, -0.092202)
        c1 = P(8.02746, 0.377352)
        z1 = P(8.98373, -0.0192476)
        c2 = P(11.8959, -1.22702)
        c3 = P(11.8651, -4.86581)
        z2 = P(6.46264, -6.45311)
        c4 = P(5.64168, -6.69432)
        c5 = P(3.22569, -6.95189)
        z3 = P(3.79785, -6.33641)
        c6 = P(4.21717, -5.88536)
        c7 = P(5.12916, -5.07869)
        z4 = P(5.777, -4.61165)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            endknot(*z4)])

    @classmethod
    def path_ESWRNEFe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ESWRNEFswl(cls, ta=None, **kwargs):
        pass
