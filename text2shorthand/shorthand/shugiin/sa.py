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


class CharSa(ShugiinChar):
    def __init__(self, name='sa', kana='さ',
                 model='SR7', head_type='SR', tail_type='SR'):
        super().__init__(name, kana, model, head_type, tail_type)

    @classmethod
    def path_SR(cls, ta=None, **kwargs):
        #M317.5253 75.954841C321.17872 78.961985 322.40594 96.302645 316.8737 100.50908
        z0 = P(0, -0)
        c0 = P(1.28885, -1.06085)
        c1 = P(1.72178, -7.17825)
        z1 = P(-0.22987, -8.66219)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
            endknot(*z1)])

    @classmethod
    def path_SRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SRswl(cls, ta=None, **kwargs):
        pass

class CharZa(CharSa):
    def __init__(self, name='za', kana='ざ',
                 model='SR7', head_type='SR', tail_type='SR'):
        super().__init__(name, kana, model, head_type, tail_type)
