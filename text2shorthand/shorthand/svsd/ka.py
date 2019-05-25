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


class CharKa(SvsdChar):
    def __init__(self, name='ka', kana='か',
                 model='NEL10', head_type='NEL', tail_type='NEL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {'NER'}
    
    @classmethod
    def path_NEL(cls, ta=None, **kwargs):
        #M 160.59751,553.41334 C 171.59476,553.75251 181.30937,543.06349 184.01306,536.85589

        z0 = P(0, -0)
        c0 = z0 + PP(3.88143, -1)
        z1 = z0 + PP(10.117, 35)
        c1 = z1 + PP(2.3886, -113)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_NELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELswl(cls, ta=None, **kwargs):
        pass
