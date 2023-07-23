import cv2
import numpy as np
import math
import random


class Recorder:
    def __init__(self, size, fn) -> None:
        fouracc = cv2.VideoWriter_fourcc(*"mp4v")
        self.writer = cv2.VideoWriter(fn, fouracc, 30, (size,size), False)
    def add_frame(self, frame):
        self.writer.write(frame)

class Particle:
    def __init__(self,x,y,z) -> None:
        self.pos = np.array([x,y,z])
        self.orig_pos = self.pos.copy()
        self.target = np.array([0,0,0])
    def __repr__(self) -> str:
        return f"<Particle> {self.pos[0]:.2f} {self.pos[1]:.2f} {self.pos[2]:.2f}"
    def get_coords(self):
        return self.pos
    def set_target(self,x,y,z):
        self.target = np.array([x,y,z])
    def step(self, step_size):
        tmp = (self.target - self.pos)
        norm = np.linalg.norm(tmp)
        step_v = tmp*(step_size/norm)
        self.pos += step_v
        if norm < 2:
            self.target = self.orig_pos.copy()
    def randomize(self, step=1):
        for i in range(len(self.pos)):
            self.pos[i] += (random.random()-0.5)*step

d_alpha = 3
d_beta = 3
r = 75
c = (0, 0, 200)

# Camera model
# Extrinsic
R = np.eye(3)
t = np.zeros((3,1))
ex = np.array([[0,0,0,1]])
RT = np.concatenate((R, t), axis=1)
RT = np.concatenate((RT, ex), axis=0)
print(f"Extrinsics:\n{RT}")
# Intrinsic
f = 700
x0 = 400
y0 = 400
K = np.array([[f, 0, x0], [0, f, y0], [0, 0, 1]])
print(f"Intrinsic:\n{K}")


# Generate the object
particles = []
min_z = 100000
max_z = 0
for alpha in range(0,360,d_alpha):
    for beta in range(-90,90,d_beta):
        x = r * math.sin(math.radians(beta)) + c[0]
        y = r * math.cos(math.radians(beta)) * math.cos(math.radians(alpha)) + c[1] + (random.random()-0.5)*1
        z = r * math.cos(math.radians(beta)) * math.sin(math.radians(alpha)) + c[2] + (random.random()-0.5)*1
        particle = Particle(x,y,z)
        
        if x < 0 and y < 0:
            particle.set_target(-50,50,250)
        elif x < 0 and y > 0:
            particle.set_target(50,50,250)
        elif x > 0 and y > 0:
            particle.set_target(50,-50,200)
        elif x > 0 and y < 0:
            particle.set_target(30,50,200)
        
        
        
        particles.append(particle)

        if z < min_z:
            min_z = z
        if z > max_z:
            max_z = z

print(f"min {min_z} max {max_z}")



IM_SIZE = 1000
rec = Recorder(IM_SIZE, "output.mp4")

for i in range(0,330):
    img = np.zeros((IM_SIZE,IM_SIZE), dtype=np.uint8)

    # Draw scene
    for particle in particles:
        xyz = particle.get_coords()
        if i >= 25 or i <= 225:
            particle.step(1)
            particle.randomize(0.1)
        uv = K@xyz
        uv = [uv[0]/uv[2], uv[1]/uv[2]]
        #color = int((xyz[2]-50.0)/(max_z-50.0)*255)
        color = 255
        img[int(uv[1]), int(uv[0])] = color
    
    #rec.add_frame(img)
    cv2.imshow("out", img)
    cv2.waitKey(1)
    print(i)








