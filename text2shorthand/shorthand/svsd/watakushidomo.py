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

class CharWatakushidomo(SvsdChar):
    def __init__(self, name='私ども', kana='watakushidomo',
                 model='UNR5P', head_type='NER', tail_type='SER', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UNRP(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UNRPswl(cls, ta=None, **kwargs):
        pass

