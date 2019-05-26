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


class CharKi(SvsdChar):
    def __init__(self, name='ki', kana='き',
                 model='SWL10', head_type='SWL', tail_type='SWL',
                 soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        self.tail_ligature = {'S', 'NEL', 'SEL', 'EL', 'SWR', 'SR'}
    
    @classmethod
    def path_SWL(cls, ta=None, **kwargs):
        #M 187.95946,574.67849 C 179.76943,582.81887 173.39262,595.06803 177.03343,600.8267
        z0 = P(0, -0)
        c0 = z0 + PP(4.07367, -135)
        z1 = z0 + PP(9.99742, -112)
        c1 = z1 + PP(2.4035, 122)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_SWLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWLswl(cls, ta=None, **kwargs):
        pass
