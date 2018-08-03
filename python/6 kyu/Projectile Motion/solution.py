from math import sin, cos, pi, sqrt

class Projectile:
    def __init__(self, h0, v0, a):
        self.h0 = float(h0)
        self.v0 = float(v0)
        self.a = float(a)*pi/180 #in rads
    
    def height_eq(self):
        result = "h(t) = -16.0t^2"
        if sin(self.a)*self.v0 != 0 :
            result += " + " + str(float(format(sin(self.a)*self.v0, '.3f')))+"t"
        if self.h0 != 0 :
            result += " + " + str(float(format(self.h0, '.1f')))
        return result
    
    def horiz_eq(self):
        result = "x(t) = "
        if cos(self.a)*self.v0 == 0 :
            result += "0"
        else :
            result += str(float(format(cos(self.a)*self.v0, '.3f')))+"t"
        return result


    def height(self, t):
        result = -16*t*t+sin(self.a)*self.v0*t+self.h0
        return float(format(result, '.3f'))
    
    def horiz(self, t):
        result = cos(self.a)*self.v0*t
        return float(format(result, '.3f'))
    
    def landing(self):
        t1 = (self.v0 * sin(self.a) - sqrt((self.v0 * sin(self.a))**2 + 4 * 16 * self.h0)) / (2 * 16)
        t2 = (self.v0 * sin(self.a) + sqrt((self.v0 * sin(self.a))**2 + 4 * 16 * self.h0)) / (2 * 16)
        t = t1 if t1 > 0 else t2
        x = cos(self.a) * self.v0 * t
        result = [ float(format(x, '.3f')), 0, float(format(t, '.3f')) ]
        return result



def testing(value1, value2):
    if (value1 == value2):
        print "Yep!"
    else:
        print "Nah."

p = Projectile(5, 2, 45)
testing(p.height_eq(), "h(t) = -16.0t^2 + 1.414t + 5.0")
testing(p.horiz_eq(), "x(t) = 1.414t")
testing(p.height(0.2), 4.643)
testing(p.horiz(0.2), 0.283)
testing(p.landing(), [0.856, 0, 0.605])