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

class CharNotsu(SvsdChar):
    def __init__(self, name='のつ', kana='notsu',
                 model='ER10OR1', head_type='ER', tail_type='EROR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_EROR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ERORswl(cls, ta=None, **kwargs):
        pass

