import math
from ..waseda.char import WasedaChar
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

class CharSu(WasedaChar):
    def __init__(self, name='su', kana='す',
                 model='NEL8CL4|SWR8CR4', head_type='NEL|SWR',
                 tail_type='NELCL4|SWRCR4'):
        super().__init__(name, kana, model, head_type, tail_type)

    def to_reverse(self):
        reverse = getattr(self.before, 'tail_type', '') in {
            'ER', 'ERCL1', 'ERCL4', 'E', 'ECL1', 'ECL4', 'ELCL4', 
            'NER', 'NE', 'NECL1', 'NECL4', 'NECL4', 'NELCL4'}
        reverse = reverse and getattr(self.before, 'model', '') not in {'ER4' , 'SR8SWR4'}

        return reverse

    def get_paths(self):
        if self.to_reverse():
            self.model = 'SWR8CR4'
            self.head_type = 'SWR'
            self.tail_type = 'SWRCR4'
            self.head_ligature = {'ER', 'NER'}
            self.tail_ligature = {'ER', 'EL', 'E', 'NER', 'NE', 'NEL',
                'SW', 'S', 'SL', 'SR', 'SE', 'SER', 'SEL', 'SWR', 'SWL'}
        else:
            self.model = 'NEL8CL4'
            self.head_type = 'NEL'
            self.tail_type = 'NEL8CL4'
            self.head_ligature = {'SEL', 'SL', 'SWL'}
            self.tail_ligature = {'ER', 'E', 'EL', 'NE', 'NER', 'NEL',
                'SW', 'SWL', 'S', 'SL', 'SER', 'SEL'}

        return super(WasedaChar, self).get_paths()

    def _get_paths(self):
        if self.before:
            reverse = self.to_reverse()
            reverse = reverse and self.before.model != 'ER4' 
            reverse = reverse and self.before.model != 'ER8SWR4'
        else:
            reverse = False

        if reverse:
            if self.tail_type.endswith('NEF'):
                self.head_type = 'SWR'
                self.tail_type = 'NEF'
                return [self.path_SWRCRNE()]

            self.head_type = 'SWR'
            self.tail_type = 'SWRCR1'

            bt = getattr(self.before, 'tail_type', '')
            ah = getattr(self.after, 'head_type', '')

            me = 'SWRCR'
    
            #bt = bt.lower() if bt in {'ER', 'NER'} else ''
            bt = bt.lower() if bt in {'NER'} else ''
            ah = ah.lower() if ah in {
                'ER', 'EL', 'E', 'NER', 'NE', 'NEL', 
                'SW', 'S', 'SL', 'SR', 'SE', 'SER', 'SEL', 'SWR', 'SWL'} else ''

            ta = getattr(self.after, 'head_angle', 0)

            path_func = getattr(self, "path_" + bt + me + ah)
            
            try:
                path_func = getattr(self, 'path_' + bt + me + ah)
                path = path_func(ta)
                if path is None:
                    raise Exception('path_func did not return a path')
                return [path]
            except:
                self.color = pyx.color.rgb.red
                return [self.path_SWRCR()]
        else:
            if self.tail_type.endswith('NEF'):
                self.head_type = 'NEL'
                self.tail_type = 'NEF'
                if getattr(self.before, 'tail_type', '') == 'SEL':
                    return [self.path_selNELCLNE()]
                else:
                    return [self.path_NELCLNE()]


            self.head_type = 'NEL'
            self.tail_type = 'NEL8CL1'

            bt = getattr(self.before, 'tail_type', '')
            ah = getattr(self.after, 'head_type', '')

            me = 'NELCL'

            bt = bt.lower() if bt in {'SWL', 'SL', 'SEL'} else ''
            ah = ah.lower() if ah in {
                'ER', 'E', 'EL', 'NE', 'NER', 'NEL',
                'SW', 'SWL', 'S', 'SL', 'SER', 'SEL', 'SR', 'SE', 'SWR'} else ''

            ta = getattr(self.after, 'head_angle', 0)

            try:
                path_func = getattr(self, 'path_' + bt + me + ah)
                path = path_func(ta)
                if path is None:
                    raise Exception('path_func did not return a path')
                return [path]
            except:
                self.color = pyx.color.rgb.red
                return [self.path_NELCL()]

    @classmethod
    def path_NELCL(cls, ta=-60, **kwargs):
        #M0.000000 19.000000C5.715820 15.699982,16.009872 11.109207,16.009872 4.584778C16.009872 -1.582764,8.956314 -0.503296,9.535477 2.781189C10.036255 5.621170,11.275757 8.279282,13.129425 10.488388
        #
        #z0 = P(0, -0)
        #c0 = P(2.00888, 1.15982)
        #c1 = P(5.62683, 2.7733)
        #z1 = P(5.62683, 5.06637)
        #c2 = P(5.62683, 7.23402)
        #c3 = P(3.14779, 6.85463)
        #z2 = P(3.35134, 5.70026)
        #c4 = P(3.52734, 4.70212)
        #c5 = P(3.96298, 3.7679)
        z3 = P(4.61447, 2.99149)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.00888, 1.15982)
        #z1 = z0 + P(5.62683, 5.06637)
        #c1 = z1 + P(0, -2.29308)
        #c2 = z1 + P(0, 2.16764)
        #z2 = z1 + P(-2.27549, 0.633889)
        #c3 = z2 + P(-0.203553, 1.15436)
        #c4 = z2 + P(0.176003, -0.998139)
        #z3 = z2 + P(1.26313, -2.70877)
        #c5 = z3 + P(-0.65149, 0.776412)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31965, 29)
        z1 = z0 + PP(7.57161, 41)
        c1 = z1 + PP(2.29308, -90)
        c2 = z1 + PP(2.16764, 90)
        z2 = z1 + PP(2.36213, 164)
        #z2 = z3 - PP(2.9888, ta-14)
        c3 = z2 + PP(1.17217, 100)
        c4 = z2 + PP(1.01354, -79)
        #z3 = z2 + PP(2.9888, -64)
        c5 = z3 + PP(1.01354, 130)
        
        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            curve(),
            endknot(*z3)])

    @classmethod
    def path_NELCLse(cls, ta=-60, **kwargs):
        #M 47.3414,253.81 C 53.0924,250.623 63.5396,246.23 63.5396,239.73 63.5396,233.585 55.149016,236.42224 56.360102,238.47848 57.739307,240.82016 59.392508,242.98138 60.4218,245.331
        #
        #z0 = P(0, -0)
        #c0 = P(2.02125, 1.1201)
        #c1 = P(5.69302, 2.66407)
        #z1 = P(5.69302, 4.94856)
        #c2 = P(5.69302, 7.10828)
        #c3 = P(2.74406, 6.1111)
        #z2 = P(3.16971, 5.38841)
        #c4 = P(3.65445, 4.56541)
        #c5 = P(4.23548, 3.80583)
        z3 = P(4.59724, 2.98003)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.02125, 1.1201)
        #z1 = z0 + P(5.69302, 4.94856)
        #c1 = z1 + P(0, -2.28449)
        #c2 = z1 + P(0, 2.15972)
        #z2 = z1 + P(-2.52331, 0.439859)
        #c3 = z2 + P(-0.425648, 0.722686)
        #c4 = z2 + P(0.484735, -0.823007)
        #z3 = z2 + P(1.42752, -2.40839)
        #c5 = z3 + P(-0.361755, 0.825797)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31086, 28)
        z1 = z0 + PP(7.54312, 40)
        c1 = z1 + PP(2.28449, -90)
        c2 = z1 + PP(2.15972, 90)
        #z2 = z1 + PP(2.56136, 170)
        z2 = z3 - PP(2.79967, ta+1)
        c3 = z2 + PP(0.83872, 120)
        #c4 = z2 + PP(0.955148, -59)
        #z3 = z2 + PP(2.79967, -59)
        #c5 = z3 + PP(0.901558, 113)
        
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
    def path_NELCLser(cls, ta=-60, **kwargs):
        #M 94.4404,253.81 C 100.191,250.623 110.639,246.229 110.639,239.729 110.639,236.75 95.631786,243.37827 99.339163,244.6638 101.25656,245.32866 104.25883,247.07332 105.14583,247.69432
        #
        #z0 = P(0, -0)
        #c0 = P(2.02111, 1.1201)
        #c1 = P(5.69316, 2.66442)
        #z1 = P(5.69316, 4.94891)
        #c2 = P(5.69316, 5.99591)
        #c3 = P(0.418724, 3.66633)
        #z2 = P(1.72172, 3.21452)
        #c4 = P(2.39561, 2.98085)
        #c5 = P(3.45078, 2.36767)
        z3 = P(3.76253, 2.14942)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.02111, 1.1201)
        #z1 = z0 + P(5.69316, 4.94891)
        #c1 = z1 + P(0, -2.28449)
        #c2 = z1 + P(0, 1.047)
        #z2 = z1 + P(-3.97144, -1.73438)
        #c3 = z2 + P(-1.30299, 0.451812)
        #c4 = z2 + P(0.673888, -0.233672)
        #z3 = z2 + P(2.04081, -1.06511)
        #c5 = z3 + P(-0.311745, 0.218257)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31073, 28)
        z1 = z0 + PP(7.54346, 40)
        c1 = z1 + PP(2.28449, -90)
        c2 = z1 + PP(1.047, 90)
        #z2 = z1 + PP(4.33364, -156)
        z2 = z3 - PP(2.30203, ta+8)
        c3 = z2 + PP(1.3791, 160)
        #c4 = z2 + PP(0.713251, -19)
        #z3 = z2 + PP(2.30203, -27)
        #c5 = z3 + PP(0.380553, 145)
        
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
    def path_NELCLsel(cls, ta=-90, **kwargs):
        #M 5728.7387,-8.0278348 C 5734.5237,-11.103095 5745.1187,-15.297035 5745.1187,-21.772785 5745.1187,-25.638629 5741.791,-23.735532 5740.8398,-22.634637 5738.9517,-20.449506 5738.5187,-18.094713 5738.5187,-13.505135

        #z0 = P(0, -0)
        #c0 = P(2.04082, 1.08488)
        #c1 = P(5.7785, 2.56441)
        #z1 = P(5.7785, 4.84891)
        #c2 = P(5.7785, 6.2127)
        #c3 = P(4.60456, 5.54133)
        #z2 = P(4.269, 5.15296)
        #c4 = P(3.60292, 4.38209)
        #c5 = P(3.45017, 3.55137)
        z3 = P(3.45017, 1.93227)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.04082, 1.08488)
        #z1 = z0 + P(5.7785, 4.84891)
        #c1 = z1 + P(0, -2.2845)
        #c2 = z1 + P(0, 1.36378)
        #z2 = z1 + P(-1.5095, 0.304042)
        #c3 = z2 + P(0.335562, 0.388371)
        #c4 = z2 + P(-0.66608, -0.770866)
        #z3 = z2 + P(-0.818833, -3.22069)
        #c5 = z3 + P(0, 1.6191)

        z0 = P(0, -0)
        c0 = z0 + PP(2.31126, 27)
        z1 = z0 + PP(7.54341, 40)
        c1 = z1 + PP(2.2845, -90)
        c2 = z1 + PP(1.36378, 90)
        #z2 = z1 + PP(1.53982, 168)
        z2 = z3 - PP(3.32315, ta + -14)
        c3 = z2 + PP(0.513258, 49)
        #c4 = z2 + PP(1.01877, -130)
        #z3 = z2 + PP(3.32315, -104)
        #c5 = z3 + PP(1.6191, 90)

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
    def path_elNELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_selNELCLsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_elNELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_swlNELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_slNELCL(cls, ta=None, **kwargs):
        return cls.path_selNELCL()

    @classmethod
    def path_selNELCL(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLer(cls, ta=None, **kwargs):
        
        #M 166.895,106.89 C 172.701,103.803 183.093,99.3092 183.093,92.8092 183.093,88.640168 171.90644,96.503536 173.56974,100.1502 174.47529,102.13556 178.64474,99.629835 179.98674,98.855135
        #
        #z0 = P(0, -0)
        #c0 = P(2.04058, 1.08496)
        #c1 = P(5.69295, 2.66435)
        #z1 = P(5.69295, 4.94884)
        #c2 = P(5.69295, 6.41408)
        #c3 = P(1.76132, 3.65043)
        #z2 = P(2.3459, 2.36877)
        #c4 = P(2.66417, 1.67099)
        #c5 = P(4.12956, 2.55166)
        z3 = P(4.60122, 2.82393)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.04058, 1.08496)
        #z1 = z0 + P(5.69295, 4.94884)
        #c1 = z1 + P(0, -2.28449)
        #c2 = z1 + P(0, 1.46525)
        #z2 = z1 + P(-3.34704, -2.58007)
        #c3 = z2 + P(-0.584583, 1.28166)
        #c4 = z2 + P(0.318264, -0.697774)
        #z3 = z2 + P(2.25532, 0.455163)
        #c5 = z3 + P(-0.471659, -0.272276)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31108, 27)
        z1 = z0 + PP(7.54325, 41)
        c1 = z1 + PP(2.28449, -90)
        c2 = z1 + PP(1.46525, 90)
        #z2 = z1 + PP(4.22604, -142)
        z2 = z3 - PP(2.30079, ta-19)
        c3 = z2 + PP(1.40868, 114)
        #c4 = z2 + PP(0.76693, -65)
        #z3 = z2 + PP(2.30079, 11)
        #c5 = z3 + PP(0.544607, -150)
        
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
    def path_NELCLe(cls, ta=None, **kwargs):
        #M0.000000 19.000000C5.715820 15.699982,16.009872 11.109207,16.009872 4.584778C16.009872 -1.582764,8.956314 -0.503296,9.535477 2.781189C10.036255 5.621170,11.275757 8.279282,13.129425 10.488388
        #
        #z0 = P(0, -0)
        #c0 = P(2.00888, 1.15982)
        #c1 = P(5.62683, 2.7733)
        #z1 = P(5.62683, 5.06637)
        #c2 = P(5.62683, 7.23402)
        #c3 = P(3.14779, 6.85463)
        #z2 = P(3.35134, 5.70026)
        #c4 = P(3.52734, 4.70212)
        #c5 = P(3.96298, 3.7679)
        z3 = P(4.61447, 2.99149)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.00888, 1.15982)
        #z1 = z0 + P(5.62683, 5.06637)
        #c1 = z1 + P(0, -2.29308)
        #c2 = z1 + P(0, 2.16764)
        #z2 = z1 + P(-2.27549, 0.633889)
        #c3 = z2 + P(-0.203553, 1.15436)
        #c4 = z2 + P(0.176003, -0.998139)
        #z3 = z2 + P(1.26313, -2.70877)
        #c5 = z3 + P(-0.65149, 0.776412)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31965, 29)
        z1 = z0 + PP(7.57161, 41)
        c1 = z1 + PP(2.29308, -90)
        c2 = z1 + PP(2.16764, 90)
        #z2 = z1 + PP(2.36213, 164)
        z2 = z3 - PP(2.9888, ta-14)
        c3 = z2 + PP(1.17217, 100)
        c4 = z2 + PP(1.01354, -79)
        #z3 = z2 + PP(2.9888, -64)
        c5 = z3 + PP(1.01354, 130)
        
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
    def path_NELCLel(cls, ta=-30, **kwargs):
        #M 47.3414,106.89 C 53.1251,103.815 63.7211,99.6218 63.7211,93.1461 63.7211,90.065455 59.6112,88.4949 56.4308,90.3311 53.522,92.0104 56.781,95.633 61.2179,97.9921

        #z0 = P(0, -0)
        #c0 = P(2.04036, 1.08479)
        #c1 = P(5.77839, 2.56406)
        #z1 = P(5.77839, 4.84854)
        #c2 = P(5.77839, 5.93533)
        #c3 = P(4.32851, 6.48938)
        #z2 = P(3.20654, 5.84161)
        #c4 = P(2.18038, 5.24919)
        #c5 = P(3.33008, 3.97122)
        z3 = P(4.89532, 3.13898)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.04036, 1.08479)
        #z1 = z0 + P(5.77839, 4.84854)
        #c1 = z1 + P(0, -2.28448)
        #c2 = z1 + P(0, 1.08678)
        #z2 = z1 + P(-2.57186, 0.993069)
        #c3 = z2 + P(1.12197, 0.647771)
        #c4 = z2 + P(-1.02616, -0.59242)
        #z3 = z2 + P(1.68878, -2.70263)
        #c5 = z3 + P(-1.56524, 0.832238)

        z0 = P(0, -0)
        c0 = z0 + PP(2.31081, 27)
        z1 = z0 + PP(7.54309, 39)
        c1 = z1 + PP(2.28448, -90)
        c2 = z1 + PP(1.08678, 90)
        #z2 = z1 + PP(2.75692, 158)
        z2 = z3 - PP(3.18688, ta + -30)
        c3 = z2 + PP(1.29554, 29)
        #c4 = z2 + PP(1.18489, -150)
        #z3 = z2 + PP(3.18688, -58)
        #c5 = z3 + PP(1.77274, 152)

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
    def path_NELCLne(cls, ta=None, **kwargs):
        #M 47.3414,152.193 C 53.0925,149.005 63.7825,144.09605 63.7825,136.81894 63.7825,133.48267 52.72522,140.66612 54.105215,144.55952 54.71457,146.2787 58.467132,145.30043 59.577032,144.52343
        #
        #z0 = P(0, -0)
        #c0 = P(2.02128, 1.12045)
        #c1 = P(5.77839, 2.84575)
        #z1 = P(5.77839, 5.40337)
        #c2 = P(5.77839, 6.57593)
        #c3 = P(1.8922, 4.05124)
        #z2 = P(2.37721, 2.68286)
        #c4 = P(2.59137, 2.07864)
        #c5 = P(3.91025, 2.42246)
        z3 = P(4.30033, 2.69555)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.02128, 1.12045)
        #z1 = z0 + P(5.77839, 5.40337)
        #c1 = z1 + P(0, -2.55761)
        #c2 = z1 + P(0, 1.17257)
        #z2 = z1 + P(-3.40118, -2.7205)
        #c3 = z2 + P(-0.485013, 1.36837)
        #c4 = z2 + P(0.214164, -0.604223)
        #z3 = z2 + P(1.92312, 0.0126842)
        #c5 = z3 + P(-0.390085, -0.273084)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31106, 29)
        z1 = z0 + PP(7.91114, 43)
        c1 = z1 + PP(2.55761, -90)
        c2 = z1 + PP(1.17257, 90)
        #z2 = z1 + PP(4.35536, -141)
        z2 = z3 - PP(1.92317, 0)
        c3 = z2 + PP(1.45179, 109)
        #c4 = z2 + PP(0.641055, -70)
        #z3 = z2 + PP(1.92317, 0)
        #c5 = z3 + PP(0.476174, -145)
        
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
    def path_NELCLnel(cls, ta=None, **kwargs):
        #M 192.151,115.033 C 197.935,111.958 207.51481,107.68477 208.531,101.289 209.2806,96.571141 200.34538,103.87293 201.10414,106.8766 201.4337,108.18121 203.64649,108.35139 205.09549,107.48039

        #z0 = P(0, -0)
        #c0 = P(2.04047, 1.08479)
        #c1 = P(5.42001, 2.59229)
        #z1 = P(5.7785, 4.84858)
        #c2 = P(6.04294, 6.51293)
        #c3 = P(2.8908, 3.93702)
        #z2 = P(3.15847, 2.8774)
        #c4 = P(3.27473, 2.41716)
        #c5 = P(4.05535, 2.35712)
        z3 = P(4.56653, 2.66439)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.04047, 1.08479)
        #z1 = z0 + P(5.7785, 4.84858)
        #c1 = z1 + P(-0.358489, -2.25629)
        #c2 = z1 + P(0.264442, 1.66436)
        #z2 = z1 + P(-2.62003, -1.97118)
        #c3 = z2 + P(-0.267674, 1.05963)
        #c4 = z2 + P(0.116261, -0.460237)
        #z3 = z2 + P(1.40806, -0.213004)
        #c5 = z3 + P(-0.511175, -0.307269)

        z0 = P(0, -0)
        c0 = z0 + PP(2.3109, 27)
        z1 = z0 + PP(7.54319, 39)
        c1 = z1 + PP(2.28459, -99)
        c2 = z1 + PP(1.68523, 80)
        #z2 = z1 + PP(3.27874, -143)
        z2 = z3 - PP(1.42408, ta + 320)
        c3 = z2 + PP(1.09291, 104)
        #c4 = z2 + PP(0.474695, -75)
        #z3 = z2 + PP(1.42408, -8)
        #c5 = z3 + PP(0.596418, -148)

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
    def path_NELCLner(cls, ta=None, **kwargs):
        #M 153.186,152.193 C 158.992,149.106 169.627,144.897 169.627,138.397 169.627,136.907 165.25036,138.0785 163.66673,139.31676 161.84025,140.74491 159.2115,144.23222 160.9794,145.73227 163.33666,147.73238 168.292,142.3 168.836,140.804
        #
        #z0 = P(0, -0)
        #c0 = P(2.04058, 1.08496)
        #c1 = P(5.77835, 2.56425)
        #z1 = P(5.77835, 4.84874)
        #c2 = P(5.77835, 5.37242)
        #c3 = P(4.24014, 4.96068)
        #z2 = P(3.68356, 4.52548)
        #c4 = P(3.04162, 4.02354)
        #c5 = P(2.11772, 2.79789)
        #z3 = P(2.73907, 2.27069)
        #c6 = P(3.56755, 1.56773)
        #c7 = P(5.30915, 3.47699)
        z4 = P(5.50035, 4.00278)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.04058, 1.08496)
        #z1 = z0 + P(5.77835, 4.84874)
        #c1 = z1 + P(0, -2.28449)
        #c2 = z1 + P(0, 0.523675)
        #z2 = z1 + P(-2.0948, -0.323259)
        #c3 = z2 + P(0.556582, 0.435199)
        #c4 = z2 + P(-0.641934, -0.501937)
        #z3 = z2 + P(-0.944489, -2.25479)
        #c5 = z3 + P(-0.621346, 0.527207)
        #c6 = z3 + P(0.828482, -0.702958)
        #z4 = z3 + P(2.76128, 1.73209)
        #c7 = z4 + P(-0.191194, -0.525784)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31108, 27)
        z1 = z0 + PP(7.54318, 40)
        c1 = z1 + PP(2.28449, -90)
        c2 = z1 + PP(0.523675, 90)
        z2 = z1 + PP(2.11959, -171)
        c3 = z2 + PP(0.706528, 38)
        c4 = z2 + PP(0.814875, -141)
        #z3 = z2 + PP(2.44462, -112)
        z3 = z4 - PP(3.25957, 32)
        c5 = z3 + PP(0.814873, 139)
        #c6 = z3 + PP(1.08652, -40)
        #z4 = z3 + PP(3.25957, 32)
        #c7 = z4 + PP(0.559468, -109)
        
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
    def path_NELCLsw(cls, ta=None, **kwargs):
        #M 369.13767,89.985786 C 374.86717,86.809736 385.51767,82.717836 385.51767,76.241136 385.51767,73.272236 382.31914,72.159799 381.43511,74.638037 380.58463,77.022221 378.85173,82.467075 377.90645,85.331695

        #z0 = P(0, -0)
        #c0 = P(2.02124, 1.12044)
        #c1 = P(5.7785, 2.56397)
        #z1 = P(5.7785, 4.84881)
        #c2 = P(5.7785, 5.89617)
        #c3 = P(4.65013, 6.28861)
        #z2 = P(4.33826, 5.41434)
        #c4 = P(4.03823, 4.57326)
        #c5 = P(3.4269, 2.65243)
        z3 = P(3.09343, 1.64186)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.02124, 1.12044)
        #z1 = z0 + P(5.7785, 4.84881)
        #c1 = z1 + P(0, -2.28484)
        #c2 = z1 + P(0, 1.04736)
        #z2 = z1 + P(-1.44024, 0.565538)
        #c3 = z2 + P(0.311866, 0.874267)
        #c4 = z2 + P(-0.30003, -0.841087)
        #z3 = z2 + P(-1.24483, -3.77248)
        #c5 = z3 + P(0.333474, 1.01057)

        z0 = P(0, -0)
        c0 = z0 + PP(2.31102, 29)
        z1 = z0 + PP(7.54334, 40)
        c1 = z1 + PP(2.28484, -90)
        c2 = z1 + PP(1.04736, 90)
        #z2 = z1 + PP(1.54729, 158)
        z2 = z3 - PP(3.97256, ta + 1)
        c3 = z2 + PP(0.928226, ta + 180)
        #c4 = z2 + PP(0.892998, -109)
        #z3 = z2 + PP(3.97256, -108)
        #c5 = z3 + PP(1.06417, 71)

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
    def path_NELCLswr(cls, ta=None, **kwargs):
        #M 98.1273,317.713 C 103.878,314.525 114.326,310.132 114.326,303.632 114.326,297.488 103.44343,301.79334 105.37311,304.15124 107.08172,306.239 108.87448,308.80247 109.43521,311.15138
        #
        #z0 = P(0, -0)
        #c0 = P(2.02114, 1.12045)
        #c1 = P(5.69319, 2.66442)
        #z1 = P(5.69319, 4.94891)
        #c2 = P(5.69319, 7.10828)
        #c3 = P(1.86841, 5.59512)
        #z2 = P(2.54661, 4.76641)
        #c4 = P(3.14712, 4.03265)
        #c5 = P(3.7772, 3.13169)
        z3 = P(3.97428, 2.30615)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.02114, 1.12045)
        #z1 = z0 + P(5.69319, 4.94891)
        #c1 = z1 + P(0, -2.28449)
        #c2 = z1 + P(0, 2.15937)
        #z2 = z1 + P(-3.14658, -0.182492)
        #c3 = z2 + P(-0.678205, 0.828707)
        #c4 = z2 + P(0.600508, -0.733764)
        #z3 = z2 + P(1.42767, -2.46027)
        #c5 = z3 + P(-0.197074, 0.825548)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31094, 29)
        z1 = z0 + PP(7.54348, 40)
        c1 = z1 + PP(2.28449, -90)
        c2 = z1 + PP(2.15937, 90)
        #z2 = z1 + PP(3.15187, -176)
        z2 = z3 - PP(2.84449, ta+8)
        c3 = z2 + PP(1.07085, 129)
        #c4 = z2 + PP(0.948166, -50)
        #z3 = z2 + PP(2.84449, -59)
        #c5 = z3 + PP(0.848744, 103)
        
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
    def path_NELCLswl(cls, ta=None, **kwargs):
        #M 2123.7539,1.7098657 C 2130.1439,1.1509857 2141.283,-9.7652432 2141.283,-11.832688 2141.283,-13.748966 2139.532,-12.842915 2137.6961,-10.22143 2135.8602,-7.5999447 2133.8635,-4.3271196 2133.22,-3.1819987

        #z0 = P(0, -0)
        #c0 = P(2.25425, 0.19716)
        #c1 = P(6.18388, 4.04816)
        #z1 = P(6.18388, 4.77751)
        #c2 = P(6.18388, 5.45353)
        #c3 = P(5.56616, 5.1339)
        #z2 = P(4.9185, 4.2091)
        #c4 = P(4.27083, 3.28429)
        #c5 = P(3.56644, 2.12971)
        z3 = P(3.33943, 1.72574)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.25425, 0.19716)
        #z1 = z0 + P(6.18388, 4.77751)
        #c1 = z1 + P(0, -0.729349)
        #c2 = z1 + P(0, 0.67602)
        #z2 = z1 + P(-1.26538, -0.568416)
        #c3 = z2 + P(0.647665, 0.924802)
        #c4 = z2 + P(-0.647665, -0.924802)
        #z3 = z2 + P(-1.57907, -2.48335)
        #c5 = z3 + P(0.227013, 0.403973)

        z0 = P(0, -0)
        c0 = z0 + PP(2.26286, 4)
        z1 = z0 + PP(7.81441, 37)
        c1 = z1 + PP(0.729349, -90)
        c2 = z1 + PP(0.67602, 90)
        #z2 = z1 + PP(1.38718, -155)
        z2 = z3 - PP(2.94287, ta + -2)
        c3 = z2 + PP(1.12904, 54)
        #c4 = z2 + PP(1.12904, -125)
        #z3 = z2 + PP(2.94287, -122)
        #c5 = z3 + PP(0.463389, 60)

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
    def path_NELCLs(cls, ta=None, **kwargs):
        #M 47.3414,182.92 C 53.0925,179.732 63.5398,175.34 63.5398,168.839 63.5398,165.859 57.612119,163.28443 57.630161,167.8 57.638423,169.86792 57.552639,175.95676 57.552639,177.15276
        #
        #z0 = P(0, -0)
        #c0 = P(2.02128, 1.12045)
        #c1 = P(5.69309, 2.66407)
        #z1 = P(5.69309, 4.94891)
        #c2 = P(5.69309, 5.99626)
        #c3 = P(3.60975, 6.90112)
        #z2 = P(3.61609, 5.31407)
        #c4 = P(3.61899, 4.58728)
        #c5 = P(3.58884, 2.4473)
        z3 = P(3.58884, 2.02695)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.02128, 1.12045)
        #z1 = z0 + P(5.69309, 4.94891)
        #c1 = z1 + P(0, -2.28484)
        #c2 = z1 + P(0, 1.04735)
        #z2 = z1 + P(-2.077, 0.365167)
        #c3 = z2 + P(-0.00634104, 1.58704)
        #c4 = z2 + P(0.00290376, -0.726791)
        #z3 = z2 + P(-0.0272459, -3.28712)
        #c5 = z3 + P(0, 0.420346)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31106, 29)
        z1 = z0 + PP(7.5434, 40)
        c1 = z1 + PP(2.28484, -90)
        c2 = z1 + PP(1.04735, 90)
        #z2 = z1 + PP(2.10886, 170)
        z2 = z3 - PP(3.28723, ta)
        c3 = z2 + PP(1.58705, 90)
        #c4 = z2 + PP(0.726797, -89)
        #z3 = z2 + PP(3.28723, -90)
        #c5 = z3 + PP(0.420346, 90)
        
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
    def path_NELCLsr(cls, ta=None, **kwargs):
        #M 161.229,182.92 C 166.98,179.732 177.427,175.339 177.427,168.839 177.427,162.695 165.94648,168.44637 167.72137,169.81778 169.55492,171.23451 171.27404,173.65189 172.67418,176.07482
        #
        #z0 = P(0, -0)
        #c0 = P(2.02125, 1.12045)
        #c1 = P(5.69295, 2.66442)
        #z1 = P(5.69295, 4.94891)
        #c2 = P(5.69295, 7.10828)
        #c3 = P(1.658, 5.0869)
        #z2 = P(2.28181, 4.6049)
        #c4 = P(2.92623, 4.10698)
        #c5 = P(3.53043, 3.25737)
        z3 = P(4.02252, 2.40581)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.02125, 1.12045)
        #z1 = z0 + P(5.69295, 4.94891)
        #c1 = z1 + P(0, -2.28449)
        #c2 = z1 + P(0, 2.15937)
        #z2 = z1 + P(-3.41114, -0.344002)
        #c3 = z2 + P(-0.623803, 0.481996)
        #c4 = z2 + P(0.644419, -0.497924)
        #z3 = z2 + P(1.74071, -2.1991)
        #c5 = z3 + P(-0.492093, 0.851563)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31103, 29)
        z1 = z0 + PP(7.5433, 41)
        c1 = z1 + PP(2.28449, -90)
        c2 = z1 + PP(2.15937, 90)
        #z2 = z1 + PP(3.42844, -174)
        z2 = z3 - PP(2.80466, ta+9)
        c3 = z2 + PP(0.788321, 142)
        #c4 = z2 + PP(0.814374, -37)
        #z3 = z2 + PP(2.80466, -51)
        #c5 = z3 + PP(0.983522, 120)
        
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
    def path_NELCLsl(cls, ta=None, **kwargs):
        #M 104.539,182.92 C 110.29,179.733 120.57705,176.18864 120.81131,168.98762 120.87,167.18343 118.51771,169.98341 116.85883,172.29402 115.19995,174.60463 113.88081,177.51772 113.44731,178.26922
        #
        #z0 = P(0, -0)
        #c0 = P(2.02125, 1.1201)
        #c1 = P(5.63673, 2.3658)
        #z1 = P(5.71906, 4.89667)
        #c2 = P(5.73969, 5.53077)
        #c3 = P(4.91296, 4.54669)
        #z2 = P(4.32993, 3.73461)
        #c4 = P(3.7469, 2.92252)
        #c5 = P(3.28327, 1.89868)
        z3 = P(3.13091, 1.63456)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(2.02125, 1.1201)
        #z1 = z0 + P(5.71906, 4.89667)
        #c1 = z1 + P(-0.082333, -2.53087)
        #c2 = z1 + P(0.0206272, 0.6341)
        #z2 = z1 + P(-1.38914, -1.16207)
        #c3 = z2 + P(0.58303, 0.812087)
        #c4 = z2 + P(-0.58303, -0.812087)
        #z3 = z2 + P(-1.19901, -2.10004)
        #c5 = z3 + P(0.152358, 0.264122)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.31086, 28)
        z1 = z0 + PP(7.52895, 40)
        c1 = z1 + PP(2.53221, -91)
        c2 = z1 + PP(0.634436, 88)
        #z2 = z1 + PP(1.81111, -140)
        z2 = z3 - PP(2.41822, -119)
        c3 = z2 + PP(0.999704, 54)
        #c4 = z2 + PP(0.999704, -125)
        #z3 = z2 + PP(2.41822, -119)
        #c5 = z3 + PP(0.304915, 60)
        
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
    def path_erSWRCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCRswl(cls, ta=None, **kwargs):
        #M 17522.9,-0.377099 C 17527,5.08204 17521.003,21.096728 17516.9,19.4613 17514.881,18.656589 17515.185,16.883752 17515.442,15.500856 17515.818,13.48732 17518.013,11.0277 17519.5,10.88645 17520.896,10.753799 17522.648,14.253061 17520.426,17.393653

        #z0 = P(0, -0)
        #c0 = P(1.44639, -1.92586)
        #c1 = P(-0.669219, -7.57549)
        #z1 = P(-2.11667, -6.99855)
        #c2 = P(-2.82893, -6.71466)
        #c3 = P(-2.72168, -6.08924)
        #z2 = P(-2.63102, -5.60139)
        #c4 = P(-2.49837, -4.89106)
        #c5 = P(-1.72403, -4.02336)
        #z3 = P(-1.19944, -3.97353)
        #c6 = P(-0.706967, -3.92673)
        #c7 = P(-0.0889, -5.1612)
        z4 = P(-0.872772, -6.26913)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.44639, -1.92586)
        #z1 = z0 + P(-2.11667, -6.99855)
        #c1 = z1 + P(1.44745, -0.576943)
        #c2 = z1 + P(-0.712258, 0.283884)
        #z2 = z1 + P(-0.51435, 1.39716)
        #c3 = z2 + P(-0.0906639, -0.487855)
        #c4 = z2 + P(0.132644, 0.710331)
        #z3 = z2 + P(1.43157, 1.62786)
        #c5 = z3 + P(-0.524581, -0.0498299)
        #c6 = z3 + P(0.492478, 0.0467963)
        #z4 = z3 + P(0.326672, -2.2956)
        #c7 = z4 + P(0.783872, 1.10793)

        z0 = P(0, -0)
        c0 = z0 + PP(2.40852, -53)
        z1 = z0 + PP(7.31163, -106)
        c1 = z1 + PP(1.55819, -21)
        c2 = z1 + PP(0.766748, 158)
        z2 = z1 + PP(1.48883, 110)
        c3 = z2 + PP(0.496208, -100)
        c4 = z2 + PP(0.722609, 79)
        z3 = z2 + PP(2.16779, 48)
        #z3 = z4 - PP(2.31872, ta + 45)
        c5 = z3 + PP(0.526942, -174)
        #c6 = z3 + PP(0.494696, 5)
        #z4 = z3 + PP(2.31872, -81)
        #c7 = z4 + PP(1.35719, 54)

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
    def path_nerSWRCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_nerSWRCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_erSWRCR(cls, ta=None, **kwargs):
        #M 305.75,267.491 C 310.45,273.08526 300.87346,286.44479 293.80546,284.68279 286.73746,282.92079 296.11083,280.17961 302.79983,280.17961

        #z0 = P(0, -0)
        #c0 = P(1.65806, -1.97353)
        #c1 = P(-1.72033, -6.68648)
        #z1 = P(-4.21377, -6.06488)
        #c2 = P(-6.7072, -5.44329)
        #c3 = P(-3.40048, -4.47626)
        z2 = P(-1.04075, -4.47626)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.65806, -1.97353)
        #z1 = z0 + P(-4.21377, -6.06488)
        #c1 = z1 + P(2.49343, -0.621594)
        #c2 = z1 + P(-2.49343, 0.621594)
        #z2 = z1 + P(3.17301, 1.58862)
        #c3 = z2 + P(-2.35973, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(2.57759, -49)
        z1 = z0 + PP(7.38503, -124)
        #z1 = z2 - PP(3.54848, ta + 26)
        c1 = z1 + PP(2.56975, -13)
        c2 = z1 + PP(2.56975, 166)
        z2 = z1 + PP(3.54848, 26)
        c3 = z2 + PP(2.35973, 180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])

    @classmethod
    def path_nerSWRCR(cls, ta=None, **kwargs):
        #M 226.962,1050.03 C 230.58718,1053.1692 224.20469,1070.3292 219.86859,1069.7077 217.03536,1069.3016 217.77731,1067.2392 218.92946,1066.2624 220.06394,1065.3006 224.3197,1062.6987 226.07758,1062.1046

        #z0 = P(0, -0)
        #c0 = P(1.27888, -1.10744)
        #c1 = P(-0.972718, -7.16111)
        #z1 = P(-2.5024, -6.94186)
        #c2 = P(-3.5019, -6.79859)
        #c3 = P(-3.24015, -6.07102)
        #z2 = P(-2.8337, -5.72643)
        #c4 = P(-2.43348, -5.38713)
        #c5 = P(-0.932145, -4.46924)
        z3 = P(-0.312004, -4.25965)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.27888, -1.10744)
        #z1 = z0 + P(-2.5024, -6.94186)
        #c1 = z1 + P(1.52968, -0.219251)
        #c2 = z1 + P(-0.999501, 0.143263)
        #z2 = z1 + P(-0.331304, 1.21543)
        #c3 = z2 + P(-0.406453, -0.344593)
        #c4 = z2 + P(0.400219, 0.339302)
        #z3 = z2 + P(2.5217, 1.46678)
        #c5 = z3 + P(-0.620141, -0.209585)

        z0 = P(0, -0)
        c0 = z0 + PP(1.69173, -40)
        z1 = z0 + PP(7.37912, -109)
        c1 = z1 + PP(1.54531, -8)
        c2 = z1 + PP(1.00972, 171)
        z2 = z1 + PP(1.25977, 105)
        #z2 = z3 - PP(2.91726, ta + 371)
        c3 = z2 + PP(0.532868, -139)
        c4 = z2 + PP(0.524691, 40)
        #z3 = z2 + PP(2.91726, 30)
        c5 = z3 + PP(0.6546, -161)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

    @classmethod
    def path_SWRCRer(cls, ta=30, **kwargs):
        #M 189.155,441.355 C 189.155,449.296 185.65706,460.89421 178.97,459.226 175.39015,458.33294 185.76354,452.66771 187.29154,451.78671
        #
        #z0 = P(0, -0)
        #c0 = P(0, -2.79094)
        #c1 = P(-1.22939, -6.86725)
        #z1 = P(-3.57962, -6.28094)
        #c2 = P(-4.83779, -5.96706)
        #c3 = P(-1.19196, -3.97596)
        z2 = P(-0.654931, -3.66633)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.79094)
        #z1 = z0 + P(-3.57962, -6.28094)
        #c1 = z1 + P(2.35023, -0.586309)
        #c2 = z1 + P(-1.25817, 0.313875)
        #z2 = z1 + P(2.92469, 2.61461)
        #c3 = z2 + P(-0.537031, -0.309636)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.79094, -90)
        #z1 = z0 + PP(7.22938, -119)
        z1 = z2 - PP(3.92301, ta+15)
        c1 = z1 + PP(2.42226, -14)
        #c2 = z1 + PP(1.29673, 165)
        #z2 = z1 + PP(3.92301, 41)
        #c3 = z2 + PP(0.6199, -150)
        
        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_SWRCRel(cls, ta=None, **kwargs):
        #M 135.299,441.355 C 135.299,449.326 131.262,461.114 124.346,461.114 121.51877,461.114 123.42936,453.52329 126.17742,452.41299 128.15338,451.61465 131.47074,455.99865 131.47074,455.99865
        #
        #z0 = P(0, -0)
        #c0 = P(0, -2.80149)
        #c1 = P(-1.41884, -6.9445)
        #z1 = P(-3.84954, -6.9445)
        #c2 = P(-4.8432, -6.9445)
        #c3 = P(-4.1717, -4.27667)
        #z2 = P(-3.20587, -3.88644)
        #c4 = P(-2.5114, -3.60586)
        #c5 = P(-1.34548, -5.14666)
        z3 = P(-1.34548, -5.14666)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80149)
        #z1 = z0 + P(-3.84954, -6.9445)
        #c1 = z1 + P(2.4307, 0)
        #c2 = z1 + P(-0.993658, 0)
        #z2 = z1 + P(0.643671, 3.05806)
        #c3 = z2 + P(-0.965833, -0.390226)
        #c4 = z2 + P(0.694471, 0.280584)
        #z3 = z2 + P(1.86039, -1.26022)
        #c5 = z3 + P(0, 0)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.80149, -90)
        z1 = z0 + PP(7.94009, -119)
        c1 = z1 + PP(2.4307, 0)
        c2 = z1 + PP(0.993658, 180)
        #z2 = z1 + PP(3.12506, 78)
        z2 = z3 - PP(2.24704, -34)
        c3 = z2 + PP(1.04169, -157)
        #c4 = z2 + PP(0.749011, 22)
        #z3 = z2 + PP(2.24704, -34)
        #c5 = z3 + PP(0, 0)
        
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
    def path_SWRCRe(cls, ta=None, **kwargs):
        #M 70.0186,441.355 C 70.0186,449.326 65.6392,460.921 58.7223,460.921 54.861134,460.921 54.897139,454.00191 59.942903,453.84218 62.081307,453.77448 66.024954,453.53942 67.273422,453.48919
        #
        #z0 = P(0, -0)
        #c0 = P(0, -2.80149)
        #c1 = P(-1.53918, -6.87666)
        #z1 = P(-3.9702, -6.87666)
        #c2 = P(-5.32724, -6.87666)
        #c3 = P(-5.31459, -4.44488)
        #z2 = P(-3.5412, -4.38874)
        #c4 = P(-2.78964, -4.36495)
        #c5 = P(-1.40361, -4.28233)
        z3 = P(-0.96482, -4.26468)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80149)
        #z1 = z0 + P(-3.9702, -6.87666)
        #c1 = z1 + P(2.43101, 0)
        #c2 = z1 + P(-1.35704, 0)
        #z2 = z1 + P(0.428993, 2.48792)
        #c3 = z2 + P(-1.77338, -0.0561387)
        #c4 = z2 + P(0.751563, 0.0237938)
        #z3 = z2 + P(2.57638, 0.124062)
        #c5 = z3 + P(-0.438786, -0.0176538)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.80149, -90)
        z1 = z0 + PP(7.94046, -119)
        c1 = z1 + PP(2.43101, 0)
        c2 = z1 + PP(1.35704, 180)
        #z2 = z1 + PP(2.52464, 80)
        z2 = z3 - PP(2.57937, ta+2)
        c3 = z2 + PP(1.77427, -178)
        #c4 = z2 + PP(0.75194, 1)
        #z3 = z2 + PP(2.57937, 2)
        #c5 = z3 + PP(0.439141, -177)
        
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
    def path_SWRCRner(cls, ta=None, **kwargs):
        #M 181.335,513.873 C 181.335,521.845 179.29279,533.80589 176.76954,533.58263 174.07935,533.63368 176.17118,530.72965 177.83296,527.78076
        #
        #z0 = P(0, -0)
        #c0 = P(0, -2.80184)
        #c1 = P(-0.717755, -7.00561)
        #z1 = P(-1.60458, -6.92714)
        #c2 = P(-2.55007, -6.94509)
        #c3 = P(-1.81488, -5.92444)
        z2 = P(-1.23083, -4.88802)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80184)
        #z1 = z0 + P(-1.60458, -6.92714)
        #c1 = z1 + P(0.886821, -0.0784669)
        #c2 = z1 + P(-0.945494, -0.017942)
        #z2 = z1 + P(0.373749, 2.03912)
        #c3 = z2 + P(-0.584049, -1.03642)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.80184, -90)
        #z1 = z0 + PP(7.11055, -103)
        z1 = z2 - PP(2.07309, 79)
        c1 = z1 + PP(0.890286, -5)
        #c2 = z1 + PP(0.945664, -178)
        #z2 = z1 + PP(2.07309, 79)
        #c3 = z2 + PP(1.18965, -119)
        
        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            tensioncurve(1.5),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_SWRCRne(cls, ta=None, **kwargs):
        #M 70.0186,513.873 C 70.9913,521.796 67.249807,534.05381 62.8962,533.442 54.924586,532.32175 66.950878,524.67822 69.838578,522.65622

        #z0 = P(0, -0)
        #c0 = P(0.341865, -2.78462)
        #c1 = P(-0.97312, -7.09274)
        #z1 = P(-2.50324, -6.87772)
        #c2 = P(-5.30494, -6.484)
        #c3 = P(-1.07818, -3.7976)
        z2 = P(-0.0632705, -3.08695)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.341865, -2.78462)
        #z1 = z0 + P(-2.50324, -6.87772)
        #c1 = z1 + P(1.53012, -0.215027)
        #c2 = z1 + P(-2.8017, 0.393723)
        #z2 = z1 + P(2.43997, 3.79077)
        #c3 = z2 + P(-1.01491, -0.710652)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80552, -83)
        z1 = z0 + PP(7.3191, -109)
        z1 = z2 - PP(4.50814, 57)
        c1 = z1 + PP(1.54515, -7)
        #c2 = z1 + PP(2.82923, 172)
        #z2 = z1 + PP(4.50814, 57)
        #c3 = z2 + PP(1.23898, -144)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            #controlcurve(c2, c3),
            curve(),
            endknot(*z2, angle=ta)])

    @classmethod
    def path_SWRCRnel(cls, ta=None, **kwargs):
        #M 435.383,211.896 C 435.383,219.838 430.183,231.486 425.829,231.486 423.242,231.486 423.69255,229.19127 424.167,227.992 424.6945,226.65865 426.05967,226.24215 427.61172,225.97499 429.16377,225.70783 430.9027,225.59 432.1777,224.854

        #z0 = P(0, -0)
        #c0 = P(0, -2.80176)
        #c1 = P(-1.83444, -6.91092)
        #z1 = P(-3.37044, -6.91092)
        #c2 = P(-4.28307, -6.91092)
        #c3 = P(-4.12413, -6.10139)
        #z2 = P(-3.95676, -5.67831)
        #c4 = P(-3.77067, -5.20793)
        #c5 = P(-3.28906, -5.061)
        #z3 = P(-2.74153, -4.96675)
        #c6 = P(-2.19401, -4.87251)
        #c7 = P(-1.58055, -4.83094)
        z4 = P(-1.13076, -4.57129)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80176)
        #z1 = z0 + P(-3.37044, -6.91092)
        #c1 = z1 + P(1.53599, 0)
        #c2 = z1 + P(-0.912636, 0)
        #z2 = z1 + P(-0.586317, 1.23261)
        #c3 = z2 + P(-0.167375, -0.423076)
        #c4 = z2 + P(0.18609, 0.470376)
        #z3 = z2 + P(1.21522, 0.711556)
        #c5 = z3 + P(-0.547529, -0.0942481)
        #c6 = z3 + P(0.547529, 0.0942481)
        #z4 = z3 + P(1.61078, 0.39546)
        #c7 = z4 + P(-0.449792, -0.259644)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80176, -90)
        z1 = z0 + PP(7.68899, -115)
        c1 = z1 + PP(1.53599, 0)
        c2 = z1 + PP(0.912636, 180)
        z2 = z1 + PP(1.36495, 115)
        c3 = z2 + PP(0.454981, -111)
        c4 = z2 + PP(0.505849, 68)
        #z3 = z2 + PP(1.40822, 30)
        z3 = z4 - PP(1.65861, ta + 343)
        c5 = z3 + PP(0.555581, -170)
        #c6 = z3 + PP(0.555581, 9)
        #z4 = z3 + PP(1.65861, 13)
        #c7 = z4 + PP(0.519353, -150)

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
    def path_SWRCRsw(cls, ta=None, **kwargs):
        #M 70.0186,764.248 C 70.0186,772.22 65.6392,783.814 58.7223,783.814 54.700578,783.814 59.178503,773.79072 64.498058,776.1283 65.944758,776.8333 64.328105,780.1994 63.61795,781.68656

        #z0 = P(0, -0)
        #c0 = P(0, -2.80184)
        #c1 = P(-1.53918, -6.87666)
        #z1 = P(-3.9702, -6.87666)
        #c2 = P(-5.38367, -6.87666)
        #c3 = P(-3.80986, -3.35388)
        #z2 = P(-1.94025, -4.17545)
        #c4 = P(-1.43179, -4.42323)
        #c5 = P(-1.99998, -5.60628)
        z3 = P(-2.24957, -6.12895)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80184)
        #z1 = z0 + P(-3.9702, -6.87666)
        #c1 = z1 + P(2.43101, 0)
        #c2 = z1 + P(-1.41347, 0)
        #z2 = z1 + P(2.02995, 2.70122)
        #c3 = z2 + P(-1.86961, 0.821566)
        #c4 = z2 + P(0.508457, -0.247779)
        #z3 = z2 + P(-0.309323, -1.95351)
        #c5 = z3 + P(0.249591, 0.522677)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80184, -90)
        z1 = z0 + PP(7.94046, -119)
        c1 = z1 + PP(2.43101, 0)
        c2 = z1 + PP(1.41347, 180)
        #z2 = z1 + PP(3.37894, 53)
        z2 = z3 - PP(1.97784, ta+16)
        c3 = z2 + PP(2.04216, 156)
        #c4 = z2 + PP(0.565617, -25)
        #z3 = z2 + PP(1.97784, -98)
        #c5 = z3 + PP(0.579212, 64)

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
    def path_SWRCRswr(cls, ta=None, **kwargs):
        #M 122.831,764.248 C 122.831,772.22 118.794,784.008 111.878,784.008 109.28,784.008 112.58019,777.2022 115.22737,776.53126 116.67383,776.16464 118.15374,776.21832 118.78249,779.2517

        #z0 = P(0, -0)
        #c0 = P(0, -2.80184)
        #c1 = P(-1.41884, -6.94485)
        #z1 = P(-3.84954, -6.94485)
        #c2 = P(-4.76263, -6.94485)
        #c3 = P(-3.60275, -4.55288)
        #z2 = P(-2.67237, -4.31707)
        #c4 = P(-2.164, -4.18822)
        #c5 = P(-1.64387, -4.20709)
        z3 = P(-1.42289, -5.2732)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80184)
        #z1 = z0 + P(-3.84954, -6.94485)
        #c1 = z1 + P(2.4307, 0)
        #c2 = z1 + P(-0.913093, 0)
        #z2 = z1 + P(1.17717, 2.62777)
        #c3 = z2 + P(-0.930378, -0.235808)
        #c4 = z2 + P(0.508373, 0.128852)
        #z3 = z2 + P(1.24948, -0.956126)
        #c5 = z3 + P(-0.22098, 1.06611)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80184, -90)
        z1 = z0 + PP(7.94039, -118)
        c1 = z1 + PP(2.4307, 0)
        c2 = z1 + PP(0.913093, 180)
        z2 = z1 + PP(2.8794, 65)
        z2 = z3 - PP(1.57333, -37)
        c3 = z2 + PP(0.959796, -165)
        #c4 = z2 + PP(0.524448, 14)
        #z3 = z2 + PP(1.57333, -37)
        #c5 = z3 + PP(1.08877, 101)

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
    def path_SWRCRswl(cls, ta=None, *kwargs):
        #M 169.621,764.248 C 169.621,772.22 165.24053,783.9566 158.325,783.814 154.0534,783.72592 159.36226,774.69094 164.41707,777.3418 165.30004,777.80485 164.74981,779.98042 164.47547,780.33229

        #z0 = P(0, -0)
        #c0 = P(0, -2.80184)
        #c1 = P(-1.53956, -6.92678)
        #z1 = P(-3.97009, -6.87666)
        #c2 = P(-5.47139, -6.84571)
        #c3 = P(-3.60554, -3.67027)
        #z2 = P(-1.82897, -4.60195)
        #c4 = P(-1.51864, -4.76469)
        #c5 = P(-1.71203, -5.52931)
        z3 = P(-1.80845, -5.65298)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80184)
        #z1 = z0 + P(-3.97009, -6.87666)
        #c1 = z1 + P(2.43053, -0.0501182)
        #c2 = z1 + P(-1.5013, 0.0309566)
        #z2 = z1 + P(2.14112, 2.27472)
        #c3 = z2 + P(-1.77656, 0.931671)
        #c4 = z2 + P(0.310329, -0.162743)
        #z3 = z2 + P(0.0205253, -1.05104)
        #c5 = z3 + P(0.0964195, 0.123668)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80184, -90)
        z1 = z0 + PP(7.94041, -119)
        c1 = z1 + PP(2.43105, -1)
        c2 = z1 + PP(1.50162, 178)
        #z2 = z1 + PP(3.1239, 46)
        z2 = z3 - PP(1.05124, -88)
        c3 = z2 + PP(2.00604, 152)
        #c4 = z2 + PP(0.350413, -27)
        #z3 = z2 + PP(1.05124, -88)
        #c5 = z3 + PP(0.156814, 52)

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
    def path_SWRCRse(cls, ta=None, **kwargs):
        #M 70.0186,671.696 C 70.0186,679.667 64.003592,694.7632 58.479492,690.6002 55.248331,688.29082 59.746658,678.398 63.110291,682.53594 64.013577,683.64717 65.241303,685.21841 65.771709,686.44441
        
        #z0 = P(0, -0)
        #c0 = P(0, -2.80149)
        #c1 = P(-2.11403, -8.1072)
        #z1 = P(-4.05553, -6.64407)
        #c2 = P(-5.19116, -5.83241)
        #c3 = P(-3.61018, -2.35548)
        #z2 = P(-2.42799, -3.8098)
        #c4 = P(-2.11052, -4.20036)
        #c5 = P(-1.67903, -4.75258)
        z3 = P(-1.49261, -5.18347)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80149)
        #z1 = z0 + P(-4.05553, -6.64407)
        #c1 = z1 + P(1.9415, -1.46313)
        #c2 = z1 + P(-1.13562, 0.811654)
        #z2 = z1 + P(1.62754, 2.83426)
        #c3 = z2 + P(-1.18218, 1.45432)
        #c4 = z2 + P(0.317469, -0.390553)
        #z3 = z2 + P(0.935382, -1.37367)
        #c5 = z3 + P(-0.186416, 0.43089)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.80149, -90)
        z1 = z0 + PP(7.78402, -121)
        c1 = z1 + PP(2.43108, -37)
        c2 = z1 + PP(1.39586, 144)
        #z2 = z1 + PP(3.26832, 60)
        z2 = z3 - PP(1.6619, ta-1)
        c3 = z2 + PP(1.87419, 129)
        #c4 = z2 + PP(0.503307, -50)
        #z3 = z2 + PP(1.6619, -55)
        #c5 = z3 + PP(0.469486, 113)
        
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
    def path_SWRCRser(cls, ta=None, **kwargs):
        #M 118.355,671.696 C 118.355,679.667 115.02773,690.94674 108.11238,691.04161 103.79763,691.10081 103.98022,684.80671 108.85872,684.63771 110.2649,684.589 113.46489,685.35942 114.62589,686.17242
        
        #z0 = P(0, -0)
        #c0 = P(0, -2.80149)
        #c1 = P(-1.1694, -6.76586)
        #z1 = P(-3.59987, -6.79921)
        #c2 = P(-5.11633, -6.82001)
        #c3 = P(-5.05216, -4.60789)
        #z2 = P(-3.33756, -4.54849)
        #c4 = P(-2.84335, -4.53137)
        #c5 = P(-1.71868, -4.80214)
        z3 = P(-1.31063, -5.08788)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80149)
        #z1 = z0 + P(-3.59987, -6.79921)
        #c1 = z1 + P(2.43047, 0.033343)
        #c2 = z1 + P(-1.51646, -0.0208064)
        #z2 = z1 + P(0.262309, 2.25071)
        #c3 = z2 + P(-1.7146, -0.0593967)
        #c4 = z2 + P(0.494216, 0.0171196)
        #z3 = z2 + P(2.02693, -0.539389)
        #c5 = z3 + P(-0.408045, 0.285737)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.80149, -90)
        z1 = z0 + PP(7.69339, -117)
        c1 = z1 + PP(2.4307, 0)
        c2 = z1 + PP(1.5166, -179)
        #z2 = z1 + PP(2.26595, 83)
        z2 = z3 - PP(2.09747, ta+12)
        c3 = z2 + PP(1.71563, -178)
        #c4 = z2 + PP(0.494512, 1)
        #z3 = z2 + PP(2.09747, -14)
        #c5 = z3 + PP(0.498143, 144)
        
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
    def path_SWRCRsel(cls, ta=None, **kwargs):
        #M 172.211,671.696 C 172.211,679.667 168.17293,691.57756 161.258,691.456 157.89042,691.3968 162.33982,681.39287 167.93129,683.17848 169.15551,683.56943 167.95281,685.53548 167.95281,687.02448

        #z0 = P(0, -0)
        #c0 = P(0, -2.80149)
        #c1 = P(-1.41922, -6.98757)
        #z1 = P(-3.84954, -6.94485)
        #c2 = P(-5.03311, -6.92404)
        #c3 = P(-3.46932, -3.40806)
        #z2 = P(-1.50415, -4.03563)
        #c4 = P(-1.07388, -4.17303)
        #c5 = P(-1.49658, -4.86402)
        z3 = P(-1.49658, -5.38735)

        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80149)
        #z1 = z0 + P(-3.84954, -6.94485)
        #c1 = z1 + P(2.43032, -0.0427235)
        #c2 = z1 + P(-1.18357, 0.0208064)
        #z2 = z1 + P(2.34539, 2.90922)
        #c3 = z2 + P(-1.96518, 0.62757)
        #c4 = z2 + P(0.430264, -0.137403)
        #z3 = z2 + P(0.00756342, -1.35171)
        #c5 = z3 + P(0, 0.523324)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80149, -90)
        z1 = z0 + PP(7.94039, -118)
        c1 = z1 + PP(2.4307, -1)
        c2 = z1 + PP(1.18375, 178)
        #z2 = z1 + PP(3.7369, 51)
        z2 = z3 - PP(1.35174, ta+1)
        c3 = z2 + PP(2.06295, 162)
        #c4 = z2 + PP(0.451671, -17)
        #z3 = z2 + PP(1.35174, -89)
        #c5 = z3 + PP(0.523324, 90)

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
    def path_SWRCRsl(cls, ta=None, **kwargs):
        #M 125.634,573.469 C 125.634,581.411 123.823,593.013 116.933,593.013 114.344,593.013 119.39006,582.64083 122.37886,584.30849 125.16374,585.86236 120.09281,589.09763 118.14163,592.88615
        
        #z0 = P(0, -0)
        #c0 = P(0, -2.79129)
        #c1 = P(-0.636494, -6.86893)
        #z1 = P(-3.05805, -6.86893)
        #c2 = P(-3.96798, -6.86893)
        #c3 = P(-2.19449, -3.22353)
        #z2 = P(-1.14405, -3.80965)
        #c4 = P(-0.165278, -4.35577)
        #c5 = P(-1.94751, -5.49284)
        z3 = P(-2.63327, -6.82435)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.79129)
        #z1 = z0 + P(-3.05805, -6.86893)
        #c1 = z1 + P(2.42156, 0)
        #c2 = z1 + P(-0.90993, 0)
        #z2 = z1 + P(1.914, 3.05929)
        #c3 = z2 + P(-1.05044, 0.586116)
        #c4 = z2 + P(0.978774, -0.546123)
        #z3 = z2 + P(-1.48922, -3.0147)
        #c5 = z3 + P(0.685761, 1.33151)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.79129, -90)
        z1 = z0 + PP(7.5189, -113)
        c1 = z1 + PP(2.42156, 0)
        c2 = z1 + PP(0.90993, 180)
        #z2 = z1 + PP(3.60869, 57)
        z2 = z3 - PP(3.36247, ta-2)
        c3 = z2 + PP(1.2029, 150)
        #c4 = z2 + PP(1.12082, -29)
        #z3 = z2 + PP(3.36247, -116)
        #c5 = z3 + PP(1.49773, 62)
        
        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            #controlcurve(c4, c5),
            tensioncurve(1.5),
            endknot(*z3, angle=ta)])
    
    @classmethod
    def path_SWRCRsr(cls,ta=None, **kwargs):
        #M 182.4,573.469 C 182.4,581.441 178.021,593.035 171.104,593.035 168.505,593.035 170.16999,587.47648 171.38256,585.80795 172.63643,584.08259 175.46303,583.40711 178.53469,587.71196
        
        #z0 = P(0, -0)
        #c0 = P(0, -2.80184)
        #c1 = P(-1.53904, -6.87666)
        #z1 = P(-3.97009, -6.87666)
        #c2 = P(-4.88353, -6.87666)
        #c3 = P(-4.29836, -4.92307)
        #z2 = P(-3.87219, -4.33665)
        #c4 = P(-3.4315, -3.73025)
        #c5 = P(-2.43807, -3.49285)
        z3 = P(-1.3585, -5.00583)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80184)
        #z1 = z0 + P(-3.97009, -6.87666)
        #c1 = z1 + P(2.43105, 0)
        #c2 = z1 + P(-0.913444, 0)
        #z2 = z1 + P(0.0979027, 2.54002)
        #c3 = z2 + P(-0.42617, -0.586421)
        #c4 = z2 + P(0.440685, 0.606395)
        #z3 = z2 + P(2.51369, -0.669183)
        #c5 = z3 + P(-1.07957, 1.51298)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.80184, -90)
        z1 = z0 + PP(7.94041, -119)
        c1 = z1 + PP(2.43105, 0)
        c2 = z1 + PP(0.913444, 180)
        #z2 = z1 + PP(2.5419, 87)
        z2 = z3 - PP(2.60124, -14)
        c3 = z2 + PP(0.724921, -126)
        #c4 = z2 + PP(0.749612, 53)
        #z3 = z2 + PP(2.60124, -14)
        #c5 = z3 + PP(1.85865, 125)
        
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
    def path_SWRCRs(cls, ta=None, **kwargs):
        #M 70.0186,573.469 C 70.0186,581.441 65.6392,593.034 58.7223,593.034 55.328144,593.034 62.039765,581.98261 66.043078,583.0187 67.348527,583.35656 66.546228,585.70467 66.546228,587.03267
        
        #z0 = P(0, -0)
        #c0 = P(0, -2.80184)
        #c1 = P(-1.53918, -6.87631)
        #z1 = P(-3.9702, -6.87631)
        #c2 = P(-5.16311, -6.87631)
        #c3 = P(-2.80424, -2.99219)
        #z2 = P(-1.39724, -3.35634)
        #c4 = P(-0.938424, -3.47508)
        #c5 = P(-1.2204, -4.30035)
        z3 = P(-1.2204, -4.76709)
        
        #z0 = P(0, -0)
        #c0 = z0 + P(0, -2.80184)
        #z1 = z0 + P(-3.9702, -6.87631)
        #c1 = z1 + P(2.43101, 0)
        #c2 = z1 + P(-1.19291, 0)
        #z2 = z1 + P(2.57296, 3.51998)
        #c3 = z2 + P(-1.407, 0.364144)
        #c4 = z2 + P(0.458813, -0.118744)
        #z3 = z2 + P(0.176837, -1.41075)
        #c5 = z3 + P(0, 0.466739)
        
        z0 = P(0, -0)
        c0 = z0 + PP(2.80184, -90)
        z1 = z0 + PP(7.94016, -120)
        c1 = z1 + PP(2.43101, 0)
        c2 = z1 + PP(1.19291, 180)
        #z2 = z1 + PP(4.36009, 53)
        z2 = z3 - PP(1.42179, ta+8)
        c3 = z2 + PP(1.45336, 165)
        #c4 = z2 + PP(0.47393, -14)
        #z3 = z2 + PP(1.42179, -82)
        #c5 = z3 + PP(0.466739, 90)
        
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
    def path_SWRCR(cls, ta=None, **kwargs):
        #M 389.9,143.114 C 390.869,151.008 387.492,163.265 383.145,162.732 375.203,161.615 386.00027,157.32075 388.80527,155.20775

        #z0 = P(0, -0)
        #c0 = P(0.341842, -2.78483)
        #c1 = P(-0.849489, -7.10882)
        #z1 = P(-2.38301, -6.92079)
        #c2 = P(-5.18478, -6.52674)
        #c3 = P(-1.37574, -5.01183)
        z2 = P(-0.386196, -4.26641)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.341842, -2.78483)
        #z1 = z0 + P(-2.38301, -6.92079)
        #c1 = z1 + P(1.53353, -0.188031)
        #c2 = z1 + P(-2.80176, 0.394053)
        #z2 = z1 + P(1.99682, 2.65439)
        #c3 = z2 + P(-0.989542, -0.745419)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80573, -83)
        z1 = z0 + PP(7.31957, -108)
        #z1 = z2 - PP(3.3216, ta + 376)
        c1 = z1 + PP(1.54501, -6)
        c2 = z1 + PP(2.82934, 171)
        z2 = z1 + PP(3.3216, 53)
        c3 = z2 + PP(1.23889, -143)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            #curve(),
            endknot(*z2)])
    
    @classmethod
    def path_selNELCL(cls, ta=None, **kwargs):
        #M 314.789,567.675 C 321.366,567.675 331.23,560.379 331.23,553.879 331.23,547.729 324.249,548.651 324.826,551.921 325.305,554.641 326.93702,557.6368 328.60102,559.8448

        #z0 = P(0, -0)
        #c0 = P(2.32022, -0)
        #c1 = P(5.80002, 2.57387)
        #z1 = P(5.80002, 4.86692)
        #c2 = P(5.80002, 7.03651)
        #c3 = P(3.33728, 6.71124)
        #z2 = P(3.54083, 5.55766)
        #c4 = P(3.70981, 4.59811)
        #c5 = P(4.28555, 3.54125)
        z3 = P(4.87257, 2.76232)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.32022, 0)
        #z1 = z0 + P(5.80002, 4.86692)
        #c1 = z1 + P(0, -2.29306)
        #c2 = z1 + P(0, 2.16958)
        #z2 = z1 + P(-2.25919, 0.690739)
        #c3 = z2 + P(-0.203553, 1.15358)
        #c4 = z2 + P(0.168981, -0.959556)
        #z3 = z2 + P(1.33174, -2.79534)
        #c5 = z3 + P(-0.587022, 0.778933)

        z0 = P(0, -0)
        c0 = z0 + PP(2.32022, 0)
        z1 = z0 + PP(7.57147, 40)
        c1 = z1 + PP(2.29306, -90)
        c2 = z1 + PP(2.16958, 90)
        z2 = z1 + PP(2.36243, 162)
        #z2 = z3 - PP(3.09636, ta + -11)
        c3 = z2 + PP(1.1714, 100)
        c4 = z2 + PP(0.974321, -80)
        z3 = z2 + PP(3.09636, -64)
        c5 = z3 + PP(0.975363, 127)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])

    @classmethod
    def path_NELCLNE(cls, ta=None, **kwargs):
        #M 257.495,106.89 C 263.225,103.714 274.65135,98.806744 273.896,91.5963 273.41282,86.983919 262.3878,93.979303 264.233,99.2493 264.89663,101.14466 268.16047,100.2385 269.685,99.2493 271.61164,97.999182 275.10102,95.118948 275.10102,95.118948

        #z0 = P(0, -0)
        #c0 = P(2.02142, 1.12042)
        #c1 = P(6.05238, 2.85159)
        #z1 = P(5.78591, 5.39528)
        #c2 = P(5.61545, 7.02242)
        #c3 = P(1.72607, 4.55461)
        #z2 = P(2.37702, 2.69547)
        #c4 = P(2.61113, 2.02683)
        #c5 = P(3.76254, 2.3465)
        #z3 = P(4.30036, 2.69547)
        #c6 = P(4.98004, 3.13648)
        #c7 = P(6.21101, 4.15257)
        z4 = P(6.21101, 4.15257)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.02142, 1.12042)
        #z1 = z0 + P(5.78591, 5.39528)
        #c1 = z1 + P(0.266471, -2.54368)
        #c2 = z1 + P(-0.170455, 1.62715)
        #z2 = z1 + P(-3.40889, -2.69981)
        #c3 = z2 + P(-0.650946, 1.85914)
        #c4 = z2 + P(0.234114, -0.668641)
        #z3 = z2 + P(1.92334, 0)
        #c5 = z3 + P(-0.53782, -0.348968)
        #c6 = z3 + P(0.679676, 0.441014)
        #z4 = z3 + P(1.91065, 1.4571)
        #c7 = z4 + P(0, 0)

        z0 = P(0, -0)
        c0 = z0 + PP(2.31116, 28)
        z1 = z0 + PP(7.91112, 42)
        c1 = z1 + PP(2.5576, -84)
        c2 = z1 + PP(1.63605, 95)
        z2 = z1 + PP(4.34851, -141)
        c3 = z2 + PP(1.9698, 109)
        c4 = z2 + PP(0.708442, -70)
        z3 = z2 + PP(1.92334, 0)
        #z3 = z4 - PP(2.40286, ta + 217)
        c5 = z3 + PP(0.641116, -147)
        c6 = z3 + PP(0.810217, 32)
        #z4 = z3 + PP(2.40286, 37)
        c7 = z4 + PP(0, 0)

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

    @classmethod
    def path_selNELCLNE(cls, ta=None, **kwargs):
        #M 63.614331,265.83723 C 70.165657,265.83723 76.155303,255.54649 75.399953,248.33605 74.916773,243.72367 63.891753,250.71905 65.736953,255.98905 66.400583,257.88441 69.537104,256.74674 71.188953,255.98905 73.234194,255.05091 74.971255,253.45614 76.604973,251.8587

        #z0 = P(0, -0)
        #c0 = P(2.31116, -0)
        #c1 = P(4.42418, 3.63034)
        #z1 = P(4.15771, 6.17403)
        #c2 = P(3.98725, 7.80117)
        #c3 = P(0.0978683, 5.33336)
        #z2 = P(0.748814, 3.47422)
        #c4 = P(0.982928, 2.80558)
        #c5 = P(2.08942, 3.20692)
        #z3 = P(2.67216, 3.47422)
        #c6 = P(3.39367, 3.80517)
        #c7 = P(4.00647, 4.36777)
        z4 = P(4.58281, 4.93131)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.31116, 0)
        #z1 = z0 + P(4.15771, 6.17403)
        #c1 = z1 + P(0.266471, -2.54368)
        #c2 = z1 + P(-0.170455, 1.62715)
        #z2 = z1 + P(-3.40889, -2.69981)
        #c3 = z2 + P(-0.650946, 1.85914)
        #c4 = z2 + P(0.234114, -0.668641)
        #z3 = z2 + P(1.92334, 0)
        #c5 = z3 + P(-0.582736, -0.267296)
        #c6 = z3 + P(0.721516, 0.330955)
        #z4 = z3 + P(1.91065, 1.4571)
        #c7 = z4 + P(-0.576339, -0.563541)

        z0 = P(0, -0)
        c0 = z0 + PP(2.31116, 0)
        z1 = z0 + PP(7.44346, 56)
        c1 = z1 + PP(2.5576, -84)
        c2 = z1 + PP(1.63605, 95)
        z2 = z1 + PP(4.34851, -141)
        c3 = z2 + PP(1.9698, 109)
        c4 = z2 + PP(0.708442, -70)
        z3 = z2 + PP(1.92334, 0)
        #z3 = z4 - PP(2.40286, ta + 352)
        c5 = z3 + PP(0.641115, -155)
        c6 = z3 + PP(0.793798, 24)
        #z4 = z3 + PP(2.40286, 37)
        c7 = z4 + PP(0.806068, -135)

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

    @classmethod
    def path_SWRCRNE(cls, ta=None, **kwargs):
        #M 409.622,307.442 C 410.592,315.335 406.83,327.443 402.483,326.91 396.778,326.209 403.17849,320.65665 409.443,316.192 410.64276,315.33694 411.32536,314.91087 412.69751,313.99864

        #z0 = P(0, -0)
        #c0 = P(0.342194, -2.78447)
        #c1 = P(-0.984956, -7.05591)
        #z1 = P(-2.51848, -6.86788)
        #c2 = P(-4.53108, -6.62058)
        #c3 = P(-2.27313, -4.66183)
        #z2 = P(-0.0631472, -3.08681)
        #c4 = P(0.360101, -2.78516)
        #c5 = P(0.600908, -2.63485)
        z3 = P(1.08497, -2.31304)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.342194, -2.78447)
        #z1 = z0 + P(-2.51848, -6.86788)
        #c1 = z1 + P(1.53352, -0.188031)
        #c2 = z1 + P(-2.0126, 0.247297)
        #z2 = z1 + P(2.45533, 3.78107)
        #c3 = z2 + P(-2.20998, -1.57503)
        #c4 = z2 + P(0.423249, 0.301646)
        #z3 = z2 + P(1.14812, 0.773769)
        #c5 = z3 + P(-0.484064, -0.321814)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80542, -82)
        z1 = z0 + PP(7.31509, -110)
        c1 = z1 + PP(1.54501, -6)
        c2 = z1 + PP(2.02773, 172)
        z2 = z1 + PP(4.50834, 57)
        #z2 = z3 - PP(1.38452, ta + 359)
        c3 = z2 + PP(2.7138, -144)
        c4 = z2 + PP(0.51974, 35)
        #z3 = z2 + PP(1.38452, 33)
        c5 = z3 + PP(0.581277, -146)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            #curve(),
            endknot(*z3)])


class CharSun(CharSu):
    def __init__(self, name='sun', kana='すん',
                 model='NEL8CL4NE1F|SWR8CR4NE1F', head_type='NEL|SWR',
                 tail_type='NEF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharSui(WasedaChar):
    def __init__(self, name='sui', kana='すい',
                 model='SWR8CNR4', head_type='SWR',
                 tail_type='CNR'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {'ER', 'NE', 'NER', 'NEL', 'S', 'SL', 'SEL', 'SW', 'SWR'}


    @classmethod
    def path_SWRCNR(cls, ta=None, **kwargs):
        #M 402.729,174.327 C 402.92056,180.9449 400.59939,192.82526 392.39182,192.92856 391.28491,192.94249 390.27519,192.54729 389.85654,191.70798 389.23636,190.46463 389.23951,187.74194 389.68179,185.83349 390.03015,184.33031 390.9051,181.79559 391.84069,181.73871 393.83949,181.6172 392.0942,189.32518 391.957,192.86396

        #z0 = P(0, -0)
        #c0 = P(0.0675781, -2.33465)
        #c1 = P(-0.751279, -6.52578)
        #z1 = P(-3.64673, -6.56222)
        #c2 = P(-4.03722, -6.56713)
        #c3 = P(-4.39343, -6.42771)
        #z2 = P(-4.54112, -6.13162)
        #c4 = P(-4.7599, -5.693)
        #c5 = P(-4.75879, -4.73249)
        #z3 = P(-4.60277, -4.05923)
        #c6 = P(-4.47987, -3.52895)
        #c7 = P(-4.17121, -2.63475)
        #z4 = P(-3.84115, -2.61469)
        #c8 = P(-3.13602, -2.57182)
        #c9 = P(-3.75172, -5.29102)
        z5 = P(-3.80012, -6.53943)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0675781, -2.33465)
        #z1 = z0 + P(-3.64673, -6.56222)
        #c1 = z1 + P(2.89545, 0.0364419)
        #c2 = z1 + P(-0.390493, -0.00491419)
        #z2 = z1 + P(-0.89439, 0.430594)
        #c3 = z2 + P(0.14769, -0.29609)
        #c4 = z2 + P(-0.218786, 0.438626)
        #z3 = z2 + P(-0.0616479, 2.07239)
        #c5 = z3 + P(-0.156027, -0.673259)
        #c6 = z3 + P(0.122894, 0.530289)
        #z4 = z3 + P(0.761612, 1.44455)
        #c7 = z4 + P(-0.330055, -0.020066)
        #c8 = z4 + P(0.705132, 0.042866)
        #z5 = z4 + P(0.0410316, -3.92474)
        #c9 = z5 + P(0.0484011, 1.2484)

        z0 = P(0, -0)
        c0 = z0 + PP(2.33563, -88)
        z1 = z0 + PP(7.50742, -119)
        c1 = z1 + PP(2.89568, 0)
        c2 = z1 + PP(0.390524, -179)
        z2 = z1 + PP(0.992645, 154)
        c3 = z2 + PP(0.33088, -63)
        c4 = z2 + PP(0.490163, 116)
        z3 = z2 + PP(2.07331, 91)
        c5 = z3 + PP(0.691102, -103)
        c6 = z3 + PP(0.544342, 76)
        z4 = z3 + PP(1.63302, 62)
        #z4 = z5 - PP(3.92496, ta + 4)
        c7 = z4 + PP(0.330665, -176)
        c8 = z4 + PP(0.706434, 3)
        z5 = z4 + PP(3.92496, -89)
        c9 = z5 + PP(1.24934, 87)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCNRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCNRer(cls, ta=None, **kwargs):
        #M 116.893,133.91 C 117.124,140.527 113.31983,151.21689 106.576,152.193 105.469,152.212 104.3905,151.5475 103.9645,150.7115 103.3555,149.4625 103.504,147.322 103.944,145.413 104.317,143.916 105.182,141.391 106.117,141.326 108.117,141.221 106.5795,148.583 106.3945,152.12

        #z0 = P(0, -0)
        #c0 = P(0.0814917, -2.33433)
        #c1 = P(-1.26053, -6.10549)
        #z1 = P(-3.63961, -6.44984)
        #c2 = P(-4.03013, -6.45654)
        #c3 = P(-4.4106, -6.22212)
        #z2 = P(-4.56089, -5.9272)
        #c4 = P(-4.77573, -5.48658)
        #c5 = P(-4.72334, -4.73146)
        #z3 = P(-4.56812, -4.058)
        #c6 = P(-4.43653, -3.52989)
        #c7 = P(-4.13138, -2.63913)
        #z4 = P(-3.80153, -2.6162)
        #c8 = P(-3.09598, -2.57916)
        #c9 = P(-3.63837, -5.17631)
        z5 = P(-3.70364, -6.42408)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0814917, -2.33433)
        #z1 = z0 + P(-3.63961, -6.44984)
        #c1 = z1 + P(2.37907, 0.34435)
        #c2 = z1 + P(-0.390525, -0.00670278)
        #z2 = z1 + P(-0.921279, 0.52264)
        #c3 = z2 + P(0.150283, -0.294922)
        #c4 = z2 + P(-0.214842, 0.440619)
        #z3 = z2 + P(-0.00723194, 1.86919)
        #c5 = z3 + P(-0.155222, -0.673453)
        #c6 = z3 + P(0.131586, 0.528108)
        #z4 = z3 + P(0.766586, 1.4418)
        #c7 = z4 + P(-0.329847, -0.0229306)
        #c8 = z4 + P(0.705556, 0.0370417)
        #z5 = z4 + P(0.0978958, -3.80788)
        #c9 = z5 + P(0.0652639, 1.24778)

        z0 = P(0, -0)
        c0 = z0 + PP(2.33575, -88)
        z1 = z0 + PP(7.40589, -119)
        c1 = z1 + PP(2.40386, 8)
        c2 = z1 + PP(0.390583, -179)
        z2 = z1 + PP(1.0592, 150)
        c3 = z2 + PP(0.331005, -62)
        c4 = z2 + PP(0.490207, 115)
        z3 = z2 + PP(1.86921, 90)
        c5 = z3 + PP(0.69111, -102)
        c6 = z3 + PP(0.544255, 76)
        z4 = z3 + PP(1.63293, 62)
        #z4 = z5 - PP(3.80914, ta + 5)
        c7 = z4 + PP(0.330643, -176)
        c8 = z4 + PP(0.706527, 3)
        z5 = z4 + PP(3.80914, -88)
        c9 = z5 + PP(1.24948, 87)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCNRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCNRne(cls, ta=None, **kwargs):
        #M221.486804513 133.840041859C221.647039112 140.506797811 220.023887264 152.576142285 214.330448633 152.593008547C213.562471304 152.59528479 212.871704702 152.192018689 212.57621468 151.349728408C212.153781164 150.091336821 212.199566197 147.352895672 212.505459148 145.429540184C212.764196206 143.921283253 213.364199642 141.37729546 214.012755863 141.311805832C215.400050155 141.206015665 214.275648886 148.955862379 214.147325856 152.519456805

        #z0 = P(0, -0)
        #c0 = P(0.0565272, -2.35188)
        #c1 = P(-0.516085, -6.60968)
        #z1 = P(-2.5246, -6.61563)
        #c2 = P(-2.79553, -6.61643)
        #c3 = P(-3.03922, -6.47417)
        #z2 = P(-3.14346, -6.17703)
        #c4 = P(-3.29248, -5.7331)
        #c5 = P(-3.27633, -4.76703)
        #z3 = P(-3.16842, -4.08852)
        #c6 = P(-3.07714, -3.55644)
        #c7 = P(-2.86547, -2.65898)
        #z4 = P(-2.63668, -2.63587)
        #c8 = P(-2.14727, -2.59855)
        #c9 = P(-2.54394, -5.33253)
        z5 = P(-2.5892, -6.58968)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0565272, -2.35188)
        #z1 = z0 + P(-2.5246, -6.61563)
        #c1 = z1 + P(2.00852, 0.00595004)
        #c2 = z1 + P(-0.270925, -0.000803008)
        #z2 = z1 + P(-0.618855, 0.438602)
        #c3 = z2 + P(0.104242, -0.297141)
        #c4 = z2 + P(-0.149025, 0.443933)
        #z3 = z2 + P(-0.024961, 2.08851)
        #c5 = z3 + P(-0.107912, -0.678517)
        #c6 = z3 + P(0.0912767, 0.53208)
        #z4 = z3 + P(0.531741, 1.45265)
        #c7 = z4 + P(-0.228796, -0.0231033)
        #c8 = z4 + P(0.489407, 0.0373204)
        #z5 = z4 + P(0.0474733, -3.95381)
        #c9 = z5 + P(0.0452695, 1.25716)

        z0 = P(0, -0)
        c0 = z0 + PP(2.35256, -88)
        z1 = z0 + PP(7.08097, -110)
        c1 = z1 + PP(2.00853, 0)
        c2 = z1 + PP(0.270927, -179)
        z2 = z1 + PP(0.75852, 144)
        c3 = z2 + PP(0.314896, -70)
        c4 = z2 + PP(0.468278, 108)
        z3 = z2 + PP(2.08866, 90)
        c5 = z3 + PP(0.687045, -99)
        c6 = z3 + PP(0.539852, 80)
        z4 = z3 + PP(1.54691, 69)
        #z4 = z5 - PP(3.9541, ta + 4)
        c7 = z4 + PP(0.22996, -174)
        c8 = z4 + PP(0.490827, 4)
        z5 = z4 + PP(3.9541, -89)
        c9 = z5 + PP(1.25797, 87)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCNRner(cls, ta=None, **kwargs):
        #M221.486804513 133.840041859C221.647039112 140.506797811 220.023887264 152.576142285 214.330448633 152.593008547C213.562471304 152.59528479 212.871704702 152.192018689 212.57621468 151.349728408C212.153781164 150.091336821 212.199566197 147.352895672 212.505459148 145.429540184C212.764196206 143.921283253 213.364199642 141.37729546 214.012755863 141.311805832C215.400050155 141.206015665 214.275648886 148.955862379 214.147325856 152.519456805

        #z0 = P(0, -0)
        #c0 = P(0.0565272, -2.35188)
        #c1 = P(-0.516085, -6.60968)
        #z1 = P(-2.5246, -6.61563)
        #c2 = P(-2.79553, -6.61643)
        #c3 = P(-3.03922, -6.47417)
        #z2 = P(-3.14346, -6.17703)
        #c4 = P(-3.29248, -5.7331)
        #c5 = P(-3.27633, -4.76703)
        #z3 = P(-3.16842, -4.08852)
        #c6 = P(-3.07714, -3.55644)
        #c7 = P(-2.86547, -2.65898)
        #z4 = P(-2.63668, -2.63587)
        #c8 = P(-2.14727, -2.59855)
        #c9 = P(-2.54394, -5.33253)
        z5 = P(-2.5892, -6.58968)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0565272, -2.35188)
        #z1 = z0 + P(-2.5246, -6.61563)
        #c1 = z1 + P(2.00852, 0.00595004)
        #c2 = z1 + P(-0.270925, -0.000803008)
        #z2 = z1 + P(-0.618855, 0.438602)
        #c3 = z2 + P(0.104242, -0.297141)
        #c4 = z2 + P(-0.149025, 0.443933)
        #z3 = z2 + P(-0.024961, 2.08851)
        #c5 = z3 + P(-0.107912, -0.678517)
        #c6 = z3 + P(0.0912767, 0.53208)
        #z4 = z3 + P(0.531741, 1.45265)
        #c7 = z4 + P(-0.228796, -0.0231033)
        #c8 = z4 + P(0.489407, 0.0373204)
        #z5 = z4 + P(0.0474733, -3.95381)
        #c9 = z5 + P(0.0452695, 1.25716)

        z0 = P(0, -0)
        c0 = z0 + PP(2.35256, -88)
        z1 = z0 + PP(7.08097, -110)
        c1 = z1 + PP(2.00853, 0)
        c2 = z1 + PP(0.270927, -179)
        z2 = z1 + PP(0.75852, 144)
        c3 = z2 + PP(0.314896, -70)
        c4 = z2 + PP(0.468278, 108)
        z3 = z2 + PP(2.08866, 90)
        c5 = z3 + PP(0.687045, -99)
        c6 = z3 + PP(0.539852, 80)
        z4 = z3 + PP(1.54691, 69)
        #z4 = z5 - PP(3.9541, ta + 4)
        c7 = z4 + PP(0.22996, -174)
        c8 = z4 + PP(0.490827, 4)
        z5 = z4 + PP(3.9541, -89)
        c9 = z5 + PP(1.25797, 87)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCNRnel(cls, ta=None, **kwargs):
        #M 199.303,133.91 C 199.534,140.527 198.43508,152.1678 190.33993,152.18452 189.23277,152.1868 188.23693,151.78652 187.81093,150.95052 187.20193,149.70152 187.26793,146.98352 187.70793,145.07452 188.08193,143.57752 188.94693,141.05252 189.88193,140.98752 191.88093,140.88252 190.26093,148.57452 190.07593,152.11152

        #z0 = P(0, -0)
        #c0 = P(0.0814917, -2.33433)
        #c1 = P(-0.306183, -6.44095)
        #z1 = P(-3.16197, -6.44684)
        #c2 = P(-3.55255, -6.44765)
        #c3 = P(-3.90386, -6.30644)
        #z2 = P(-4.05415, -6.01152)
        #c4 = P(-4.26899, -5.5709)
        #c5 = P(-4.24571, -4.61205)
        #z3 = P(-4.09048, -3.93859)
        #c6 = P(-3.95854, -3.41049)
        #c7 = P(-3.65339, -2.51972)
        #z4 = P(-3.32354, -2.49679)
        #c8 = P(-2.61834, -2.45975)
        #c9 = P(-3.18984, -5.17332)
        z5 = P(-3.25511, -6.42109)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0814917, -2.33433)
        #z1 = z0 + P(-3.16197, -6.44684)
        #c1 = z1 + P(2.85579, 0.00589844)
        #c2 = z1 + P(-0.390581, -0.000804333)
        #z2 = z1 + P(-0.892175, 0.435328)
        #c3 = z2 + P(0.150283, -0.294922)
        #c4 = z2 + P(-0.214842, 0.440619)
        #z3 = z2 + P(-0.0363361, 2.07292)
        #c5 = z3 + P(-0.155222, -0.673453)
        #c6 = z3 + P(0.131939, 0.528108)
        #z4 = z3 + P(0.766939, 1.4418)
        #c7 = z4 + P(-0.329847, -0.0229306)
        #c8 = z4 + P(0.705203, 0.0370417)
        #z5 = z4 + P(0.0684389, -3.9243)
        #c9 = z5 + P(0.0652639, 1.24778)

        z0 = P(0, -0)
        c0 = z0 + PP(2.33575, -88)
        z1 = z0 + PP(7.18052, -116)
        c1 = z1 + PP(2.8558, 0)
        c2 = z1 + PP(0.390582, -179)
        z2 = z1 + PP(0.992717, 153)
        c3 = z2 + PP(0.331005, -62)
        c4 = z2 + PP(0.490207, 115)
        z3 = z2 + PP(2.07324, 91)
        c5 = z3 + PP(0.69111, -102)
        c6 = z3 + PP(0.54434, 75)
        z4 = z3 + PP(1.63309, 61)
        #z4 = z5 - PP(3.9249, ta + 4)
        c7 = z4 + PP(0.330643, -176)
        c8 = z4 + PP(0.706175, 3)
        z5 = z4 + PP(3.9249, -89)
        c9 = z5 + PP(1.24948, 87)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCNRs(cls, ta=None, **kwargs):
        #M 163.767,133.91 C 163.998,140.527 161.658,152.523 153.45,152.523 152.343,152.542 151.347,152.125 150.921,151.289 150.312,150.04 150.378,147.322 150.819,145.413 151.192,143.916 152.057,141.391 152.992,141.326 154.992,141.221 153.36692,148.99097 153.186,152.45

        #z0 = P(0, -0)
        #c0 = P(0.0814917, -2.33433)
        #c1 = P(-0.744008, -6.56625)
        #z1 = P(-3.63961, -6.56625)
        #c2 = P(-4.03013, -6.57296)
        #c3 = P(-4.3815, -6.42585)
        #z2 = P(-4.53178, -6.13092)
        #c4 = P(-4.74662, -5.69031)
        #c5 = P(-4.72334, -4.73146)
        #z3 = P(-4.56777, -4.058)
        #c6 = P(-4.43618, -3.52989)
        #c7 = P(-4.13103, -2.63913)
        #z4 = P(-3.80118, -2.6162)
        #c8 = P(-3.09563, -2.57916)
        #c9 = P(-3.66892, -5.32023)
        z5 = P(-3.73274, -6.5405)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0814917, -2.33433)
        #z1 = z0 + P(-3.63961, -6.56625)
        #c1 = z1 + P(2.8956, 0)
        #c2 = z1 + P(-0.390525, -0.00670278)
        #z2 = z1 + P(-0.892175, 0.435328)
        #c3 = z2 + P(0.150283, -0.294922)
        #c4 = z2 + P(-0.214842, 0.440619)
        #z3 = z2 + P(-0.0359833, 2.07292)
        #c5 = z3 + P(-0.155575, -0.673453)
        #c6 = z3 + P(0.131586, 0.528108)
        #z4 = z3 + P(0.766586, 1.4418)
        #c7 = z4 + P(-0.329847, -0.0229306)
        #c8 = z4 + P(0.705556, 0.0370417)
        #z5 = z4 + P(0.0684389, -3.9243)
        #c9 = z5 + P(0.0638246, 1.22027)

        z0 = P(0, -0)
        c0 = z0 + PP(2.33575, -88)
        z1 = z0 + PP(7.50749, -118)
        c1 = z1 + PP(2.8956, 0)
        c2 = z1 + PP(0.390583, -179)
        z2 = z1 + PP(0.992717, 153)
        c3 = z2 + PP(0.331005, -62)
        c4 = z2 + PP(0.490207, 115)
        z3 = z2 + PP(2.07323, 90)
        c5 = z3 + PP(0.691189, -103)
        c6 = z3 + PP(0.544255, 76)
        z4 = z3 + PP(1.63293, 62)
        #z4 = z5 - PP(3.9249, ta + 4)
        c7 = z4 + PP(0.330643, -176)
        c8 = z4 + PP(0.706527, 3)
        z5 = z4 + PP(3.9249, -89)
        #c9 = z5 + PP(1.22194, 87)
        c9 = z5 + PP(1.22194, ta+180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCNRsl(cls, ta=None, **kwargs):
        #M 181.535,133.91 C 181.766,140.527 179.426,152.523 171.218,152.523 170.111,152.542 169.115,152.125 168.689,151.289 168.08,150.04 168.3623,147.34563 169.08097,145.57799 169.72682,143.98949 171.19356,140.61285 172.40993,141.65599 173.13937,142.28154 172.8307,144.23024 172.18828,146.37683 171.54585,148.52342 170.56965,150.8679 169.96404,152.28501

        #z0 = P(0, -0)
        #c0 = P(0.0814917, -2.33433)
        #c1 = P(-0.744008, -6.56625)
        #z1 = P(-3.63961, -6.56625)
        #c2 = P(-4.03013, -6.57296)
        #c3 = P(-4.3815, -6.42585)
        #z2 = P(-4.53178, -6.13092)
        #c4 = P(-4.74662, -5.69031)
        #c5 = P(-4.64704, -4.73979)
        #z3 = P(-4.39351, -4.11621)
        #c6 = P(-4.16566, -3.55582)
        #c7 = P(-3.64823, -2.36462)
        #z4 = P(-3.21912, -2.73261)
        #c8 = P(-2.96179, -2.95329)
        #c9 = P(-3.07068, -3.64075)
        #z5 = P(-3.29732, -4.39802)
        #c10 = P(-3.52395, -5.15529)
        #c11 = P(-3.86833, -5.98237)
        z6 = P(-4.08198, -6.4823)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0814917, -2.33433)
        #z1 = z0 + P(-3.63961, -6.56625)
        #c1 = z1 + P(2.8956, 0)
        #c2 = z1 + P(-0.390525, -0.00670278)
        #z2 = z1 + P(-0.892175, 0.435328)
        #c3 = z2 + P(0.150283, -0.294922)
        #c4 = z2 + P(-0.214842, 0.440619)
        #z3 = z2 + P(0.138278, 2.01472)
        #c5 = z3 + P(-0.253531, -0.623584)
        #c6 = z3 + P(0.227842, 0.560388)
        #z4 = z3 + P(1.17438, 1.38359)
        #c7 = z4 + P(-0.429108, 0.367997)
        #c8 = z4 + P(0.25733, -0.22068)
        #z5 = z4 + P(-0.0781932, -1.66541)
        #c9 = z5 + P(0.226632, 0.757269)
        #c10 = z5 + P(-0.226635, -0.757269)
        #z6 = z5 + P(-0.784662, -2.08427)
        #c11 = z6 + P(0.213646, 0.499925)

        z0 = P(0, -0)
        c0 = z0 + PP(2.33575, -88)
        z1 = z0 + PP(7.50749, -118)
        c1 = z1 + PP(2.8956, 0)
        c2 = z1 + PP(0.390583, -179)
        z2 = z1 + PP(0.992717, 153)
        c3 = z2 + PP(0.331005, -62)
        c4 = z2 + PP(0.490207, 115)
        z3 = z2 + PP(2.01946, 86)
        c5 = z3 + PP(0.673153, -112)
        c6 = z3 + PP(0.604935, 67)
        z4 = z3 + PP(1.8148, 49)
        c7 = z4 + PP(0.565292, 139)
        c8 = z4 + PP(0.338996, -40)
        #z5 = z4 + PP(1.66724, -92)
        z5 = z6 - PP(2.22708, ta + 4)
        c9 = z5 + PP(0.790455, 73)
        #c10 = z5 + PP(0.790456, -106)
        #z6 = z5 + PP(2.22708, -110)
        #c11 = z6 + PP(0.543663, 66)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            #controlcurve(c10, c11),
            curve(),
            endknot(*z6, angle=ta)])

    @classmethod
    def path_SWRCNRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCNRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCNRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCNRsel(cls, ta=None, **kwargs):
        #M 121.642,226.515 C 121.873,233.131 119.533,245.127 111.325,245.127 110.218,245.147 109.222,244.73 108.796,243.894 108.187,242.645 108.253,239.926 108.693,238.018 109.067,236.52 109.932,233.996 110.867,233.93 111.8665,233.878 111.9265,235.77387 111.73088,238.12542 111.53525,240.47698 111.084,243.28423 111.061,245.055

        #z0 = P(0, -0)
        #c0 = P(0.0814917, -2.33398)
        #c1 = P(-0.744008, -6.5659)
        #z1 = P(-3.63961, -6.5659)
        #c2 = P(-4.03013, -6.57296)
        #c3 = P(-4.3815, -6.42585)
        #z2 = P(-4.53178, -6.13093)
        #c4 = P(-4.74662, -5.69031)
        #c5 = P(-4.72334, -4.7311)
        #z3 = P(-4.56812, -4.058)
        #c6 = P(-4.43618, -3.52954)
        #c7 = P(-4.13103, -2.63913)
        #z4 = P(-3.80118, -2.61585)
        #c8 = P(-3.44858, -2.5975)
        #c9 = P(-3.42741, -3.26632)
        #z5 = P(-3.49642, -4.0959)
        #c10 = P(-3.56544, -4.92548)
        #c11 = P(-3.72463, -5.91581)
        z6 = P(-3.73274, -6.5405)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0814917, -2.33398)
        #z1 = z0 + P(-3.63961, -6.5659)
        #c1 = z1 + P(2.8956, 0)
        #c2 = z1 + P(-0.390525, -0.00705556)
        #z2 = z1 + P(-0.892175, 0.434975)
        #c3 = z2 + P(0.150283, -0.294922)
        #c4 = z2 + P(-0.214842, 0.440619)
        #z3 = z2 + P(-0.0363361, 2.07292)
        #c5 = z3 + P(-0.155222, -0.6731)
        #c6 = z3 + P(0.131939, 0.528461)
        #z4 = z3 + P(0.766939, 1.44216)
        #c7 = z4 + P(-0.329847, -0.0232833)
        #c8 = z4 + P(0.352601, 0.0183444)
        #z5 = z4 + P(0.304758, -1.48005)
        #c9 = z5 + P(0.0690104, 0.829575)
        #c10 = z5 + P(-0.0690139, -0.829578)
        #z6 = z5 + P(-0.236319, -2.4446)
        #c11 = z6 + P(0.00811389, 0.624688)

        z0 = P(0, -0)
        c0 = z0 + PP(2.3354, -88)
        z1 = z0 + PP(7.50718, -119)
        c1 = z1 + PP(2.8956, 0)
        c2 = z1 + PP(0.390589, -178)
        z2 = z1 + PP(0.992562, 154)
        c3 = z2 + PP(0.331005, -62)
        c4 = z2 + PP(0.490207, 115)
        z3 = z2 + PP(2.07324, 91)
        c5 = z3 + PP(0.690766, -102)
        c6 = z3 + PP(0.544682, 75)
        z4 = z3 + PP(1.6334, 61)
        c7 = z4 + PP(0.330668, -175)
        c8 = z4 + PP(0.353078, 2)
        #z5 = z4 + PP(1.5111, -78)
        z5 = z6 - PP(2.456, ta + -4)
        c9 = z5 + PP(0.83244, 85)
        #c10 = z5 + PP(0.832444, -94)
        #z6 = z5 + PP(2.456, -95)
        #c11 = z6 + PP(0.624741, 89)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            #controlcurve(c10, c11),
            curve(),
            endknot(*z6, angle=ta)])

    @classmethod
    def path_SWRCNRsw(cls, ta=None, **kwargs):
        #M 47.3414,226.515 C 47.5725,233.131 43.461938,247.39832 35.532531,245.27684 34.458167,245.01011 33.603398,244.34975 33.408134,243.4321 33.142541,242.06811 33.908943,239.45853 34.827802,237.72926 35.575489,236.37861 37.063344,234.16391 37.983731,234.34183 39.942367,234.7582 36.389175,241.7701 35.295916,245.13901

        #z0 = P(0, -0)
        #c0 = P(0.0815269, -2.33398)
        #c1 = P(-1.36859, -7.36717)
        #z1 = P(-4.16591, -6.61876)
        #c2 = P(-4.54492, -6.52466)
        #c3 = P(-4.84646, -6.2917)
        #z2 = P(-4.91535, -5.96798)
        #c4 = P(-5.00904, -5.48679)
        #c5 = P(-4.73867, -4.56619)
        #z3 = P(-4.41452, -3.95614)
        #c6 = P(-4.15075, -3.47966)
        #c7 = P(-3.62587, -2.69837)
        #z4 = P(-3.30118, -2.76113)
        #c8 = P(-2.61021, -2.90802)
        #c9 = P(-3.8637, -5.38166)
        z5 = P(-4.24938, -6.57014)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0815269, -2.33398)
        #z1 = z0 + P(-4.16591, -6.61876)
        #c1 = z1 + P(2.79732, -0.748411)
        #c2 = z1 + P(-0.379012, 0.0940964)
        #z2 = z1 + P(-0.74944, 0.650783)
        #c3 = z2 + P(0.0688848, -0.323727)
        #c4 = z2 + P(-0.0936953, 0.481185)
        #z3 = z2 + P(0.500827, 2.01184)
        #c5 = z3 + P(-0.324153, -0.610048)
        #c6 = z3 + P(0.263767, 0.476479)
        #z4 = z3 + P(1.11334, 1.19501)
        #c7 = z4 + P(-0.324692, 0.0627662)
        #c8 = z4 + P(0.690963, -0.146886)
        #z5 = z4 + P(-0.948201, -3.80901)
        #c9 = z5 + P(0.385677, 1.18848)

        z0 = P(0, -0)
        c0 = z0 + PP(2.3354, -87)
        z1 = z0 + PP(7.82066, -122)
        c1 = z1 + PP(2.89571, -14)
        c2 = z1 + PP(0.390518, 166)
        z2 = z1 + PP(0.992562, 139)
        c3 = z2 + PP(0.330974, -77)
        c4 = z2 + PP(0.490223, 101)
        z3 = z2 + PP(2.07324, 76)
        c5 = z3 + PP(0.690821, -117)
        c6 = z3 + PP(0.544615, 61)
        z4 = z3 + PP(1.63327, 47)
        #z4 = z5 - PP(3.92525, ta + 5)
        c7 = z4 + PP(0.330703, 169)
        c8 = z4 + PP(0.706403, -12)
        #z5 = z4 + PP(3.92525, -103)
        #c9 = z5 + PP(1.24949, 72)
        c9 = z5 + PP(1.24949, ta+180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCNRswr(cls, ta=None, **kwargs):
        #M47.3414 226.515C47.5725 233.131 45.2325 245.127 37.0242 245.127C35.9174 245.147 34.921 244.73 34.4952 243.894C33.8861 242.645 33.952 239.926 34.3927 238.018C34.7659 236.52 35.6308 233.996 36.5659 233.93C38.5656 233.826 36.9454 241.518 36.76 245.055

        #z0 = P(0, -0)
        #c0 = P(0.0815269, -2.33398)
        #c1 = P(-0.743973, -6.5659)
        #z1 = P(-3.63968, -6.5659)
        #c2 = P(-4.03013, -6.57296)
        #c3 = P(-4.38164, -6.42585)
        #z2 = P(-4.53185, -6.13093)
        #c4 = P(-4.74673, -5.69031)
        #c5 = P(-4.72348, -4.7311)
        #z3 = P(-4.56801, -4.058)
        #c6 = P(-4.43636, -3.52954)
        #c7 = P(-4.13124, -2.63913)
        #z4 = P(-3.80136, -2.61585)
        #c8 = P(-3.09591, -2.57916)
        #c9 = P(-3.66748, -5.29273)
        z5 = P(-3.73288, -6.5405)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.0815269, -2.33398)
        #z1 = z0 + P(-3.63968, -6.5659)
        #c1 = z1 + P(2.89571, 0)
        #c2 = z1 + P(-0.390454, -0.00705556)
        #z2 = z1 + P(-0.892175, 0.434975)
        #c3 = z2 + P(0.150213, -0.294922)
        #c4 = z2 + P(-0.214877, 0.440619)
        #z3 = z2 + P(-0.0361597, 2.07292)
        #c5 = z3 + P(-0.155469, -0.6731)
        #c6 = z3 + P(0.131657, 0.528461)
        #z4 = z3 + P(0.766657, 1.44216)
        #c7 = z4 + P(-0.329882, -0.0232833)
        #c8 = z4 + P(0.70545, 0.0366889)
        #z5 = z4 + P(0.0684742, -3.92465)
        #c9 = z5 + P(0.065405, 1.24778)

        z0 = P(0, -0)
        c0 = z0 + PP(2.3354, -87)
        z1 = z0 + PP(7.50722, -119)
        c1 = z1 + PP(2.89571, 0)
        c2 = z1 + PP(0.390518, -178)
        z2 = z1 + PP(0.992562, 154)
        c3 = z2 + PP(0.330973, -63)
        c4 = z2 + PP(0.490222, 115)
        z3 = z2 + PP(2.07324, 90)
        c5 = z3 + PP(0.690821, -103)
        c6 = z3 + PP(0.544614, 76)
        z4 = z3 + PP(1.63327, 62)
        #z4 = z5 - PP(3.92525, ta + 5)
        c7 = z4 + PP(0.330703, -175)
        c8 = z4 + PP(0.706403, 2)
        z5 = z4 + PP(3.92525, -89)
        c9 = z5 + PP(1.24949, 86)
        #c9 = z5 + PP(1.24949, ta+180)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            #curve(),
            endknot(*z5)])

    @classmethod
    def path_SWRCNRswl(cls, ta=None, **kwargs):
        pass

class CharSuku(CharSu):
    def __init__(self, name='suku', kana='すく',
                 model='BNEL8CL4', head_type='BNEL', tail_type='NELCL4'):
        super().__init__(name, kana, model, head_type, tail_type)

    #def to_reverse(self):
    #    return False

    def get_paths(self):
        if getattr(self.before, 'tail_type', '') in {'', 'P', 'E'}:
            return self.barb(super().get_paths())
        else:
            return super().get_paths()

class CharSutsu(CharSu):
    def __init__(self, name='su', kana='す',
                 model='NEL8CL4SW1F', head_type='NEL',
                 tail_type='SWF'):
        super().__init__(name, kana, model, head_type, tail_type)
        self.tail_ligature = {}
        
    def to_reverse(self):
        return False

    def get_paths(self):
        return super(WasedaChar, self).get_paths()

    @classmethod
    def path_NELCLSWF(cls, ta=None, **kwargs):
        #M 296.017,106.89 C 301.747,103.714 312.398,99.6223 312.398,93.1456 312.398,88.937323 309.51246,90.749539 308.24729,93.647698 307.05914,96.369439 305.874,99.2291 304.858,102.023 304.51999,102.96062 304.16894,103.91129 303.95654,104.7233

        #z0 = P(0, -0)
        #c0 = P(2.02142, 1.12042)
        #c1 = P(5.77885, 2.56388)
        #z1 = P(5.77885, 4.84872)
        #c2 = P(5.77885, 6.33331)
        #c3 = P(4.7609, 5.694)
        #z2 = P(4.31457, 4.67159)
        #c4 = P(3.89542, 3.71142)
        #c5 = P(3.47733, 2.7026)
        #z3 = P(3.11891, 1.71697)
        #c6 = P(2.99967, 1.3862)
        #c7 = P(2.87582, 1.05082)
        z4 = P(2.80089, 0.764364)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.02142, 1.12042)
        #z1 = z0 + P(5.77885, 4.84872)
        #c1 = z1 + P(0, -2.28484)
        #c2 = z1 + P(0, 1.48459)
        #z2 = z1 + P(-1.46428, -0.177129)
        #c3 = z2 + P(0.446324, 1.02241)
        #c4 = z2 + P(-0.419153, -0.96017)
        #z3 = z2 + P(-1.19567, -2.95462)
        #c5 = z3 + P(0.358422, 0.985626)
        #c6 = z3 + P(-0.119242, -0.330772)
        #z4 = z3 + P(-0.318015, -0.952606)
        #c7 = z4 + P(0.07493, 0.286459)

        z0 = P(0, -0)
        c0 = z0 + PP(2.31116, 28)
        z1 = z0 + PP(7.54355, 39)
        c1 = z1 + PP(2.28484, -90)
        c2 = z1 + PP(1.48459, 90)
        z2 = z1 + PP(1.47495, -173)
        c3 = z2 + PP(1.11558, 66)
        c4 = z2 + PP(1.04767, -113)
        z3 = z2 + PP(3.18738, -112)
        #z3 = z4 - PP(1.00429, ta + -3)
        c5 = z3 + PP(1.04877, 70)
        c6 = z3 + PP(0.351609, -109)
        z4 = z3 + PP(1.00429, -108)
        c7 = z4 + PP(0.296097, 75)

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

class CharJiyuu(CharSutsu):
    def __init__(self, name='jiyuu', kana='じゆう',
                 model='NEL8CL4SW1F',
                 head_type='NEL', tail_type='SWF'):
        super().__init__(name, kana, model, head_type, tail_type)

class CharSushi(CharSu):
    def __init__(self, name='sushi', kana='すし',
                 model='NEL8CL4CR1|SWR8CR4CR1', head_type='NEL|SWR',
                 tail_type='CL4CR1|CR4CR1'):
        super().__init__(name, kana, model, head_type, tail_type)

    def get_paths(self):
        if self.to_reverse():
            self.model = 'SWR8CR4CR1'
            self.head_type = 'SWR'
            self.tail_type = 'CR4CR1'
            self.head_ligature = {'ER', 'NER'}
            #self.tail_ligature = {'ER', 'EL', 'E', 'NER', 'NE', 'NEL',
            #     'SW', 'S', 'SL', 'SR', 'SE', 'SER', 'SEL', 'SWR', 'SWL'}
            self.tail_ligature = {}
        else:
            self.model = 'NEL8CL4CR1'
            self.head_type = 'NEL'
            self.tail_type = 'CL4CR'
            self.head_ligature = {'SEL', 'SL', 'SWL'}
            #self.tail_ligature = {'ER', 'E', 'EL', 'NE', 'NER', 'NEL',
            #    'SW', 'SWL', 'S', 'SL', 'SER', 'SEL'}
            self.tail_ligature = {}

        return super(WasedaChar, self).get_paths()

    @classmethod
    def path_SWRCRCR(cls, ta=None, **kwargs):
        #M 389.9,143.114 C 390.869,151.008 387.76719,164.00638 383.145,162.732 381.97705,162.40999 381.72862,160.60294 382.10025,159.55035 382.98674,157.03943 386.23735,155.9123 388.80527,155.20775 389.60426,154.98854 390.67419,154.74962 391.2889,155.30511 391.64735,155.62903 391.68959,156.29956 391.49159,156.74025 391.2087,157.36989 390.42284,158.09833 389.76622,157.88542 388.86678,157.59378 388.89771,156.71367 388.77298,155.22838

        #z0 = P(0, -0)
        #c0 = P(0.341842, -2.78483)
        #c1 = P(-0.752408, -7.37037)
        #z1 = P(-2.38301, -6.92079)
        #c2 = P(-2.79504, -6.8072)
        #c3 = P(-2.88268, -6.16971)
        #z2 = P(-2.75158, -5.79838)
        #c4 = P(-2.43884, -4.91258)
        #c5 = P(-1.2921, -4.51496)
        #z3 = P(-0.386196, -4.26641)
        #c6 = P(-0.10433, -4.18907)
        #c7 = P(0.273117, -4.10479)
        #z4 = P(0.489973, -4.30075)
        #c8 = P(0.616426, -4.41502)
        #c9 = P(0.631328, -4.65157)
        #z5 = P(0.561478, -4.80704)
        #c10 = P(0.46168, -5.02916)
        #c11 = P(0.184446, -5.28614)
        #z6 = P(-0.0471946, -5.21103)
        #c12 = P(-0.364497, -5.10814)
        #c13 = P(-0.353586, -4.79766)
        z7 = P(-0.397588, -4.27368)

        #z0 = P(0, -0)
        #c0 = z0 + P(0.341842, -2.78483)
        #z1 = z0 + P(-2.38301, -6.92079)
        #c1 = z1 + P(1.63061, -0.449573)
        #c2 = z1 + P(-0.412027, 0.113598)
        #z2 = z1 + P(-0.368565, 1.12242)
        #c3 = z2 + P(-0.131103, -0.37133)
        #c4 = z2 + P(0.312734, 0.885797)
        #z3 = z2 + P(2.36538, 1.53197)
        #c5 = z3 + P(-0.905905, -0.24855)
        #c6 = z3 + P(0.281866, 0.0773324)
        #z4 = z3 + P(0.876169, -0.0343464)
        #c7 = z4 + P(-0.216856, 0.195965)
        #c8 = z4 + P(0.126453, -0.114272)
        #z5 = z4 + P(0.0715045, -0.506285)
        #c9 = z5 + P(0.06985, 0.155466)
        #c10 = z5 + P(-0.0997973, -0.222123)
        #z6 = z5 + P(-0.608672, -0.403991)
        #c11 = z6 + P(0.231641, -0.0751099)
        #c12 = z6 + P(-0.317302, 0.102884)
        #z7 = z6 + P(-0.350393, 0.937345)
        #c13 = z7 + P(0.044002, -0.523977)

        z0 = P(0, -0)
        c0 = z0 + PP(2.80573, -83)
        z1 = z0 + PP(7.31957, -108)
        c1 = z1 + PP(1.69145, -15)
        c2 = z1 + PP(0.4274, 164)
        z2 = z1 + PP(1.18138, 108)
        c3 = z2 + PP(0.393795, -109)
        c4 = z2 + PP(0.939382, 70)
        z3 = z2 + PP(2.81815, 32)
        c5 = z3 + PP(0.939383, -164)
        c6 = z3 + PP(0.292282, 15)
        z4 = z3 + PP(0.876842, -2)
        c7 = z4 + PP(0.292282, 137)
        c8 = z4 + PP(0.170436, -42)
        z5 = z4 + PP(0.51131, -81)
        c9 = z5 + PP(0.170436, 65)
        c10 = z5 + PP(0.243512, -114)
        z6 = z5 + PP(0.730541, -146)
        #z6 = z7 - PP(1.00069, ta + 375)
        c11 = z6 + PP(0.243514, -17)
        c12 = z6 + PP(0.333566, 162)
        z7 = z6 + PP(1.00069, 110)
        c13 = z7 + PP(0.525822, -85)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            knot(*z6),
            controlcurve(c12, c13),
            #curve(),
            endknot(*z7)])

    @classmethod
    def path_nerSWRCRCR(cls, ta=None, **kwargs):
        #M 128.905,585.768 C 134.10995,590.08726 127.124,606.741 122.493,605.5 121.329,605.167 121.095,603.371 121.458,602.316 122.369,599.813 126.53783,598.90248 129.09783,598.16848 129.89783,597.95448 130.97583,597.69048 131.58183,598.25548 131.94083,598.57848 132.01283,599.24948 131.80883,599.68748 131.52783,600.31748 130.75183,601.04648 130.09183,600.84548 129.19283,600.55248 129.25183,599.66448 129.12183,598.17948

        #z0 = P(0, -0)
        #c0 = P(1.83619, -1.52374)
        #c1 = P(-0.628297, -7.39881)
        #z1 = P(-2.26201, -6.96101)
        #c2 = P(-2.67264, -6.84354)
        #c3 = P(-2.75519, -6.20995)
        #z2 = P(-2.62714, -5.83777)
        #c4 = P(-2.30576, -4.95476)
        #c5 = P(-0.835085, -4.63355)
        #z3 = P(0.0680261, -4.37461)
        #c6 = P(0.350248, -4.29912)
        #c7 = P(0.730543, -4.20599)
        #z4 = P(0.944326, -4.40531)
        #c8 = P(1.07097, -4.51925)
        #c9 = P(1.09637, -4.75597)
        #z5 = P(1.02441, -4.91048)
        #c10 = P(0.925276, -5.13273)
        #c11 = P(0.651521, -5.38991)
        #z6 = P(0.418687, -5.319)
        #c12 = P(0.10154, -5.21564)
        #c13 = P(0.122354, -4.90237)
        z7 = P(0.0764928, -4.37849)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.83619, -1.52374)
        #z1 = z0 + P(-2.26201, -6.96101)
        #c1 = z1 + P(1.63371, -0.437797)
        #c2 = z1 + P(-0.410633, 0.117475)
        #z2 = z1 + P(-0.365125, 1.12324)
        #c3 = z2 + P(-0.128058, -0.372181)
        #c4 = z2 + P(0.321381, 0.883003)
        #z3 = z2 + P(2.69516, 1.46315)
        #c5 = z3 + P(-0.903111, -0.258939)
        #c6 = z3 + P(0.282222, 0.0754944)
        #z4 = z3 + P(0.8763, -0.0306917)
        #c7 = z4 + P(-0.213783, 0.199319)
        #c8 = z4 + P(0.126647, -0.113947)
        #z5 = z4 + P(0.0800806, -0.505178)
        #c9 = z5 + P(0.0719667, 0.154517)
        #c10 = z5 + P(-0.0991306, -0.22225)
        #z6 = z5 + P(-0.605719, -0.408517)
        #c11 = z6 + P(0.232833, -0.0709083)
        #c12 = z6 + P(-0.317147, 0.103364)
        #z7 = z6 + P(-0.342194, 0.940506)
        #c13 = z7 + P(0.0458611, -0.523875)

        z0 = P(0, -0)
        c0 = z0 + PP(2.38608, -39)
        z1 = z0 + PP(7.31931, -108)
        c1 = z1 + PP(1.69136, -15)
        c2 = z1 + PP(0.427107, 164)
        z2 = z1 + PP(1.1811, 108)
        c3 = z2 + PP(0.393595, -108)
        c4 = z2 + PP(0.93967, 70)
        z3 = z2 + PP(3.06671, 28)
        c5 = z3 + PP(0.939499, -164)
        c6 = z3 + PP(0.292145, 14)
        z4 = z3 + PP(0.876837, -2)
        c7 = z4 + PP(0.292287, 137)
        c8 = z4 + PP(0.170363, -41)
        z5 = z4 + PP(0.511486, -80)
        c9 = z5 + PP(0.170454, 65)
        c10 = z5 + PP(0.243356, -114)
        z6 = z5 + PP(0.730604, -146)
        #z6 = z7 - PP(1.00082, ta + 373)
        c11 = z6 + PP(0.243391, -16)
        c12 = z6 + PP(0.333566, 161)
        z7 = z6 + PP(1.00082, 109)
        c13 = z7 + PP(0.525879, -84)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            knot(*z6),
            controlcurve(c12, c13),
            #curve(),
            endknot(*z7)])

    @classmethod
    def path_erSWRCRCR(cls, ta=None, **kwargs):
        #M 319.568,269.27 C 324.5605,274.9043 317.787,290.244 313.156,289.003 311.991,288.669 311.758,286.874 312.121,285.818 313.032,283.316 317.24233,282.44848 319.80233,281.71448 320.60233,281.49948 321.68033,281.23648 322.28633,281.80148 322.64533,282.12448 322.71733,282.79448 322.51333,283.23248 322.23233,283.86348 321.45633,284.59248 320.79633,284.39048 319.89633,284.09848 319.95533,283.20948 319.82633,281.72548

        #z0 = P(0, -0)
        #c0 = P(1.76124, -1.98766)
        #c1 = P(-0.628297, -7.39916)
        #z1 = P(-2.26201, -6.96136)
        #c2 = P(-2.673, -6.84354)
        #c3 = P(-2.75519, -6.2103)
        #z2 = P(-2.62714, -5.83777)
        #c4 = P(-2.30576, -4.95512)
        #c5 = P(-0.820445, -4.64907)
        #z3 = P(0.0826664, -4.39014)
        #c6 = P(0.364889, -4.31429)
        #c7 = P(0.745183, -4.22151)
        #z4 = P(0.958966, -4.42083)
        #c8 = P(1.08561, -4.53477)
        #c9 = P(1.11101, -4.77114)
        #z5 = P(1.03905, -4.92565)
        #c10 = P(0.939916, -5.14826)
        #c11 = P(0.666161, -5.40543)
        #z6 = P(0.433328, -5.33417)
        #c12 = P(0.115828, -5.23116)
        #c13 = P(0.136641, -4.91754)
        z7 = P(0.0911331, -4.39402)

        #z0 = P(0, -0)
        #c0 = z0 + P(1.76124, -1.98766)
        #z1 = z0 + P(-2.26201, -6.96136)
        #c1 = z1 + P(1.63371, -0.437797)
        #c2 = z1 + P(-0.410986, 0.117828)
        #z2 = z1 + P(-0.365125, 1.1236)
        #c3 = z2 + P(-0.128058, -0.372533)
        #c4 = z2 + P(0.321381, 0.88265)
        #z3 = z2 + P(2.7098, 1.44763)
        #c5 = z3 + P(-0.903111, -0.258939)
        #c6 = z3 + P(0.282222, 0.0758472)
        #z4 = z3 + P(0.8763, -0.0306917)
        #c7 = z4 + P(-0.213783, 0.199319)
        #c8 = z4 + P(0.126647, -0.113947)
        #z5 = z4 + P(0.0800806, -0.504825)
        #c9 = z5 + P(0.0719667, 0.154517)
        #c10 = z5 + P(-0.0991306, -0.222603)
        #z6 = z5 + P(-0.605719, -0.408517)
        #c11 = z6 + P(0.232833, -0.0712611)
        #c12 = z6 + P(-0.3175, 0.103011)
        #z7 = z6 + P(-0.342194, 0.940153)
        #c13 = z7 + P(0.0455083, -0.523522)

        z0 = P(0, -0)
        c0 = z0 + PP(2.6557, -48)
        z1 = z0 + PP(7.31965, -108)
        c1 = z1 + PP(1.69136, -15)
        c2 = z1 + PP(0.427543, 164)
        z2 = z1 + PP(1.18143, 108)
        c3 = z2 + PP(0.393929, -108)
        c4 = z2 + PP(0.939338, 69)
        z3 = z2 + PP(3.07224, 28)
        c5 = z3 + PP(0.939499, -164)
        c6 = z3 + PP(0.292237, 15)
        z4 = z3 + PP(0.876837, -2)
        c7 = z4 + PP(0.292287, 137)
        c8 = z4 + PP(0.170363, -41)
        z5 = z4 + PP(0.511137, -80)
        c9 = z5 + PP(0.170454, 65)
        c10 = z5 + PP(0.243678, -114)
        z6 = z5 + PP(0.730604, -146)
        #z6 = z7 - PP(1.00049, ta + 375)
        c11 = z6 + PP(0.243494, -17)
        c12 = z6 + PP(0.333793, 162)
        z7 = z6 + PP(1.00049, 110)
        c13 = z7 + PP(0.525496, -85)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            knot(*z6),
            controlcurve(c12, c13),
            #curve(),
            endknot(*z7)])

    @classmethod
    def path_SWRCRCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SWRCRCRswl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCR(cls, ta=None, **kwargs):
        #M 225.442,143.114 C 231.226,140.039 241.822,135.845 241.822,129.37 241.822,126.402 232.64757,129.6931 231.97091,133.14378 231.60717,134.99866 234.42306,136.0923 236.33245,137.15571 237.46777,137.64799 238.27281,137.89093 238.27034,138.72137 238.26809,139.47715 237.18807,140.44449 236.49823,140.13575 235.59014,139.72934 235.23185,139.09704 236.33245,137.15571

        #z0 = P(0, -0)
        #c0 = P(2.04047, 1.08479)
        #c1 = P(5.7785, 2.56434)
        #z1 = P(5.7785, 4.84858)
        #c2 = P(5.7785, 5.89562)
        #c3 = P(2.54196, 4.7346)
        #z2 = P(2.30325, 3.51727)
        #c4 = P(2.17493, 2.86291)
        #c5 = P(3.16832, 2.4771)
        #z3 = P(3.84191, 2.10195)
        #c6 = P(4.24242, 1.92829)
        #c7 = P(4.52642, 1.84258)
        #z4 = P(4.52555, 1.54962)
        #c8 = P(4.52476, 1.283)
        #c9 = P(4.14375, 0.941744)
        #z5 = P(3.90039, 1.05066)
        #c10 = P(3.58004, 1.19403)
        #c11 = P(3.45364, 1.41709)
        z6 = P(3.84191, 2.10195)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.04047, 1.08479)
        #z1 = z0 + P(5.7785, 4.84858)
        #c1 = z1 + P(0, -2.28424)
        #c2 = z1 + P(0, 1.04704)
        #z2 = z1 + P(-3.47525, -1.33131)
        #c3 = z2 + P(0.238711, 1.21732)
        #c4 = z2 + P(-0.128319, -0.65436)
        #z3 = z2 + P(1.53865, -1.41532)
        #c5 = z3 + P(-0.67359, 0.375147)
        #c6 = z3 + P(0.400516, -0.173665)
        #z4 = z3 + P(0.683645, -0.55233)
        #c7 = z4 + P(0.000871361, 0.292961)
        #c8 = z4 + P(-0.00079375, -0.266622)
        #z5 = z4 + P(-0.625161, -0.498962)
        #c9 = z5 + P(0.24336, -0.108917)
        #c10 = z5 + P(-0.320354, 0.143372)
        #z6 = z5 + P(-0.0584835, 1.05129)
        #c11 = z6 + P(-0.388267, -0.684858)

        z0 = P(0, -0)
        c0 = z0 + PP(2.3109, 27)
        z1 = z0 + PP(7.54319, 39)
        c1 = z1 + PP(2.28424, -90)
        c2 = z1 + PP(1.04704, 90)
        z2 = z1 + PP(3.72152, -159)
        c3 = z2 + PP(1.24051, 78)
        c4 = z2 + PP(0.666823, -101)
        z3 = z2 + PP(2.09059, -42)
        c5 = z3 + PP(0.771012, 150)
        c6 = z3 + PP(0.436546, -23)
        z4 = z3 + PP(0.878885, -38)
        c7 = z4 + PP(0.292962, 89)
        c8 = z4 + PP(0.266624, -90)
        z5 = z4 + PP(0.799868, -141)
        #z5 = z6 - PP(1.05292, ta + 392)
        c9 = z5 + PP(0.266622, -24)
        c10 = z5 + PP(0.350973, 155)
        z6 = z5 + PP(1.05292, 93)
        c11 = z6 + PP(0.787262, -119)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            #curve(),
            endknot(*z6)])

    @classmethod
    def path_selNELCLCR(cls, ta=None, **kwargs):
        #M 231.22,460.584 C 237.17549,460.584 247.838,450.89682 247.838,444.42182 247.838,441.45382 238.72,444.76282 237.989,448.20182 237.628,450.05782 241.67505,451.85819 243.56805,452.95019 244.70705,453.43419 245.54605,453.65419 245.53105,454.48419 245.53105,455.24019 244.46005,456.21919 243.76905,455.91119 242.86805,455.49119 242.53105,454.88219 243.61305,452.93119

        #z0 = P(0, -0)
        #c0 = P(2.10096, -0)
        #c1 = P(5.86246, 3.41742)
        #z1 = P(5.86246, 5.70166)
        #c2 = P(5.86246, 6.7487)
        #c3 = P(2.64583, 5.58136)
        #z2 = P(2.38795, 4.36816)
        #c4 = P(2.2606, 3.7134)
        #c5 = P(3.68831, 3.07827)
        #z3 = P(4.35612, 2.69304)
        #c6 = P(4.75793, 2.52229)
        #c7 = P(5.05391, 2.44468)
        #z4 = P(5.04862, 2.15188)
        #c8 = P(5.04862, 1.88518)
        #c9 = P(4.6708, 1.53981)
        #z5 = P(4.42703, 1.64846)
        #c10 = P(4.10917, 1.79663)
        #c11 = P(3.99029, 2.01147)
        z6 = P(4.37199, 2.69974)

        #z0 = P(0, -0)
        #c0 = z0 + P(2.10096, 0)
        #z1 = z0 + P(5.86246, 5.70166)
        #c1 = z1 + P(0, -2.28424)
        #c2 = z1 + P(0, 1.04704)
        #z2 = z1 + P(-3.47451, -1.3335)
        #c3 = z2 + P(0.257881, 1.2132)
        #c4 = z2 + P(-0.127353, -0.654756)
        #z3 = z2 + P(1.96816, -1.67512)
        #c5 = z3 + P(-0.667808, 0.385233)
        #c6 = z3 + P(0.401814, -0.170744)
        #z4 = z3 + P(0.692503, -0.541161)
        #c7 = z4 + P(0.00529167, 0.292806)
        #c8 = z4 + P(0, -0.2667)
        #z5 = z4 + P(-0.621594, -0.503414)
        #c9 = z5 + P(0.243769, -0.108656)
        #c10 = z5 + P(-0.317853, 0.148167)
        #z6 = z5 + P(-0.0550333, 1.05128)
        #c11 = z6 + P(-0.381706, -0.688269)

        z0 = P(0, -0)
        c0 = z0 + PP(2.10096, 0)
        z1 = z0 + PP(8.17786, 44)
        c1 = z1 + PP(2.28424, -90)
        c2 = z1 + PP(1.04704, 90)
        z2 = z1 + PP(3.72162, -159)
        c3 = z2 + PP(1.24031, 77)
        c4 = z2 + PP(0.667026, -101)
        z3 = z2 + PP(2.58451, -40)
        c5 = z3 + PP(0.770956, 150)
        c6 = z3 + PP(0.436587, -23)
        z4 = z3 + PP(0.878872, -38)
        c7 = z4 + PP(0.292853, 88)
        c8 = z4 + PP(0.2667, -90)
        z5 = z4 + PP(0.799878, -140)
        #z5 = z6 - PP(1.05272, ta + 391)
        c9 = z5 + PP(0.266889, -24)
        c10 = z5 + PP(0.35069, 155)
        z6 = z5 + PP(1.05272, 92)
        c11 = z6 + PP(0.787029, -119)

        return pyx.metapost.path.path([
            beginknot(*z0),
            controlcurve(c0, c1),
            knot(*z1),
            controlcurve(c2, c3),
            knot(*z2),
            controlcurve(c4, c5),
            knot(*z3),
            controlcurve(c6, c7),
            knot(*z4),
            controlcurve(c8, c9),
            knot(*z5),
            controlcurve(c10, c11),
            #curve(),
            endknot(*z6)])

    @classmethod
    def path_NELCLCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_NELCLCRswl(cls, ta=None, **kwargs):
        pass

