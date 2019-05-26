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

class CharHana(SvsdChar):
    def __init__(self, name='はな', kana='hana',
                 model='USWL2CL1', head_type='SEL', tail_type='NELCL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_USWLCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USWLCLswl(cls, ta=None, **kwargs):
        pass

