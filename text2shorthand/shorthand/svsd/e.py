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


class CharE(SvsdChar):
    def __init__(self, name='e', kana='え',
                 model='S10', head_type='S', tail_type='S'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {'S'}
    
    @classmethod
    def path_S(cls, ta=None, **kwargs):
        return pyx.path.line(0, 0, *PP(10, -90))

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
        return cls.jog(cls.path_S())

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
        pass

    @classmethod
    def path_Ssw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Sswl(cls, ta=None, **kwargs):
        pass
