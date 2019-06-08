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
        self.tail_ligature -= {'SR', 'S', 'ER', 'NER', 'SWL'}
        self.offset_from_centerline = 4.5

    @classmethod
    def path_SEL(cls, ta=None, **kwargs):
        #M420.159653225 361.748513378C418.177757409 369.144821083 422.129524302 380.54427375 436.284829834 380.297220019

        z0 = P(0, -0)
        c0 = P(-0.699169, -2.60925)
        c1 = P(0.694927, -6.63073)
        z1 = P(5.6886, -6.54357)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_SELe(cls, ta=None, **kwargs):
        #M 0,456.236 C -1.9819,463.633 3.8644578,481.86374 16.1252,474.785

        z0 = P(0, -0)
        c0 = P(-0.69917, -2.6095)
        c1 = P(1.36329, -9.0409)
        z1 = P(5.68861, -6.54368)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

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
