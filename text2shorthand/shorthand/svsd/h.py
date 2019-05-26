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

class CharH(SvsdChar):
    def __init__(self, name='ー', kana='h',
                 model='UWL1P', head_type='SWL', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UWLP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UWLPswl(cls, ta=None, **kwargs):
        pass

