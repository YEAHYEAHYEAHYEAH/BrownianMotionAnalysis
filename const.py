import math as mmmmm

frames = [2738,2737,2730,3738]

kb = 1.38064852*10**(-23.0)
T = 296
n = 8.9*10**(-4.0)
p = 4.0*kb*T/(6.0*mmmmm.pi*n)

ppm = (1/2.53)*10**(-6.0)
frr = sum(frames)/(len(frames)*120)

con = ppm**2.0*frr

