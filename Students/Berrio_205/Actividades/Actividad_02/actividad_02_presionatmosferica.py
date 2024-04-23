pa = 101325 # Presión atmosférica en Pascales (N/m**2). 
g = 9.81  # Gravedad en m/s**2.
rho = 997 # Densidad del agua en kg/m**3

p = lambda z: (pa + rho * g * z) / pa  # Presión normalizada a múltiplos de 1 atmosfera. 

Z_ = np.linspace(0,30,10)
P_ = p(Z_)

plt.figure(figsize=(6,4))
plt.plot(Z_,P_,"--*", label= ('$P_{30m} = $', round(P_[-1]),'atm'))
plt.xlabel("Profundidad (m)", fontsize=14)
plt.xticks(fontsize=14)
plt.ylabel("Presión (atm)", fontsize=14)
plt.yticks(fontsize=14)
plt.title('Relación presión vs profundidad')
plt.grid()
plt.legend()
plt.show()
