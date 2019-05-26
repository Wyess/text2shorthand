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

class CharArimashite(SvsdChar):
    def __init__(self, name='ありまして', kana='arimashite',
                 model='NE10S5', head_type='NE', tail_type='S', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_NES(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NESswl(cls, ta=None, **kwargs):
        pass

