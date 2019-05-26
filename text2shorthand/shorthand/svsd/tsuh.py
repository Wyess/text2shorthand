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

class CharTsuh(SvsdChar):
    def __init__(self, name='つー', kana='tsuh',
                 model='SE5CL1FP', head_type='SE', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SECLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SECLFPswl(cls, ta=None, **kwargs):
        pass

