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

class CharUn(SvsdChar):
    def __init__(self, name='うん', kana='un',
                 model='SE10CL1', head_type='SE', tail_type='SECL1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SECL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLswl(cls, ta=None, **kwargs):
        pass

