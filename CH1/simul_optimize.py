#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel
class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles
    def evolve_fast(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        
        for p in self.particles:
            t_x_ang = timestep* p.ang_vel
            for i in range(nsteps):
                norm = (p.x**2+p.y**2)**0.5
                p.x, p.y = (p.x - t_x_ang*p.y/norm,
                           p.y + t_x_ang*p.x/norm)
                              
                #重複


# In[19]:


import matplotlib.pyplot as plt
from matplotlib import animation
def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]
    fig = plt.figure()
    ax = plt.subplot(111, aspect = "equal")
    line, = ax.plot(X ,Y ,"ro") #此逗號不可少
    
    #指定坐標軸範圍
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    
    def init():
        line.set_data([], [])
        return line,
    def animate(i):
        #粒子移動0.01個時間單位
        simulator.evolve_fast(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
      
        line.set_data(X, Y)
        return line,
    anim = animation.FuncAnimation(fig = fig,
                               func = animate,
                              init_func= init,
                              blit = True,
                              interval = 10)
    return anim


# In[20]:


def test_visualize():
    particles = [Particle(0.3, 0.5, 1),
                Particle(0.0, -0.5, -1),
                Particle(-0.1, -0.4, 3)]
    simulator = ParticleSimulator(particles)
    visualize(simulator)
if __name__ == "__main__":
    test_visualize()


# In[ ]:


def test_evolve():
    particles = [Particle(0.3, 0.5, +1),
                Particle(0.0, -0.5, -1),
                Particle(-0.1, -0.4, +3)]
    simulator = ParticleSimulator(particles)
    
    simulator.evolve_fast(0.1)
    
    p0, p1, p2 = particles
    def fequal(a, b, eps = 1e-5):
        return abs(a - b) < eps
    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)
    
    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)
    
    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)
if __name__ == "__main__":
    test_visualize()    
    


# In[ ]:


from random import uniform
def benchmark():
    particles = [Particle(uniform(-1.0, 1.0),
                         uniform(-1.0, 1.0),
                         uniform(-1.0, 1.0))
                for i in range(1000)]
    simulator = ParticleSimulator(particles)
    simulator.evolve_fast(0.1)
if __name__ == "__main__":
    benchmark() 


# In[ ]:





# In[ ]:





# In[ ]:




