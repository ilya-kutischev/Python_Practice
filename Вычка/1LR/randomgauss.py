import random
import math

u = random.random()
v = random.random()

w = math.sin(2*math.pi*v)*(-2*math.log(u))**(0.5)
print(w)