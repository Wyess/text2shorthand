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

class CharMatsu(SvsdChar):
    def __init__(self, name='まつ', kana='matsu',
                 model='NER20OR1', head_type='NER', tail_type='NEROR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NEROR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERORswl(cls, ta=None, **kwargs):
        pass

