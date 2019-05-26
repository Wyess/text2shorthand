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

class CharWaku(SvsdChar):
    def __init__(self, name='わく', kana='waku',
                 model='USL5CL5', head_type='USL', tail_type='USLCL5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_USLCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USLCLswl(cls, ta=None, **kwargs):
        pass

