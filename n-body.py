#!/usr/bin/env python3
#
# n-body.py Solve the n-body problem using Newton
# 
# Copyright (C) 2019  Victor De la Luz (vdelaluz@enesmorelia.unam.mx)
#                      
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

G=6.674e-11         #m^3kg^-1s^-2

class Particle:
    
    def __init__(self, p, v, m, dt=1):
        self.p = p #position
        self.v = v #velocity
        self.m = m #mass
        self.dt = dt
        self.trajectory = [p]
        self.time = [0.0]

    def setdt(self,dt):
        self.dt = dt

    def computeR(self,p1):
        r = math.sqrt( (p1[0]-self.p[0])**2 + (p1[1]-self.p[1])**2 + (p1[2]-self.p[2])**2)
        return r

    def computeU(self,p1):
        u=[0,0,0]
        i=0
        for a,b in zip(self.p,p1):
            u[i] = b - a
            i+=1
        return u
    
    #def integrate(self,dt,p1,m1):
    def integrate(self,B):
        r = self.computeR(B.p)
        u = self.computeU(B.p)

        Vx=(G*B.m*self.dt/(r**3))*u[0]
        Vy=(G*B.m*self.dt/(r**3))*u[1]
        Vz=(G*B.m*self.dt/(r**3))*u[2]

        
        self.v[0] += Vx
        self.v[1] += Vy
        self.v[2] += Vz
        
        self.p = [self.p[0]+ (self.v[0]) *dt,self.p[1]+ (self.v[1])*dt,self.p[2]+ (self.v[2])*dt]

    def getPosition(self):
        return self.p

    def getVelocity(self):
        return self.v

    def getKineticEnergy(self):
        k= (1/2)*self.m*(math.sqrt( self.v[0]^2 +self.v[1]^2+self.v[2]^2))
        return k    

    #def integrate(self,dt,p1,m1):
    def computeV(self,B):
        r = self.computeR(B.p)
        u = self.computeU(B.p)

        Vx=(G*B.m*self.dt/(r**3))*u[0]
        Vy=(G*B.m*self.dt/(r**3))*u[1]
        Vz=(G*B.m*self.dt/(r**3))*u[2]
        #print(u)
        #print(r)
        #print((G*B.m/(r**3))*u[0],(G*B.m/(r**3))*u[1],(G*B.m/(r**3))*u[2])         
        return [Vx,Vy,Vz]


    #def integrate(self,dt,p1,m1):
    def updateV(self,v):
        self.v[0] += v[0]
        self.v[1] += v[1]
        self.v[2] += v[2]
        
    #def integrate(self,dt,p1,m1):
    def updatePosition(self,time,save):        
        self.p = [self.p[0]+ (self.v[0]) *dt,self.p[1]+ (self.v[1])*dt,self.p[2]+ (self.v[2])*dt]
        if save:
            self.time.append(time)
            self.trajectory.append(self.p)


    def getTrajectory(self):
        return self.time, self.trajectory
        
class Potential:
    
    def __init__(self, system, dt):
        self.system = system #set of Particles
        self.dt = dt #set of Particles

    def integrate(self,time,save):
        print(time/3600.0/24.0)
        for particle in self.system:
            for other in self.system:
                if other != particle:
                    velocity = particle.computeV(other)
                    particle.updateV(velocity)
        for particle in self.system:
            particle.updatePosition(time,save)

        return self.system

'''lenTime=3600.0*24*30  #sec
dt=1.0      #sec  '''  
lenTime=77474 #0.762 dias * 24horas * 60min * 60seg deberia dar una vuelta despues de este tiempo
dt=0.5

'''sun = Particle([0,0,0],[0,0,0], 2e30)
mercury = Particle([0,5.7e10,0],[47000,0,0], 3.285e23)
venus = Particle([0, 1.1e11, 0], [35000,0,0], 4.8e24)
earth = Particle([0, 1.5e11, 0], [30000, 0, 0], 6e24)
mars = Particle([0.0, 2.2e11,0.0],[24000.0,0.0,0.0],2.4e24)
jupiter=Particle([0.0, 7.7e11, 0.0] ,[13000, 0.0, 0.0],1e28) 
saturn = Particle([0,1.4e12,0], [9000,0,0],5.7e26)
uranus = Particle([0,2.8e12,0], [6835,0,0], 8.7e25)
neptune = Particle([0,4.5e12,0], [5477,0,0],1e26)
pluto = Particle ([0,3.7e12,0], [4748,0,0],1.3e22)'''
Urano = Particle([0,0,0],[0,0,0],8.681e25)
cordelia = Particle([0,4.98e4,0],[10810,0,0],0.044e18)
cressida = Particle([0,6.18e7,0],[9686,0,0],0.34e18)
#desdemona = Particle([0,6.27e7,0],[9619,0,0],0.18e18)
#juliet = Particle([0,6.43e7,0],[9500,0,0],0.56e18)
cupid = Particle([0,7.5e7,0],[8825,0,0],0.0038e18)
puck = Particle([0,8.6e7,0],[8207,0,0],2.9e18)
mab = Particle([0,9.77e7,0],[7700,0,0],0.01e18)
n_steps = int(lenTime/dt)


#p0=[0.001, 0.0, 0.0]  #m
#v0=[0.0, 0.0, 0.0]  #m/s
#m=1e1               #kg

#p1=[0.0, 0.0, 0.0]  #m
#v1=[0.0, 0.0, 1e-3]  #m/s
#m1=1e1               #kg

#A = Particle(p0,v0,m)
#B = Particle(p1,v1,m1)
#C = Particle( [0.0, 0.001, 0.0] , [0.0,0.0,0.0], 1e1)

#particles = [sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,pluto]
#particles = [sun,earth]
particles=[Urano,cordelia]

twoBody = Potential(particles,dt)

x=[]
y=[]


skip=0
save=False
for t in range(1,n_steps):
    if skip == 1000:
        skip=0
        save=True
    system = twoBody.integrate(float(t)*dt,save)
    save=False
    skip += 1

#B.setdt(dt)
#x=[]
#y=[]
#v=[]
#a=[]
#x.append(0.0)
##y.append(B.getPosition()[0])
#y.append(B.getPosition())
#v.append(B.getVelocity()[0])
#
#print(B.getVelocity()[0])
#
#a.append(0.0)
#v1=B.getVelocity()[0]
##lastX = B.getPosition()[0]
#
##for t in range(1,100):
##    lastX = B.getPosition()[0]
##    lastV = v1
##    B.integrate(A)
##    print(B.getPosition())
##    x.append(float(t)*dt)
##    y.append(B.getPosition()[0])
##    v1=(B.getPosition()[0]-lastX)/B.dt
##    print(v1)
##    v.append(v1)
##    a.append((v1-lastV)/B.dt)
#
#for t in range(1,100):
#    B.integrate(A)
#    x.append(float(t)*dt)
#    y.append(B.getPosition())

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

i=0
c=['g','r','b','g','r','b','g','r','b','g','r','b']
for particle in particles:
    time, trajectory = particle.getTrajectory()
    for x, y in zip(time,trajectory):
        ax.scatter(y[0], y[1], y[2], marker='o',c=c[i])
        #ax.scatter(y[0], y[1], y[2], c=c[i])
    i=i+1


# stack the plots
#lns = []
#for i in range(len(t)):
#    ln1, = ax.plot(y0[:i], y1[:i], z1[:i], 'o-', color='steelblue')
#    ln2, = ax.plot(x2[:i], y2[:i], z2[:i], 'o-', color='darkorange')
#    lns.append([ln1, ln2])

#line_ani = animation.ArtistAnimation(fig, lns, interval=100, blit=True)

    
#for point in y:
#    ax.scatter(point[0], point[1], point[2], marker='o')

#pointA=A.getPosition()
#ax.scatter(pointA[0], pointA[1], pointA[2], marker='o')

    
#fig, ax = plt.subplots(3)    
#ax[0].plot(x,y)
#ax[0].set(xlabel='time [sec]', ylabel='distance [km]',
#           title="n-body")
#ax[0].grid()
#
#ax[1].plot(x,v)
#ax[1].set(xlabel='time [sec]', ylabel='velocity [km/s]')
#ax[1].grid()
#
#ax[2].plot(x,a)
#ax[2].set(xlabel='time [sec]', ylabel='acceleration [km/s^2]')
#ax[2].grid()



plt.show()



