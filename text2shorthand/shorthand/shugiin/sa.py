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
                 model='SR9', head_type='SR', tail_type='SR'):
        super().__init__(name, kana, model, head_type, tail_type)
        #self.tail_ligature -= {'E', 'S', 'EL', 'SEL', 'SWL'}

    @classmethod
    def path_SR(cls, ta=None, **kwargs):
        #M 387.73031,172.99871 C 392.51531,175.98971 395.024,193.291 387.777,197.474

        z0 = P(0, -0)
        c0 = P(1.68804, -1.05516)
        c1 = P(2.57305, -7.15867)
        z1 = P(0.0164712, -8.63434)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
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
        #M 1.48894,98.072 C 6.27394,101.063 7.4116361,116.58973 1.53563,122.547
        z0 = P(0, -0)
        c0 = P(1.68804, -1.05516)
        c1 = P(2.0894, -6.53264)
        z1 = P(0.0164712, -8.63424)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_SRner(cls, ta=None, **kwargs):
        #M 97.4345,267.449 C 102.22,270.44 102.1519,286.13094 97.4812,291.924

        #z0 = P(0, -0)
        #c0 = P(1.68822, -1.05516)
        #c1 = P(1.66419, -6.59057)
        #z1 = P(0.0164747, -8.63424)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.68822, -1.05516)
        #z1 = z0 + P(0.0164747, -8.63424)
        #c1 = z1 + P(1.64772, 2.04366)

        z0 = P(0, -0)
        c0 = z0 + PP(1.99084, -32)
        z1 = z0 + PP(8.63425, -89)
        #c1 = z1 + PP(2.62517, 51)
        c1 = z1 + PP(2.62517, ta)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

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
        #M 292.902,361.843 C 297.687,364.834 301.03147,388.48369 292.949,386.318

        z0 = P(0, -0)
        c0 = P(1.68804, -1.05516)
        c1 = P(2.8679, -9.39824)
        z1 = P(0.0165806, -8.63424)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

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
