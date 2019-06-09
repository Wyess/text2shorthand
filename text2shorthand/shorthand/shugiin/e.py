from ..shugiin.char import ShugiinChar
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


class CharE(ShugiinChar):
    def __init__(self, name='e', kana='え',
                 model='SE3', head_type='SE', tail_type='SE'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        #self.tail_ligature = {}
    
    @classmethod
    def path_SE(self, ta=None, **kwargs):
        return pyx.path.line(0, 0, *PP(3, -45))

    @classmethod
    def path_SEe(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEer(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEel(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEne(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEner(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEnel(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEse(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEser(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEsel(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEs(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEsr(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEsl(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEsw(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEswr(self, ta=None, **kwargs):
        pass

    @classmethod
    def path_SEswl(self, ta=None, **kwargs):
        pass


