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

class CharEtsu(SvsdChar):
    def __init__(self, name='えつ', kana='etsu',
                 model='S10OR1', head_type='S', tail_type='SOR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SOR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SORswl(cls, ta=None, **kwargs):
        pass

