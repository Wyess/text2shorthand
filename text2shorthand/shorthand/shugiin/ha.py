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


class CharHa(ShugiinChar):
    def __init__(self, name='ha', kana='は',
                 model='SEL9', head_type='SEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_SEL(cls, ta=None, **kwargs):
        #M -681.27222,-213.70215 C -683.11873,-206.94516 -679.74004,-196.41221 -666.78979,-196.50425
        z0 = P(0, -0)
        c0 = z0 + PP(2.47112, -105)
        z1 = z0 + PP(7.93169, -49)
        c1 = z1 + PP(4.56868, -179)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
            endknot(*z1)])

    @classmethod
    def path_SELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELswl(cls, ta=None, **kwargs):
        pass

class CharBa(CharHa):
    def __init__(self, name='ba', kana='ば',
                 model='SEL8', head_type='SEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharPa(CharHa):
    def __init__(self, name='pa', kana='ぱ',
                 model='SEL8', head_type='SEL', tail_type='SEL'):
        super().__init__(name, kana, model, head_type, tail_type)
