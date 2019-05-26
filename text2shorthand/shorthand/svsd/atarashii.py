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

class CharAtarashii(SvsdChar):
    def __init__(self, name='新しい', kana='atarashii',
                 model='NE10SWL5FP', head_type='NE', tail_type='P', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NESWLFP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESWLFPswl(cls, ta=None, **kwargs):
        pass

