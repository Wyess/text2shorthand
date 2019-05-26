from ..svsd.char import SvsdChar
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


class CharKu(SvsdChar):
    def __init__(self, name='ku', kana='',
                 model='SEL10', head_type='SEL', tail_type='SEL',
                 soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        self.tail_ligature = {'E', 'NEL', 'SER', 'ER'}
    
    @classmethod
    def path_SEL(cls, ta=None, **kwargs):
        #M 161.30604,649.79079 C 163.76198,660.38852 175.0209,666.97179 185.1515,665.12922
        z0 = P(0, -0)
        c0 = z0 + PP(3.83772, -76)
        z1 = z0 + PP(10.0022, -32)
        c1 = z1 + PP(3.63248, -169)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
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
