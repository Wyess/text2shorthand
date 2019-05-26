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

class CharKe(SvsdChar):
    def __init__(self, name='け', kana='ke',
                 model='SL10', head_type='SL', tail_type='SL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SL(cls, ta=None, **kwargs):
        #M 135.24026,735.33832 C 130.89193,737.09173 126.19554,757.69317 135.10526,763.68833
        z0 = P(0, -0)
        c0 = z0 + PP(1.65401, -158)
        z1 = z0 + PP(10.0014, -90)
        c1 = z1 + PP(3.78846, 146)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_SLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SLswl(cls, ta=None, **kwargs):
        pass

