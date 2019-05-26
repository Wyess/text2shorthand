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

class CharSaku(SvsdChar):
    def __init__(self, name='さく', kana='saku',
                 model='NEL5CL5', head_type='NEL', tail_type='NEL', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLswl(cls, ta=None, **kwargs):
        pass

