"""
El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.

En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

Tu tarea es escribir un par de funciones que conviertan l/100km a mpg(milas por galón), y viceversa.

Las funciones:

Se llaman l100kmampg y mpgal100km respectivamente.
Toman un argumento (el valor correspondiente a sus nombres).
Complementa el código en el editor.

Ejecuta tu código y verifica si tu salida es la misma que la nuestra.

Aquí hay información para ayudarte:

1 milla = 1609.344 metros.
1 galón = 3.785411784 litros.
"""

from re import M
from unicodedata import numeric


def l100kmampg(litrox100k:numeric)->numeric:
    k_a_mi = 62.1371 # (100 km * 1000 m) / 1609.344 m  = 62.1371 millas constante (aprox).
    g_x_km = litrox100k / 3.785411784 # litros x cada 100 km / 3.78... litros = galones x 100 km
    millaxgalon = k_a_mi / g_x_km # 100 km (o sea, 62.14 millas) / galones por los litros de 100k = milla x galón

    return millaxgalon

def mpgal100km(millaxgalon:numeric)->numeric:
    mi_a_k = (millaxgalon * 1609.344) / 1000 # conviertes millas a metros a kilómetros
    litrox100k = 378.5411784 / mi_a_k #  100 km * 3.7854 = 378.54 constante / millas a ki = millas x galón 
    """
        regla de 3: millas x galon (en KM) es a 3.79 litros como 100 es a X
    """
    return litrox100k     


print(l100kmampg(1.83)) ## 128.53
print(mpgal100km(128))  ## 1.8376

print(l100kmampg(100)) ## suponiendo 100 litros por 100 km = 2.35 millas por galón
print(mpgal100km(2.35)) ## la inversa, 2.35 millas x galón = 100 litros x km

