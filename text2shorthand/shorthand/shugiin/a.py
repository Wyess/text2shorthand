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


class CharA(ShugiinChar):
    def __init__(self, name='a', kana='あ',
                 model='EL3', head_type='EL', tail_type='EL'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {}
        self.tail_ligature -= {'E', 'SR', 'S', 'EL', 'SEL', 'ER', 'NER', 'SWL'}

    
    @classmethod
    def path_EL(cls, ta=None, **kwargs):
        #M -804.71298,-208.5292 C -803.35568,-206.56471 -798.58558,-206.21673 -796.19767,-208.55703

        #z0 = P(0, -0)
        #c0 = P(0.478825, -0.693028)
        #c1 = P(2.16161, -0.815788)
        #z1 = P(3.00401, 0.00981781)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.478825, -0.693028)
        #z1 = z0 + P(3.00401, 0.00981781)
        #c1 = z1 + P(-0.842402, -0.825606)

        z0 = P(0, -0)
        c0 = z0 + PP(0.842355, -55-20)
        z1 = z0 + PP(3.00403, 0)
        c1 = z1 + PP(1.17952, -135+20)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            #curve(),
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

