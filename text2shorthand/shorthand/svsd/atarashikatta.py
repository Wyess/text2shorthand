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

class CharAtarashikatta(SvsdChar):
    def __init__(self, name='新しかった', kana='atarashikatta',
                 model='NE10CL1SWL5NEL10_NE5', head_type='NE', tail_type='NE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NECLSWLNEL_NE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NECLSWLNEL_NEswl(cls, ta=None, **kwargs):
        pass

