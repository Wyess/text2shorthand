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

class CharNimotoduki(SvsdChar):
    def __init__(self, name='に基づき', kana='nimotoduki',
                 model='SWL10GCSEL5', head_type='SWL', tail_type='CSEL5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWLGCSEL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGCSELswl(cls, ta=None, **kwargs):
        pass

