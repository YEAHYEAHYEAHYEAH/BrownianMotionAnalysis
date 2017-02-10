import numpy as np
import csv
import math
import matplotlib.pyplot as plot
import glob
import pylab as plt
import const
import AVERAGEimport as AVG

coeffs = []
coefferrors = []
rsqrd = []

radii = []

def plotter(file):
    alltracks = np.genfromtxt (file, delimiter=",",skip_header=1)
    x = np.array(alltracks[:,1])
    x = x - x[0]

    y = np.array(alltracks[:,2])
    y = y - y[0]

    frames = alltracks[:,8]
    frames = frames - frames[0]
    rsquared = x**2+y**2
    rsqrd.append(rsquared)
 
    coeff = np.array(np.polyfit(frames,rsquared,1,))
    coefferror = np.trace(np.cov(frames**(1.0/2.0),rsquared**(1.0/2.0)))  
    coefferror = coefferror/frames.size


    if coeff[0]>0:
        coeffs.append(coeff[0])
        radii.append(const.p/(const.con*coeff[0]))
        coefferrors.append(coefferror)
        
    return frames,rsquared,coeff

for file in glob.glob('/home/s1539149/Documents/Year3Experiment1/goodtracks/20/*.csv'):
    plotter(file)

avcoeff = sum(coeffs)/len(coeffs)
avradius = sum(radii)/len(radii)
avcoefferror = sum(coefferrors)/len(coefferrors)

print avcoeff
print avradius
print avcoefferror
avSTUFF = [avcoeff,avcoefferror,avradius]
x = []
y = []


for i in range(0,2200):
    yo = avcoeff * i
    y.append(yo)
    x.append(i)

x2 = []
y2 = []
for i in range(0,2200):
    yo2 = avcoeff * i -AVG.r2averages[i]
    y2.append(yo2)
    x2.append(i)


AVG.Plotter
plot.plot(x,y)
plot.show()
plt.show()

with open('video20.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(x)
    wr.writerow(y)
    wr.writerow(x2)
    wr.writerow(y2)
    wr.writerow(AVG.timelist)
    wr.writerow(AVG.r2averages)
    wr.writerow(coeffs)
    wr.writerow(coefferrors)
    wr.writerow(avSTUFF)
