import math

def suma(c_1, c_2):
    """
    La funsión suma recibe dos números complejos: c_1 y c_2 (Que deben ser listas de longitud 2) y retorna un complejo
    (lista con longitud 2) correspondiente a la operación c_1 + c_2.
    """
    return [c_1[0] + c_2[0], c_1[1] + c_2[1]]

def resta(c_1, c_2):
    """
    La funsión suma recibe dos números complejos, c_1 y c_2 (Que deben ser listas de longitud 2) y retorna un complejo
    (lista con longitud 2) correspondiente a la operación c_1 - c_2.
    """
    return [c_1[0] - c_2[0], c_1[1] - c_2[1]]

def producto(c_1, c_2):
    """
    La funsión producto recibe 2 números complejos, c_1 y c_2 (Que deben ser listas de longitud 2) y retorna un complejo
    (lista con longitud 2) correspondiente a la operación c_1 * c_2.
    """
    return [c_1[0] * c_2[0] - c_1[1] * c_2[1] , c_1[0] * c_2[1] + c_1[1] * c_2[0]]


def division(c_1, c_2):
    """
    La funsión division recibe 2 números complejos, c_1 y c_2 (Que deben ser listas de longitud 2) y retorna un complejo
    (lista con longitud 2) correspondiente a la operación c_1 / c_2.
    """
    a = producto(c_1, conjugado(c_2))
    b = producto(c_2, conjugado(c_2))
    #print(a, "/", b)
    return [a[0] / b[0], a[1] / b[0]]

def conjugado(c_1):
    """
    La función conjugado recibe un número complejo, c_1 (que debe ser una lista de longitud 2) y retorna este mismo número,
    pero con signo opuesto en la parte imaginaria.

    """
    return [c_1[0], c_1[1] * -1]

def modulo(c_1):
    """
    La funsión modulo recibe un número complejo, c_1 (que debe ser una lista de longitud 2) y retorna un número de tipo real.
    """
    rta = math.sqrt(c_1[0] ** 2 + c_1[1] ** 2)
    return rta

def imprimir1(c_1):
    """
    La funsión imprimir1 recibe un número complejo representado de la forma [a,b] y lo devuelve en la forma (a+bi).
    """
    return str(c_1[0]) + " + " + str(c_1[1]) + "i"

def cartesiana_polar(c_1):
    """
    La funsión cartesiana_polar recibe un número complejo c_1 en su forma binómica y lo retorna en su forma polar.
    En el comentario siguiente (precedido por el simbolo #), encontrará otra opcion de return que devolverá el ángulo en grados.
    """
    r = modulo(c_1)
    a = math.atan(c_1[1]/c_1[0])
    #return [r,math.degrees(a)] #(Ángulo en grados)
    return [r, a]

def polar_cartesiana(p_1):
    """
    La funsión polar_cartesiana recibe un número complejo p_1 (que debe ser una lista de longitud 2) en su forma polar y
    lo retorna en su forma binómica (lista con longitud 2).

    """
    a = p_1[0] * math.cos(p_1[1])
    b = p_1[0] * math.sin(p_1[1])
    return [a, b]

def imprimir_exp(p_1):
    """
    La funsión imprimir_exp recibe un número complejo p_1 (que debe ser una lista de longitud 2) en su forma polar y devuelve
    este número en su forma exponencial.
    """
    return str(p_1[0]) + "e^(i" + str(round(p_1[1],4)) + ")"

def potencia_n(c_1, n):
    """
    la funsión recibe un número complejo c_1 en su forma cartesiana y devuelve este mismo elevado a una potencia n.
    """
  #Ingresando un número complejo en su forma binómica
    c_p_1 = cartesiana_polar (c_1)
    #print("Forma Polar:")
    #print(c_p_1)
    rta = polar_cartesiana([c_p_1[0] ** n, c_p_1[1] * n])
    return [round(rta[0]), round(rta[1])]
