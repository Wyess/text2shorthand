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

class CharIgirisu(SvsdChar):
    def __init__(self, name='イギリス', kana='igirisu',
                 model='SW5GS3', head_type='SW', tail_type='S', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWGS(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWGSswl(cls, ta=None, **kwargs):
        pass

