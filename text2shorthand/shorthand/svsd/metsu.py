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

class CharMetsu(SvsdChar):
    def __init__(self, name='めつ', kana='metsu',
                 model='UER5OR1', head_type='UER', tail_type='UEROR1', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_UEROR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_UERORswl(cls, ta=None, **kwargs):
        pass

