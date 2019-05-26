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

class CharMe(SvsdChar):
    def __init__(self, name='め', kana='me',
                 model='USR5', head_type='SER', tail_type='SWR', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_USR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_USRswl(cls, ta=None, **kwargs):
        pass

