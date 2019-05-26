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

class CharRetsu(SvsdChar):
    def __init__(self, name='れつ', kana='retsu',
                 model='SR5OR1', head_type='SR', tail_type='SROR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SROR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRORswl(cls, ta=None, **kwargs):
        pass

