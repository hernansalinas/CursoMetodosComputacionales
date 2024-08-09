import numpy as np
import matplotlib.pyplot as plt

def fun(t, y, λ):
    return -λ*y

def evolve(f, t, NumT,y0, deltaT, λ):
  y = np.zeros(NumT)
  y[0] = y0
  for i in range(1, NumT):
    y[i] = y[i-1] + deltaT*f(t[i-1], y[i-1], λ)
  return y

def euler(fun,ta,tb,dt,y0,λ):  
  NumT=int((tb-ta)/dt)
  t = np.linspace(ta, tb, NumT)
  y = evolve(fun, t, NumT,y0, dt, λ)
  return t,y 