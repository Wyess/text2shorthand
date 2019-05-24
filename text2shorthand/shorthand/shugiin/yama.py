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


class CharYama(ShugiinChar):
    def __init__(self, name='yama', kana='やま',
                 model='NER9ER9', head_type='NER', tail_type='ER'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.head_ligature = {'SR'}
        self.tail_ligature -= {'E', 'S', 'EL', 'SEL', 'NER'}

    @classmethod
    def path_NERER(cls, ta=None, **kwargs):
        #M 77.684812,528.55516 C 83.448303,499.39632 112.7524,487.52593 123.35315,505.78605

        z0 = P(0, -0)
        c0 = P(2.03323, 10.2866)
        c1 = P(12.3711, 14.4742)
        z1 = P(16.1108, 8.03244)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_NERERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERsw(cls, ta=None, **kwargs):
        #M 0,550.63 C 4.928121,525.69735 32.441373,516.82942 45.6684,527.861

        z0 = P(0, -0)
        c0 = P(1.73853, 8.79568)
        c1 = P(11.4446, 11.9241)
        z1 = P(16.1108, 8.0324)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_NERERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NERERswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERER(cls, ta=None, **kwargs):
        #M 0,267.449 C 12.887565,240.66513 35.298643,226.31696 48.157267,245.25435

        z0 = P(0, -0)
        c0 = P(4.54645, 9.44875)
        c1 = P(12.4526, 14.5105)
        z1 = P(16.9888, 7.82978)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            endknot(*z1)])

    @classmethod
    def path_srNERERe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_srNERERswl(cls, ta=None, **kwargs):
        pass
