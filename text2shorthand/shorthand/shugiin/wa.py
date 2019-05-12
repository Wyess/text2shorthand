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


class CharWa(ShugiinChar):
    def __init__(self, name='wa', kana='わ',
                 model='UWL3', head_type='SWR', tail_type='NEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_UWL(cls, ta=None, **kwargs):
        #M -575.32184,-219.07408 C -576.78685,-221.11124 -582.12084,-220.13256 -582.05617,-216.34696 -582.00659,-213.44457 -578.04742,-212.29027 -576.26799,-213.2859
        z0 = P(0, -0)
        c0 = z0 + PP(0.885203, 125)
        z1 = z0 + PP(2.56313, -157)
        #z1 = z2 - PP(2.3099, ta + 303)
        c1 = z1 + PP(1.33567, 90)
        c2 = z1 + PP(1.02405, -89)
        z2 = z1 + PP(2.3099, -27)
        c3 = z2 + PP(0.719325, -150)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_UWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLswl(cls, ta=None, **kwargs):
        pass
