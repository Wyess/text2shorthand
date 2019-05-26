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

class CharNihon(SvsdChar):
    def __init__(self, name='日本', kana='nihon',
                 model='E5_E5', head_type='E', tail_type='E', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_E_E(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Ee(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Eer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Eel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Ene(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Ener(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Enel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Es(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Esl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Esr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Ese(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Eser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Esel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Esw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Eswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_E_Eswl(cls, ta=None, **kwargs):
        pass

