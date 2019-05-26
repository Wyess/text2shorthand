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

class NumberE12(SvsdChar):
    def __init__(self, name='兆', kana='e12',
                 model='BEFP', head_type='BE', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_BEFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_BEFPswl(cls, ta=None, **kwargs):
        pass

