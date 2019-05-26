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

class CharNakatta(SvsdChar):
    def __init__(self, name='なかった', kana='nakatta',
                 model='NER10SWL5UNR2', head_type='NER', tail_type='SER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NERSWLUNR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERSWLUNRswl(cls, ta=None, **kwargs):
        pass

