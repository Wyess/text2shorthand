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

class CharNimotoduite(SvsdChar):
    def __init__(self, name='に基づいて', kana='nimotoduite',
                 model='SWL10GSE5', head_type='SWL', tail_type='SE', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWLGSE(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSEswl(cls, ta=None, **kwargs):
        pass

