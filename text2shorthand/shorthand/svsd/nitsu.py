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

class CharNitsu(SvsdChar):
    def __init__(self, name='につ', kana='nitsu',
                 model='SWR10OR1', head_type='SWR', tail_type='SWROR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SWROR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRORswl(cls, ta=None, **kwargs):
        pass

