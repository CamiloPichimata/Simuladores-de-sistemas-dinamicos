# Librería No. 2: Vectores y Matrices

import Libreria_Complejos as LC
import math

def adicion_vectores_complejos(vc_1, vc_2):    # vc_n = Vector Complejo No. n
    """
    La función recibe 2 vectores de números complejos y retorna su suma componente a componente.
    """
    return adicion_matrices_complejas(vc_1, vc_2)

def inverso_aditivo_vc(vc_1):
    """
    La función recibe un vector de números complejos y multiplica por (-1) la parte real y la parte imaginaria de cada uno de los complejos que conforman el vector.
    """
    return inverso_aditivo_mc(vc_1)

def mult_escalar_vector(e, vc_1):
    """
    La función recibe un número escalar complejo y un vector de números complejos, luego retorna el producto o multiplicación de dicho escalar por cada una de las componentes del vector recibido.
    """
    vc_1 = mult_escalar_matriz(e, vc_1)
    return vc_1

def adicion_matrices_complejas(mc_1, mc_2):    # mc_n = Matriz Compleja No. n
    """
    La función recibe dos matrices del mismo tamaño y devuelve su suma componente a componente.
    """
    if len(mc_1)==len(mc_2) and len(mc_1[0])==len(mc_2[0]):
        rta = crear_matriz(mc_1, mc_2)
        for i in range(len(mc_1)):  #Filas matriz 1
            for j in range(len(mc_2[0])):  #Columnas matriz 2
                rta[i][j] = LC.suma(mc_1[i][j], mc_2[i][j])
        return rta
    else:
        return "Las matrices no tienen el mismo tamaño"

def inverso_aditivo_mc(mc_1):
    """
    La función recibe una matriz de números complejos y multiplica por (-1) la parte real y la parte imaginaria de cada una de las posiciones que conforman la matriz original.
    """
    for i in range(len(mc_1)):  #Filas
        for j in range(len(mc_1[0])):  #Columnas
            mc_1[i][j] = [mc_1[i][j][0] * -1, mc_1[i][j][1] * -1]
    return mc_1

def mult_escalar_matriz(e, mc_1):    # e = escalar
    """
    La función recibe un número escalar complejo y una matriz de números complejos, luego retorna el producto o multiplicación de dicho escalar por cada una de las posiciones de la matriz recibida.
    """
    for i in range(len(mc_1)):  #Filas
        for j in range(len(mc_1[0])):  #Columnas
            mc_1[i][j] = LC.producto(mc_1[i][j], e)
    return mc_1

def transpuesta(mvc_1):    # mvc = Matriz o Vector de Complejos
    """
    La función recibe una matriz o un vector de números complejos, y retorna su transpuesta.
    """
    rta = crear_matriz1(len(mvc_1[0]), len(mvc_1))
    for i in range (len(mvc_1[0])):
        for j in range (len(mvc_1)):
            rta[i][j] = mvc_1[j][i]
    return rta

def conjugada_mv(mvc_1):
    """
    La función recibe un vector o una matriz de números complejos, y retorna su conjugado(a).
    """
    for i in range(len(mvc_1)):
        for j in range(len(mvc_1[0])):
            mvc_1[i][j] = LC.conjugado(mvc_1[i][j])
    return mvc_1

def adjunta(mvc_1):
    """
    La función recibe un vector o una matriz de números complejos, y retorna su adjunta.
    """
    rta = transpuesta(mvc_1)
    rta = conjugada_mv(rta)
    return rta


def producto_matricial(mc_1, mc_2):
    "La función recibe dos matrices (con tamaños compatibles) y devuelve su producto."

    if len(mc_1[0]) == len(mc_2):
        rta = crear_matriz(mc_1, mc_2)
        for i in range(len(mc_1)):  # Filas matriz 1
            for j in range(len(mc_2[0])):  # Columnas matriz 2
                for k in range(len(mc_1[0])):
                    rta[i][j] = LC.suma(rta[i][j], LC.producto(mc_1[i][k], mc_2[k][j]))
        return rta
    else:
        return "El tamaño de las matrices no es el apropiado"

def accion_mc_vc(mc_1, vc_1):
    """
    La función recibe una matriz y un vector de números complejos, luego calcula la acción de dicha matriz sobre el vector recibido.
    """
    return producto_matricial(mc_1,vc_1)

def prod_interno_v(vc_1, vc_2):
    """
    La función recibe dos vectores de números complejos, y retorna el producto entre la adjunta del primer vector y el segunto vector.
    """
    rta = producto_matricial(adjunta(vc_1), vc_2)
    return rta

def norma_v(vc_1):
    """
    La función recibe un vector de números complejos y retorna su norma o magnitud.
    """
    rta = prod_interno_v(vc_1, vc_1)
    return math.sqrt(rta[0][0][0])

def distancia_2v(vc_1, vc_2):
    """
    La función recibe dos vectores complejos y retorna la distancia que existe entre cada uno de los vectores.
    """
    rta = adicion_vectores_complejos(vc_1, inverso_aditivo_vc(vc_2))
    return norma_v(rta)

def mc_es_unitaria(mc_1):
    """
    La función recibe una matriz cuadrada y decide si es o no una matriz unitaria.
    """
    if len(mc_1) == len(mc_1[0]):
        mc_1t = adjunta(mc_1)
        aux = producto_matricial(mc_1, mc_1t)
        identidad = matriz_identidad(len(mc_1))
        for i in range(len(mc_1)):
            for j in range(len(mc_1)):
                for k in range(2):
                    if round(aux[i][j][k]) != identidad[i][j][k]:
                        return False
        return True
    else:
        return "Las matriz no es cuadrada"

def mc_es_hermitiana(mc_1):
    """
    La función recibe una matriz cuadrada y decide si es o no una matriz hermitiana.
    """
    if len(mc_1) == len(mc_1[0]):
        mc_1t = crear_matriz1(len(mc_1), len(mc_1))
        mc_1t = adjunta(mc_1)
        for i in range(len(mc_1)):
            for j in range(len(mc_1)):
                for k in range(2):
                    if mc_1[i][j][k] != mc_1t[i][j][k]:
                        return False
        return True
    else:
        return "Las matrices no son cuadradas"

def prod_tensor(mc_1, mc_2):
    """
    La función recibe 2 matrices de números complejos (sin importar sus tamaños) y retorna su producto tensor.
    """
    rta = crear_matriz1(len(mc_1)*len(mc_2), len(mc_1[0])*len(mc_2[0]))
    for i in range(len(rta)):
        for j in range(len(rta[0])):
            rta[i][j] = LC.producto(mc_1[i//len(mc_2[0])][j//len(mc_2[0])], mc_2[i%len(mc_2)][j%len(mc_2)])
    return rta

def crear_matriz(m_1, m_2):
    """
    La función recibe dos matrices e inicializa una nueva copuesta de ceros, es decir, de la sigueinte manera: [0,0].
    """
    matriz = []
    filas = len(m_1)
    columnas = len(m_2[0])
    for i in range(filas):
        matriz.append([[0, 0]] * columnas)
    return matriz

def crear_matriz1(filas, columnas):
    """
    La función recibe el número de filas y el número de columnas e inicializa una matriz compuesta de ceros, es decir, de la siguente manera: [0,0].
    """
    matriz = []
    for i in range(filas):
        matriz.append([[0,0]] * columnas)
    return matriz

def matriz_identidad(tamano):
    """
    La función recibe el támaño de una matriz cuadrada y genera la matriz identidad con dichas dimensiones.
    """
    identidad = crear_matriz1(tamano, tamano)
    for i in range(len(identidad)):
        for j in range(len(identidad)):
            if i == j:
                identidad[i][j] = [1,0]
            else:
                identidad[i][j] = [0,0]
    return identidad
