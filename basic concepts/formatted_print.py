from math import sin
real = 12.89643
integer = 42
string = 'some message'
print ('real=%.3f, integer=%d, string=%s' % (real, integer, string))
print ('real=%9.3e, integer=%5d, string=%s' % (real, integer, string))
t0 = 2
dt = 0.55
# Unformatted print
t = t0 + 0*dt; g = t*sin(t)
print (t, g)
t = t0 + 1*dt; g = t*sin(t)
print (t, g)
t = t0 + 2*dt; g = t*sin(t)
print (t, g)
t0 = 2
dt = 0.55
# Formatted print
t = t0 + 0*dt; g = t*sin(t)
print ('%6.2f %8.3f' % (t, g))
t = t0 + 1*dt; g = t*sin(t)
print ('%6.2f %8.3f' % (t, g))
t = t0 + 2*dt; g = t*sin(t)
print ('%6.2f %8.3f' % (t, g))