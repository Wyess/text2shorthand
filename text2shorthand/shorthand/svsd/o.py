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


class CharO(SvsdChar):
    def __init__(self, name='o', kana='お',
                 model='E10', head_type='E', tail_type='E'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature = {'E'}
    
    @classmethod
    def path_E(cls, ta=None, **kwargs):
        return pyx.path.line(0, 0, *PP(10, 0))

    @classmethod
    def path_Ee(cls, ta=None, **kwargs):
        return cls.jog(cls.path_E())

    @classmethod
    def path_Eer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ene(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ener(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Enel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Es(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ese(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eswl(cls, ta=None, **kwargs):
        pass
