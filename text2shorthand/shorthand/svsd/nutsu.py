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

class CharNutsu(SvsdChar):
    def __init__(self, name='ぬつ', kana='nutsu',
                 model='SER10OR1', head_type='SER', tail_type='SEROR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SEROR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERORswl(cls, ta=None, **kwargs):
        pass

