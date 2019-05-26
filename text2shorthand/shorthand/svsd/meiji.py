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

class EraMeiji(SvsdChar):
    def __init__(self, name='明治', kana='meiji',
                 model='M', head_type='P', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_M(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Me(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ms(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Msl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Msr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Msel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Msw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Mswl(cls, ta=None, **kwargs):
        pass

