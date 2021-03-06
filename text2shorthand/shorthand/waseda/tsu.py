import math
import re
from ..waseda.char import WasedaChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    knot,
    endknot,
    smoothknot,
    roughknot,
    tensioncurve,
    controlcurve,
    curve)

class CharTsu(WasedaChar):
    def __init__(self, name='tsu', kana='つ',
                 model='S4CR1', head_type='S',
                 tail_type='SCR1'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'ER', 'EL', 'E',
                              'NER', 'NEL', 'NE', 
                              'SER', 'SEL', 'SE',
                              'SR', 'SL', 'S', 
                              'SWR', 'SWL', 'SW'}

    @classmethod
    def path_SCR(cls, ta=None, **kwargs):
        z0 = P(0, 0)
        z1 = P(0, -4)
        z3 = P(0, -3)
        z2 = z3 - PP(1.8, 60)
        
        return pyx.metapost.path.path([
            beginknot(*z0, angle=-92),
            curve(),
            roughknot(*z1, langle=-88),
            curve(),
            knot(*z2),
            curve(),
            endknot(*z3, angle=60)])

    @classmethod
    def path_SCRer(cls, ta=None, **kwargs):
        #M 138.056,123.874 C 137.924,127.652 137.924,131.434 138.056,135.213 138.112,136.816 136.28945,138.11423 135.505,137.0809 135.08032,136.52148 135.17253,136.22813 135.65528,135.58592 136.03322,135.08314 137.31488,134.09004 138.01031,133.70405

        #z0 = P(0, -0)
        #c0 = P(-0.0463927, -1.32782)
        #c1 = P(-0.0463927, -2.65704)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.620871, -5.00487)
        #z2 = P(-0.896574, -4.6417)
        #c4 = P(-1.04583, -4.44508)
        #c5 = P(-1.01342, -4.34198)
        #z3 = P(-0.843757, -4.11627)
        #c6 = P(-0.710926, -3.93956)
        #c7 = P(-0.260474, -3.59053)
        z4 = P(-0.0160582, -3.45487)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463927, -1.32782)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0463927, 1.32817)
        #c2 = z1 + P(0.0196818, -0.56339)
        #z2 = z1 + P(-0.896574, -0.656492)
        #c3 = z2 + P(0.275703, -0.363174)
        #c4 = z2 + P(-0.149258, 0.196614)
        #z3 = z2 + P(0.0528174, 0.525425)
        #c5 = z3 + P(-0.169667, -0.225711)
        #c6 = z3 + P(0.132831, 0.176707)
        #z4 = z3 + P(0.827699, 0.661402)
        #c7 = z4 + P(-0.244416, -0.13566)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32863, -92)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.32898, 92)
        c2 = z1 + PP(0.563734, -87)
        z2 = z1 + PP(1.11123, -143)
        c3 = z2 + PP(0.455969, -52)
        c4 = z2 + PP(0.24685, 127)
        #z3 = z2 + PP(0.528073, 84)
        z3 = z4 - PP(1.0595, ta + 368)
        c5 = z3 + PP(0.282369, -126)
        #c6 = z3 + PP(0.221064, 53)
        #z4 = z3 + PP(1.0595, 38)
        #c7 = z4 + PP(0.27954, -150)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRel(cls, ta=None, **kwargs):
        #M 98.3679,123.874 C 98.200012,127.68789 98.150147,131.51975 98.3679,135.213 98.462306,136.8142 96.357918,137.38603 95.769383,136.22919 95.105441,134.92413 95.513272,133.9507 96.055331,134.26804 96.636072,134.60802 97.617672,134.95919 98.3679,135.213

        #z0 = P(0, -0)
        #c0 = P(-0.0590059, -1.34043)
        #c1 = P(-0.0765314, -2.68717)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0331799, -4.54796)
        #c3 = P(-0.706428, -4.74894)
        #z2 = P(-0.913274, -4.34235)
        #c4 = P(-1.14662, -3.88368)
        #c5 = P(-1.00329, -3.54156)
        #z3 = P(-0.812775, -3.65309)
        #c6 = P(-0.608668, -3.77258)
        #c7 = P(-0.263675, -3.896)
        z4 = P(0, -3.9852)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0590059, -1.34043)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0765314, 1.29803)
        #c2 = z1 + P(0.0331799, -0.562758)
        #z2 = z1 + P(-0.913274, -0.35715)
        #c3 = z2 + P(0.206846, -0.406583)
        #c4 = z2 + P(-0.233349, 0.458676)
        #z3 = z2 + P(0.100499, 0.689266)
        #c5 = z3 + P(-0.190512, 0.111532)
        #c6 = z3 + P(0.204107, -0.119489)
        #z4 = z3 + P(0.812775, -0.332116)
        #c7 = z4 + P(-0.263675, 0.089204)

        z0 = P(0, -0)
        c0 = z0 + PP(1.34173, -92)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.30028, 93)
        c2 = z1 + PP(0.563735, -86)
        z2 = z1 + PP(0.980626, -158)
        c3 = z2 + PP(0.456174, -63)
        c4 = z2 + PP(0.514622, 116)
        #z3 = z2 + PP(0.696554, 81)
        z3 = z4 - PP(0.878012, ta + -3)
        c5 = z3 + PP(0.220758, 149)
        #c6 = z3 + PP(0.236511, -30)
        #z4 = z3 + PP(0.878012, -22)
        #c7 = z4 + PP(0.278356, 161)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRe(cls, ta=None, **kwargs):
        #M 47.3414,123.874 C 47.2095,127.652 47.2095,131.434 47.3414,135.213 47.3974,136.816 45.641621,136.83425 44.605275,136.0527 43.734577,135.39607 43.901948,134.86414 44.541472,134.5894 45.180997,134.31465 46.292675,134.2971 47.310591,134.24814

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32782)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.597404, -4.55501)
        #z2 = P(-0.961638, -4.28032)
        #c4 = P(-1.26765, -4.04955)
        #c5 = P(-1.20883, -3.86259)
        #z3 = P(-0.984062, -3.76603)
        #c6 = P(-0.759295, -3.66947)
        #c7 = P(-0.368585, -3.6633)
        z4 = P(-0.0108281, -3.64609)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32782)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0463576, 1.32817)
        #c2 = z1 + P(0.0196818, -0.56339)
        #z2 = z1 + P(-0.961638, -0.295121)
        #c3 = z2 + P(0.364234, -0.274683)
        #c4 = z2 + P(-0.306015, 0.230779)
        #z3 = z2 + P(-0.0224242, 0.514291)
        #c5 = z3 + P(-0.224767, -0.0965601)
        #c6 = z3 + P(0.224767, 0.0965636)
        #z4 = z3 + P(0.973234, 0.119939)
        #c7 = z4 + P(-0.357757, -0.0172075)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32862, -91)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.32898, 91)
        c2 = z1 + PP(0.563734, -87)
        z2 = z1 + PP(1.0059, -162)
        c3 = z2 + PP(0.456199, -37)
        c4 = z2 + PP(0.383281, 142)
        #z3 = z2 + PP(0.51478, 92)
        z3 = z4 - PP(0.980597, ta + 364)
        c5 = z3 + PP(0.24463, -156)
        #c6 = z3 + PP(0.244632, 23)
        #z4 = z3 + PP(0.980597, 7)
        #c7 = z4 + PP(0.35817, -177)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRner(cls, ta=None, **kwargs):
        #M 121.885,189.071 C 121.753,192.849 121.753,196.631 121.885,200.409 121.941,202.013 121.34737,203.41754 120.51693,202.41985 119.52419,201.22718 121.16569,198.8529 121.885,197.575

        #z0 = P(0, -0)
        #c0 = P(-0.0463927, -1.32782)
        #c1 = P(-0.0463927, -2.65704)
        #z1 = P(0, -3.98485)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.188955, -5.04223)
        #z2 = P(-0.480822, -4.69159)
        #c4 = P(-0.82973, -4.27241)
        #c5 = P(-0.252809, -3.43795)
        z3 = P(0, -2.98881) + P(-0.3, 0)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463927, -1.32782)
        #z1 = z0 + P(0, -3.98485)
        #c1 = z1 + P(-0.0463927, 1.32782)
        #c2 = z1 + P(0.0196818, -0.563742)
        #z2 = z1 + P(-0.480822, -0.706733)
        #c3 = z2 + P(0.291866, -0.350648)
        #c4 = z2 + P(-0.348908, 0.419176)
        #z3 = z2 + P(0.480822, 1.70277)
        #c5 = z3 + P(-0.252809, -0.449131)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32863, -92)
        z1 = z0 + PP(3.98485, -90)
        c1 = z1 + PP(1.32863, 92)
        c2 = z1 + PP(0.564085, -88)
        #z2 = z1 + PP(0.854787, -124)
        z2 = z3 - PP(1.76935, ta + 373)
        c3 = z2 + PP(0.456224, -50)
        #c4 = z2 + PP(0.545385, 129)
        #z3 = z2 + PP(1.76935, 74)
        #c5 = z3 + PP(0.515394, -119)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SCRnel(cls, ta=None, **kwargs):
        #M 84.9787,189.071 C 84.8468,192.849 84.8468,196.631 84.9787,200.409 85.0347,202.013 83.509729,202.52142 82.4276,201.80473 81.448413,201.15622 80.923166,199.26628 81.719829,199.32141 82.398999,199.36842 83.848197,199.28494 84.9787,199.04183

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32782)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.98485)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.516284, -4.72728)
        #z2 = P(-0.896609, -4.4754)
        #c4 = P(-1.24075, -4.24747)
        #c5 = P(-1.42536, -3.58323)
        #z3 = P(-1.14536, -3.60261)
        #c6 = P(-0.906661, -3.61913)
        #c7 = P(-0.397326, -3.58979)
        z4 = P(0, -3.50435)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32782)
        #z1 = z0 + P(0, -3.98485)
        #c1 = z1 + P(-0.0463576, 1.32782)
        #c2 = z1 + P(0.0196818, -0.563742)
        #z2 = z1 + P(-0.896609, -0.490543)
        #c3 = z2 + P(0.380325, -0.251888)
        #c4 = z2 + P(-0.344145, 0.227925)
        #z3 = z2 + P(-0.248753, 0.872787)
        #c5 = z3 + P(-0.279995, 0.019376)
        #c6 = z3 + P(0.238701, -0.0165221)
        #z4 = z3 + P(1.14536, 0.0982612)
        #c7 = z4 + P(-0.397326, -0.0854434)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32862, -91)
        z1 = z0 + PP(3.98485, -90)
        c1 = z1 + PP(1.32862, 91)
        c2 = z1 + PP(0.564085, -88)
        z2 = z1 + PP(1.02203, -151)
        c3 = z2 + PP(0.456174, -33)
        c4 = z2 + PP(0.412778, 146)
        #z3 = z2 + PP(0.907544, 105)
        z3 = z4 - PP(1.14957, ta + 351)
        c5 = z3 + PP(0.280665, 176)
        #c6 = z3 + PP(0.239272, -3)
        #z4 = z3 + PP(1.14957, 4)
        #c7 = z4 + PP(0.40641, -167)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRne(cls, ta=None, **kwargs):
        #M 47.3414,189.071 C 47.2095,192.849 47.2095,196.631 47.3414,200.409 47.3974,202.013 45.734021,202.88508 44.7902,201.994 43.115721,200.41308 45.903529,199.34064 47.3414,198.19012

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32782)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.98485)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.564929, -4.85509)
        #z2 = P(-0.896644, -4.54192)
        #c4 = P(-1.48516, -3.98629)
        #c5 = P(-0.505354, -3.60937)
        z3 = P(0, -3.205)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32782)
        #z1 = z0 + P(0, -3.98485)
        #c1 = z1 + P(-0.0463576, 1.32782)
        #c2 = z1 + P(0.0196818, -0.563742)
        #z2 = z1 + P(-0.896644, -0.557064)
        #c3 = z2 + P(0.331715, -0.313179)
        #c4 = z2 + P(-0.588512, 0.55563)
        #z3 = z2 + P(0.896644, 1.33691)
        #c5 = z3 + P(-0.505354, -0.404362)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32862, -91)
        z1 = z0 + PP(3.98485, -90)
        c1 = z1 + PP(1.32862, 91)
        c2 = z1 + PP(0.564085, -88)
        #z2 = z1 + PP(1.0556, -148)
        z2 = z3 - PP(1.60975, ta + 377)
        c3 = z2 + PP(0.456197, -43)
        #c4 = z2 + PP(0.809365, 136)
        #z3 = z2 + PP(1.60975, 56)
        #c5 = z3 + PP(0.647218, -141)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3, angle=ta)])

    @classmethod
    def path_SCRser(cls, ta=None, **kwargs):
        #M 81.36,327.565 C 81.2281,331.344 81.2281,335.125 81.36,338.904 81.416,340.507 79.961197,341.11837 79.017357,340.2273 78.180102,339.43687 78.050748,336.91823 79.303295,337.26947 80.564112,337.62302 80.72782,337.88005 81.337339,338.21255

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32817)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.491623, -4.76347)
        #z2 = P(-0.823345, -4.45029)
        #c4 = P(-1.11761, -4.17249)
        #c5 = P(-1.16307, -3.28729)
        #z3 = P(-0.722849, -3.41073)
        #c6 = P(-0.279723, -3.53499)
        #c7 = P(-0.222186, -3.62533)
        z4 = P(-0.00796443, -3.74219)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32817)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0463576, 1.32817)
        #c2 = z1 + P(0.0196818, -0.56339)
        #z2 = z1 + P(-0.823345, -0.465087)
        #c3 = z2 + P(0.331722, -0.313175)
        #c4 = z2 + P(-0.294262, 0.277804)
        #z3 = z2 + P(0.100496, 1.03956)
        #c5 = z3 + P(-0.44022, 0.123447)
        #c6 = z3 + P(0.443127, -0.124259)
        #z4 = z3 + P(0.714885, -0.331455)
        #c7 = z4 + P(-0.214221, 0.11686)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32898, -91)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.32898, 91)
        c2 = z1 + PP(0.563734, -87)
        z2 = z1 + PP(0.945623, -150)
        c3 = z2 + PP(0.4562, -43)
        c4 = z2 + PP(0.404679, 136)
        #z3 = z2 + PP(1.0444, 84)
        z3 = z4 - PP(0.787986, ta + 5)
        c5 = z3 + PP(0.457201, 164)
        #c6 = z3 + PP(0.460219, -15)
        #z4 = z3 + PP(0.787986, -24)
        #c7 = z4 + PP(0.244023, 151)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRsel(cls, ta=None, **kwargs):
        #M 121.048,327.565 C 120.916,331.344 120.916,335.125 121.048,338.904 121.104,340.507 120.37105,341.50578 119.28009,340.80234 118.05412,340.01184 118.31636,338.22165 119.27782,337.5234 120.09314,336.93129 121.03475,337.41931 121.048,338.904

        #z0 = P(0, -0)
        #c0 = P(-0.0463927, -1.32817)
        #c1 = P(-0.0463927, -2.65704)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.237921, -4.89962)
        #z2 = P(-0.621349, -4.65239)
        #c4 = P(-1.05223, -4.37456)
        #c5 = P(-0.960062, -3.74538)
        #z3 = P(-0.622147, -3.49998)
        #c6 = P(-0.335595, -3.29188)
        #c7 = P(-0.00465684, -3.46339)
        z4 = P(0, -3.9852)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463927, -1.32817)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0463927, 1.32817)
        #c2 = z1 + P(0.0196818, -0.56339)
        #z2 = z1 + P(-0.621349, -0.66719)
        #c3 = z2 + P(0.383429, -0.247231)
        #c4 = z2 + P(-0.430879, 0.277829)
        #z3 = z2 + P(-0.000797814, 1.15242)
        #c5 = z3 + P(-0.337915, -0.245407)
        #c6 = z3 + P(0.286552, 0.208103)
        #z4 = z3 + P(0.622147, -0.485226)
        #c7 = z4 + P(-0.00465684, 0.521809)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32898, -92)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.32898, 92)
        c2 = z1 + PP(0.563734, -87)
        z2 = z1 + PP(0.911712, -132)
        c3 = z2 + PP(0.456224, -32)
        c4 = z2 + PP(0.512685, 147)
        #z3 = z2 + PP(1.15242, 90)
        z3 = z4 - PP(0.788994, ta + 53)
        c5 = z3 + PP(0.417625, -144)
        #c6 = z3 + PP(0.354145, 35)
        #z4 = z3 + PP(0.788994, -37)
        #c7 = z4 + PP(0.52183, 90)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRse(cls, ta=None, **kwargs):
        #M 47.3414,327.565 C 47.2095,331.344 47.2095,335.125 47.3414,338.904 47.3974,340.507 45.734042,341.37906 44.7902,340.488 43.952942,339.69756 44.272183,337.95877 44.998696,337.26052 45.725208,336.56227 46.576757,338.51347 47.267664,339.34642

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32817)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.564922, -4.85509)
        #z2 = P(-0.896644, -4.54192)
        #c4 = P(-1.19091, -4.26411)
        #c5 = P(-1.07871, -3.65299)
        #z3 = P(-0.823366, -3.40759)
        #c6 = P(-0.568027, -3.16218)
        #c7 = P(-0.268741, -3.84795)
        z4 = P(-0.0259152, -4.1407)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32817)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0463576, 1.32817)
        #c2 = z1 + P(0.0196818, -0.56339)
        #z2 = z1 + P(-0.896644, -0.556712)
        #c3 = z2 + P(0.331723, -0.313172)
        #c4 = z2 + P(-0.294263, 0.277808)
        #z3 = z2 + P(0.073278, 1.13433)
        #c5 = z3 + P(-0.25534, -0.245407)
        #c6 = z3 + P(0.25534, 0.245407)
        #z4 = z3 + P(0.797451, -0.73311)
        #c7 = z4 + P(-0.242826, 0.292749)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32898, -91)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.32898, 91)
        c2 = z1 + PP(0.563734, -87)
        z2 = z1 + PP(1.05541, -148)
        c3 = z2 + PP(0.456198, -43)
        c4 = z2 + PP(0.404682, 136)
        #z3 = z2 + PP(1.13669, 86)
        z3 = z4 - PP(1.08323, ta + 9)
        c5 = z3 + PP(0.354151, -136)
        #c6 = z3 + PP(0.354151, 43)
        #z4 = z3 + PP(1.08323, -42)
        #c7 = z4 + PP(0.38035, 129)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRsr(cls, ta=None, **kwargs):
        #M 132.386,239.691 C 132.255,243.469 132.255,247.251 132.386,251.03 132.442,252.633 131.12069,253.02658 130.17682,252.13545 129.33969,251.34508 129.88554,248.71872 130.73653,248.9798 131.23974,249.13417 131.99485,249.719 132.3629,250.31916

        #z0 = P(0, -0)
        #c0 = P(-0.0460412, -1.32782)
        #c1 = P(-0.0460412, -2.65704)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.444706, -4.68692)
        #z2 = P(-0.776438, -4.37372)
        #c4 = P(-1.07066, -4.09594)
        #c5 = P(-0.878811, -3.17288)
        #z3 = P(-0.579723, -3.26464)
        #c6 = P(-0.402864, -3.3189)
        #c7 = P(-0.137474, -3.52444)
        z4 = P(-0.00811872, -3.73537)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0460412, -1.32782)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0460412, 1.32817)
        #c2 = z1 + P(0.0196818, -0.56339)
        #z2 = z1 + P(-0.776438, -0.388521)
        #c3 = z2 + P(0.331732, -0.313196)
        #c4 = z2 + P(-0.294218, 0.277783)
        #z3 = z2 + P(0.196716, 1.10908)
        #c5 = z3 + P(-0.299089, 0.0917591)
        #c6 = z3 + P(0.176858, -0.0542549)
        #z4 = z3 + P(0.571604, -0.470731)
        #c7 = z4 + P(-0.129355, 0.210932)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32861, -91)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.32896, 91)
        c2 = z1 + PP(0.563734, -87)
        z2 = z1 + PP(0.868219, -153)
        c3 = z2 + PP(0.456222, -43)
        c4 = z2 + PP(0.404633, 136)
        #z3 = z2 + PP(1.12639, 79)
        z3 = z4 - PP(0.740486, ta + 20)
        c5 = z3 + PP(0.312848, 162)
        #c6 = z3 + PP(0.184993, -17)
        #z4 = z3 + PP(0.740486, -39)
        #c7 = z4 + PP(0.247437, 121)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRsl(cls, ta=None, **kwargs):
        #M 89.8639,239.691 C 89.732,243.469 89.732,247.251 89.8639,251.03 89.9199,252.633 88.256564,253.50504 87.3128,252.614 86.475564,251.82354 86.803835,250.13381 87.530322,249.43556 88.25681,248.73731 90.127631,248.45764 89.538929,249.85539

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32782)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.564914, -4.85508)
        #z2 = P(-0.896609, -4.54192)
        #c4 = P(-1.19086, -4.2641)
        #c5 = P(-1.07549, -3.67023)
        #z3 = P(-0.820159, -3.42482)
        #c6 = P(-0.564828, -3.17941)
        #c7 = P(0.0926909, -3.08112)
        z4 = P(-0.114214, -3.57238)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32782)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0463576, 1.32817)
        #c2 = z1 + P(0.0196818, -0.56339)
        #z2 = z1 + P(-0.896609, -0.556712)
        #c3 = z2 + P(0.331695, -0.313165)
        #c4 = z2 + P(-0.294255, 0.277815)
        #z3 = z2 + P(0.0764503, 1.11709)
        #c5 = z3 + P(-0.255331, -0.245407)
        #c6 = z3 + P(0.255331, 0.245407)
        #z4 = z3 + P(0.705945, -0.147553)
        #c7 = z4 + P(0.206905, 0.491253)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32862, -91)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.32898, 91)
        c2 = z1 + PP(0.563734, -87)
        z2 = z1 + PP(1.05538, -148)
        c3 = z2 + PP(0.456173, -43)
        c4 = z2 + PP(0.404681, 136)
        #z3 = z2 + PP(1.11971, 86)
        z3 = z4 - PP(0.7212, ta + 102)
        c5 = z3 + PP(0.354145, -136)
        #c6 = z3 + PP(0.354145, 43)
        #z4 = z3 + PP(0.7212, -11)
        #c7 = z4 + PP(0.533047, 67)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRs(cls, ta=None, **kwargs):
        #M 47.3414,239.691 C 47.2095,243.469 47.2095,247.251 47.3414,251.03 47.3974,252.633 46.636484,253.16525 45.580732,252.614 43.846789,251.70864 44.493344,249.30898 46.052755,248.50571 46.80353,248.11897 47.302702,249.78435 47.3414,251.03

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32782)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.9852)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.24775, -4.73566)
        #z2 = P(-0.618804, -4.54192)
        #c4 = P(-1.22822, -4.22372)
        #c5 = P(-1.00098, -3.38033)
        #z3 = P(-0.452907, -3.09802)
        #c6 = P(-0.18904, -2.96209)
        #c7 = P(-0.0136008, -3.54741)
        z4 = P(0, -3.9852)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32782)
        #z1 = z0 + P(0, -3.9852)
        #c1 = z1 + P(-0.0463576, 1.32817)
        #c2 = z1 + P(0.0196818, -0.56339)
        #z2 = z1 + P(-0.618804, -0.556712)
        #c3 = z2 + P(0.371054, -0.193742)
        #c4 = z2 + P(-0.609411, 0.318198)
        #z3 = z2 + P(0.165897, 1.4439)
        #c5 = z3 + P(-0.54807, -0.282317)
        #c6 = z3 + P(0.263867, 0.135924)
        #z4 = z3 + P(0.452907, -0.887187)
        #c7 = z4 + P(-0.0136008, 0.437796)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32862, -91)
        z1 = z0 + PP(3.9852, -90)
        c1 = z1 + PP(1.32898, 91)
        c2 = z1 + PP(0.563734, -87)
        z2 = z1 + PP(0.832375, -138)
        c3 = z2 + PP(0.41859, -27)
        c4 = z2 + PP(0.687482, 152)
        #z3 = z2 + PP(1.4534, 83)
        z3 = z4 - PP(0.996105, ta + 27)
        c5 = z3 + PP(0.61651, -152)
        #c6 = z3 + PP(0.296818, 27)
        #z4 = z3 + PP(0.996105, -62)
        #c7 = z4 + PP(0.438007, 91)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRswr(cls, ta=None, **kwargs):
        #M 85.9859,409.713 C 85.854,413.491 85.854,417.273 85.9859,421.051 86.0419,422.655 84.378674,423.52592 83.4347,422.635 82.597574,421.84492 83.83636,420.00018 84.562872,419.30205 85.289385,418.60393 85.945137,419.72914 85.9859,421.051

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32782)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.98485)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.564875, -4.85469)
        #z2 = P(-0.896644, -4.54156)
        #c4 = P(-1.19086, -4.26388)
        #c5 = P(-0.755477, -3.61553)
        #z3 = P(-0.500137, -3.37017)
        #c6 = P(-0.244797, -3.12481)
        #c7 = P(-0.0143266, -3.52027)
        z4 = P(0, -3.98485)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32782)
        #z1 = z0 + P(0, -3.98485)
        #c1 = z1 + P(-0.0463576, 1.32782)
        #c2 = z1 + P(0.0196818, -0.563742)
        #z2 = z1 + P(-0.896644, -0.556712)
        #c3 = z2 + P(0.331769, -0.313123)
        #c4 = z2 + P(-0.294216, 0.277681)
        #z3 = z2 + P(0.396507, 1.1714)
        #c5 = z3 + P(-0.25534, -0.245365)
        #c6 = z3 + P(0.25534, 0.245361)
        #z4 = z3 + P(0.500137, -0.614686)
        #c7 = z4 + P(-0.0143266, 0.464581)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32862, -91)
        z1 = z0 + PP(3.98485, -90)
        c1 = z1 + PP(1.32862, 91)
        c2 = z1 + PP(0.564085, -88)
        z2 = z1 + PP(1.05541, -148)
        c3 = z2 + PP(0.456198, -43)
        c4 = z2 + PP(0.404562, 136)
        #z3 = z2 + PP(1.23669, 71)
        z3 = z4 - PP(0.792449, ta + 39)
        c5 = z3 + PP(0.354122, -136)
        #c6 = z3 + PP(0.35412, 43)
        #z4 = z3 + PP(0.792449, -50)
        #c7 = z4 + PP(0.464802, 91)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRswl(cls, ta=None, **kwargs):
        #M 118.608,409.713 C 118.476,413.491 118.476,417.273 118.608,421.051 118.664,422.655 117.0113,423.51389 116.057,422.635 114.79873,421.47615 115.91999,419.95822 116.76362,419.40733 117.93326,418.64355 119.28489,420.63168 117.55652,421.74385

        #z0 = P(0, -0)
        #c0 = P(-0.0463927, -1.32782)
        #c1 = P(-0.0463927, -2.65704)
        #z1 = P(0, -3.98485)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.561176, -4.85046)
        #z2 = P(-0.896574, -4.54156)
        #c4 = P(-1.33881, -4.13428)
        #c5 = P(-0.944728, -3.60078)
        #z3 = P(-0.648226, -3.40717)
        #c6 = P(-0.237144, -3.13873)
        #c7 = P(0.2379, -3.83748)
        z4 = P(-0.369553, -4.22836)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463927, -1.32782)
        #z1 = z0 + P(0, -3.98485)
        #c1 = z1 + P(-0.0463927, 1.32782)
        #c2 = z1 + P(0.0196818, -0.563742)
        #z2 = z1 + P(-0.896574, -0.556712)
        #c3 = z2 + P(0.335398, -0.308895)
        #c4 = z2 + P(-0.442231, 0.407289)
        #z3 = z2 + P(0.248349, 1.1344)
        #c5 = z3 + P(-0.296502, -0.193616)
        #c6 = z3 + P(0.411082, 0.268438)
        #z4 = z3 + P(0.278673, -0.821193)
        #c7 = z4 + P(0.607453, 0.390883)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32863, -92)
        z1 = z0 + PP(3.98485, -90)
        c1 = z1 + PP(1.32863, 92)
        c2 = z1 + PP(0.564085, -88)
        z2 = z1 + PP(1.05535, -148)
        c3 = z2 + PP(0.455969, -42)
        c4 = z2 + PP(0.60121, 137)
        #z3 = z2 + PP(1.16126, 77)
        z3 = z4 - PP(0.867189, ta + 77)
        c5 = z3 + PP(0.354119, -146)
        #c6 = z3 + PP(0.490965, 33)
        #z4 = z3 + PP(0.867189, -71)
        #c7 = z4 + PP(0.722349, 32)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRsw(cls, ta=None, **kwargs):
        #M 47.3414,409.713 C 47.2095,413.491 47.2095,417.273 47.3414,421.051 47.3974,422.655 45.760494,423.18376 44.81652,422.29284 43.979394,421.50276 44.749153,420.12417 45.549894,419.5126 46.160539,419.04622 47.607727,419.33304 46.96689,421.03343

        #z0 = P(0, -0)
        #c0 = P(-0.0463576, -1.32782)
        #c1 = P(-0.0463576, -2.65704)
        #z1 = P(0, -3.98485)
        #c2 = P(0.0196818, -4.54859)
        #c3 = P(-0.555625, -4.73443)
        #z2 = P(-0.887394, -4.42131)
        #c4 = P(-1.18161, -4.14363)
        #c5 = P(-0.911071, -3.65911)
        #z3 = P(-0.629642, -3.44417)
        #c6 = P(-0.415025, -3.28025)
        #c7 = P(0.0936033, -3.38106)
        z4 = P(-0.131625, -3.97868)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0463576, -1.32782)
        #z1 = z0 + P(0, -3.98485)
        #c1 = z1 + P(-0.0463576, 1.32782)
        #c2 = z1 + P(0.0196818, -0.563742)
        #z2 = z1 + P(-0.887394, -0.436457)
        #c3 = z2 + P(0.331769, -0.313123)
        #c4 = z2 + P(-0.294216, 0.277681)
        #z3 = z2 + P(0.257752, 0.977143)
        #c5 = z3 + P(-0.281428, -0.214942)
        #c6 = z3 + P(0.214617, 0.163914)
        #z4 = z3 + P(0.498017, -0.534511)
        #c7 = z4 + P(0.225228, 0.597619)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32862, -91)
        z1 = z0 + PP(3.98485, -90)
        c1 = z1 + PP(1.32862, 91)
        c2 = z1 + PP(0.564085, -88)
        z2 = z1 + PP(0.98892, -153)
        c3 = z2 + PP(0.456198, -43)
        c4 = z2 + PP(0.404562, 136)
        #z3 = z2 + PP(1.01057, 75)
        z3 = z4 - PP(0.730563, ta + 64)
        c5 = z3 + PP(0.354122, -142)
        #c6 = z3 + PP(0.270052, 37)
        #z4 = z3 + PP(0.730563, -47)
        #c7 = z4 + PP(0.638652, 69)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            #controlcurve(c6, c7),
            curve(),
            endknot(*z4, angle=ta)])

    @classmethod
    def path_SCRNE(cls, ta=None, **kwargs):
        #M 206.74251,122.12747 C 206.67651,125.89347 206.67651,129.65747 206.74251,133.42347 206.79751,135.02147 204.87851,135.69047 203.93251,134.80847 202.58151,133.54847 204.86599,132.22559 206.74251,131.21247 207.97677,130.5461 209.04579,130.08314 209.98003,129.51243

        #z0 = P(0, -0)
        #c0 = P(-0.0232833, -1.32856)
        #c1 = P(-0.0232833, -2.65642)
        #z1 = P(0, -3.98498)
        #c2 = P(0.0194028, -4.54872)
        #c3 = P(-0.657578, -4.78473)
        #z2 = P(-0.991306, -4.47357)
        #c4 = P(-1.46791, -4.02908)
        #c5 = P(-0.661995, -3.56239)
        #z3 = P(0, -3.20499)
        #c6 = P(0.435419, -2.96991)
        #c7 = P(0.812546, -2.80658)
        z4 = P(1.14213, -2.60525)

        #z0 = P(0, -0)
        #c0 = z0 + P(-0.0232833, -1.32856)
        #z1 = z0 + P(0, -3.98498)
        #c1 = z1 + P(-0.0232833, 1.32856)
        #c2 = z1 + P(0.0194028, -0.563739)
        #z2 = z1 + P(-0.991306, -0.488597)
        #c3 = z2 + P(0.333728, -0.31115)
        #c4 = z2 + P(-0.476603, 0.4445)
        #z3 = z2 + P(0.991306, 1.26859)
        #c5 = z3 + P(-0.661995, -0.357406)
        #c6 = z3 + P(0.435419, 0.235081)
        #z4 = z3 + P(1.14213, 0.599736)
        #c7 = z4 + P(-0.329579, -0.201334)

        z0 = P(0, -0)
        c0 = z0 + PP(1.32877, -91)
        z1 = z0 + PP(3.98498, -90)
        c1 = z1 + PP(1.32877, 91)
        c2 = z1 + PP(0.564073, -88)
        z2 = z1 + PP(1.10518, -153)
        c3 = z2 + PP(0.456277, -42)
        c4 = z2 + PP(0.651713, 136)
        z3 = z2 + PP(1.60997, 51)
        #z3 = z4 - PP(1.29001, ta)
        c5 = z3 + PP(0.752314, -151)
        c6 = z3 + PP(0.494826, 28)
        z4 = z3 + PP(1.29001, 27)
        c7 = z4 + PP(0.386209, -148)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            #curve(),
            endknot(*z4)])

class CharTsun(CharTsu):
    def __init__(self, name='tsun', kana='つん',
                 model='S4CR1NE1F', head_type='S',
                 tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        return [self.path_SCRNE()]

class CharTsuku(CharTsu):
    def __init__(self, name='tsu', kana='つ',
                 model='BS4CR1', head_type='BS',
                 tail_type='SCR1'):
        super().__init__(name, kana, model, head_type, tail_type)
