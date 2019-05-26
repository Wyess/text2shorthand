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

class CharNimotoduku(SvsdChar):
    def __init__(self, name='に基づく', kana='nimotoduku',
                 model='SWL10GSE5CL5', head_type='SWL', tail_type='ECL5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWLGSECL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLGSECLswl(cls, ta=None, **kwargs):
        pass

