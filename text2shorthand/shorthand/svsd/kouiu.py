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

class CharKouiu(SvsdChar):
    def __init__(self, name='こういう', kana='kouiu',
                 model='EL10SW5FP', head_type='EL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_ELSWFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELSWFPswl(cls, ta=None, **kwargs):
        pass

