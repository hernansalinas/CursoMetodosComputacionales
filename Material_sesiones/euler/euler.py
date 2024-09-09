import evolve 
import numpy as np

def fun(t, y, λ):
    return -λ*y

ta = 0.
tb = 100.
dt = 0.01
y0 = 100. # Condiciones inicial 
λ = 0.1 

t,y = evolve.euler(fun,ta,tb,dt,y0,λ)
data = np.array([t,y])
np.savetxt(f"data/decaimiento_{λ}", data)