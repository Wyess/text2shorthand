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


class CharYa(ShugiinChar):
    def __init__(self, name='ya', kana='や',
                 model='NER9', head_type='NER', tail_type='NER'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {'SR'}
        self.tail_ligature -= {'SR', 'S', 'EL', 'SEL', 'SWL'}

    @classmethod
    def path_NER(cls, ta=None, **kwargs):
        #M156.310128498 362.621536242C155.068997827 356.212531454 160.0441439 344.031048327 173.376843324 344.973038492
        z0 = P(0, -0)
        c0 = P(-0.437843, 2.26095)
        c1 = P(1.31728, 6.55831)
        z1 = P(6.02076, 6.226)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_NERe(cls, ta=None, **kwargs):
        #M 191.691,550.63 C 190.45,544.221 195.84721,529.52156 208.758,532.981

        z0 = P(0, -0)
        c0 = P(-0.437797, 2.26095)
        c1 = P(1.46622, 7.44659)
        z1 = P(6.02086, 6.22617)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_NERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNER(cls, ta=None, **kwargs):
        #M 97.4812,291.924 C 100.02065,287.51646 108.99848,277.11455 121.66433,275.16554

        z0 = P(0, -0)
        c0 = P(0.895862, 1.55488)
        c1 = P(4.06304, 5.22444)
        z1 = P(8.53127, 5.91201)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_srNERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERswl(cls, ta=None, **kwargs):
        pass
