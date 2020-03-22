import numpy as np
import matplotlib.pyplot as mpl
#%matplotlib inline
import Libreria_Complejos as lc
import Libreria_Vectores_y_Matrices as lvm

def impresion_grafica(V, c):    # V = Vector final, c = Número de clics
    print("Vector de estado final: ", V)
    x = []
    y = []
    for i in range(len(V)):
        x.append("Punto " + str(i))
        y.append(V[i][0][0])
    index = np.arange(len(V))
    mpl.bar(x, y)
    mpl.xlabel('Estado')
    mpl.ylabel('Probabilidad')
    mpl.xticks(index, x, rotation = 30)
    mpl.title('Evolución dinámica del sistema después de ' + str(c) + ' clics de tiempo.')
    #print("Eje x:", x)
    #print("Eje y:", y)
    return mpl.show()

def impresion_grafica_cuantica(V, c):    # V = Vector final, c = Número de clics
    print("Vector de estado final: ", V)
    x = []
    y = []
    for i in range(len(V)):
        x.append("Punto " + str(i))
        y.append(lc.modulo(V[i][0])**2)
    index = np.arange(len(V))
    mpl.bar(x, y)
    mpl.xlabel('Estado')
    mpl.ylabel('Probabilidad')
    mpl.xticks(index, x, rotation = 30)
    mpl.title('Evolución dinámica del sistema después de ' + str(c) + ' clics de tiempo.')
    #print("Eje x:", x)
    #print("Eje y:", y)
    return mpl.show()

def potencia_matriz(M, n): # n = Potencia
    for i in range(n+1):
        rta = M
        if n >= 1:
            i = 2
            while i <= n:
                rta = lvm.producto_matricial(rta, M)
                i += 1
    return rta

def main():
    M1 = [[[0, 0], [0, 0], [0, 0], [0, 0]],
          [[0, 0], [0, 0], [0, 0], [1, 0]],
          [[0, 0], [1, 0], [1, 0], [0, 0]],
          [[1, 0], [0, 0], [0, 0], [0, 0]]]

    V1 = [[[1, 0]],
          [[0, 0]],
          [[0, 0]],
          [[0, 0]]]
    
    c = 5
    for i in range(c + 1):
        caux = i
        if caux == 0:
            impresion_grafica(V1, caux)
        else:
            V_rta = lvm.accion_mc_vc(potencia_matriz(M1, caux), V1)
            impresion_grafica(V_rta, caux)

main()
