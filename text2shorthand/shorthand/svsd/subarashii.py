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

class CharSubarashii(SvsdChar):
    def __init__(self, name='すばらしい', kana='subarashii',
                 model='SEL5SWL5FP', head_type='SEL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SELSWLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SELSWLFPswl(cls, ta=None, **kwargs):
        pass

