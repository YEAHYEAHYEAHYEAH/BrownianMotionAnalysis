import csv
import glob
import matplotlib.pyplot as plot

badelements = [8,7,6,5,4,3]

alllists =[]
timelist =[]
averages =[]
r2averages = []

def difference(particle,time):
    initialX = float(particle[0][1])
    initialY = float(particle[0][2])
    initialt = float(particle[0][0])
    dX = float(particle[time][1])-initialX
    dY = float(particle[time][2])-initialY
    dt = float(particle[time][0])-initialt
    return (dX,dY,dt)

def rsqrd (centre):
    rsqrd = centre[0]**2 + centre[1]**2
    return rsqrd

def average(dlist):
    average = float(sum(dlist))/float(len(dlist))
    return average

for frame in range(1,3000):
    averages.append([])


for file in glob.glob('/home/s1539149/Documents/Year3Experiment1/goodtracks/20/*.csv'):
    with open(file, 'rb' ) as f:
        reader = csv.reader(f)
        next(reader, None)
        temp = list(reader)
        for i  in temp:
            for j in badelements:
                del i[j]
        alllists.append(temp)

for particle in alllists:
    for frame in range(0, len(particle)):
        r2 = rsqrd(difference(particle,frame))
        t = difference(particle,frame)[2]
        averages[int(t)].append(r2)

dellist = []
for t in averages:
    if len(t) > 0:
        r2averages.append(average(t))

    if len(t) == 0:
        dellist.append(t)



timelist = range(0, len(r2averages))

functionsman = plot.plot(timelist,r2averages)
