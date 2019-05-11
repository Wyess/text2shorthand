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


class CharNa(ShugiinChar):
    def __init__(self, name='na', kana='な',
                 model='EL9', head_type='EL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)

    
    @classmethod
    def path_EL(cls, ta=None, **kwargs):
        #M168.908443157 172.828558166C176.682757682 178.476741638 188.003311381 176.2204628 193.431510545 172.828558166

        z0 = P(0, -0)
        c0 = P(2.74261, -1.99255)
        c1 = P(6.73625, -1.19659)
        z1 = P(8.65119, -0)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_ELe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_ELswl(cls, ta=None, **kwargs):
        pass

