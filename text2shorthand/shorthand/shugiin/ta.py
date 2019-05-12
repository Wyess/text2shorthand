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


class CharTa(ShugiinChar):
    def __init__(self, name='ta', kana='た',
                 model='S9', head_type='S', tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'S', 'SEL'}

    @classmethod
    def path_S(cls, ta=None, **kwargs):
        #M -733.01432,-220.15909 C -733.0012,-214.09851 -732.98808,-208.03792 -732.97496,-201.97734
        z0 = P(0, -0)
        c0 = z0 + PP(2.13804, -89)
        z1 = z0 + PP(9, -89)
        c1 = z1 + PP(2.13804, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_Se(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Snel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ss(cls, ta=None, **kwargs):
        return ShugiinChar.jog(cls.path_S())

    @classmethod
    def path_Ssl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ssr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ssel(cls, ta=None, **kwargs):
        return ShugiinChar.jog(cls.path_S())

    @classmethod
    def path_Ssw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sswl(cls, ta=None, **kwargs):
        pass

class CharDa(CharTa):
    def __init__(self, name='da', kana='だ',
                 model='S7', head_type='S', tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)
