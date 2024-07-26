import pygame
from func_archivos import *
from random import randint, randrange, choice
from settings import *


def crear_bloque(x=0, y=0, ancho=100, alto=100, color=(255, 255, 255), borde=0, radio=-1, imagen=None):
    """
    Crea un diccionario que representa un bloque con los parámetros especificados.

    Args:
        x (int, opcional): La coordenada x del bloque. Por defecto es 0.
        y (int, opcional): La coordenada y del bloque. Por defecto es 0.
        ancho (int, opcional): El ancho del bloque. Por defecto es 100.
        alto (int, opcional): El alto del bloque. Por defecto es 100.
        color (tupla, opcional): El color del bloque. Por defecto es (255, 255, 255).
        borde (int, opcional): El ancho del borde del bloque. Por defecto es 0.
        radio (int, opcional): El radio del bloque. Por defecto es -1.
        imagen (pygame.Surface, opcional): La imagen del bloque. Por defecto es None.

    Returns:
        dict: Un diccionario que contiene el rectángulo, el color, el borde, el radio y la imagen del bloque.
    """
    dict_bloque = {}
    dict_bloque["rect"] = pygame.Rect(x, y, ancho, alto)
    dict_bloque["color"] = color
    dict_bloque["borde"] = borde
    dict_bloque["radio"] = radio
    dict_bloque["imagen"] = imagen
    return dict_bloque

#--------------------------------------------------------------------------------------------------------------------
def crear_jugador(imagen=None):
    """
    Crea un objeto de jugador con la imagen especificada.

    Args:
        imagen (pygame.Surface, opcional): La imagen a utilizar para el jugador. Si no se proporciona, se utilizará una imagen predeterminada.

    Returns:
        dict: Un diccionario que contiene el objeto del jugador con los atributos especificados.

    """
    if imagen:
        imagen = pygame.transform.scale(imagen, (jugador_ancho, jugador_alto))
    return crear_bloque(jugador_x, jugador_y, jugador_ancho, jugador_alto, (0,0,0), 25, 25, imagen)

jugador = crear_jugador(imagen_jugador)

#--------------------------------------------------------------------------------------------------------------------
def crear_comida(imagen=None):
    """
    Crea un objeto de comida con la imagen especificada.

    Args:
        imagen (pygame.Surface, opcional): La imagen a utilizar para la comida. Si no se proporciona, se utilizará una imagen predeterminada.

    Returns:
        dict: Un diccionario que contiene el objeto de comida con los atributos especificados.

    """
    if imagen:
        imagen = pygame.transform.scale(imagen, (comida_ancho, comida_alto))
    return crear_bloque(randint(0, ANCHO - jugador_ancho), 0, jugador_ancho, jugador_alto, BLACK, 25, 25, imagen)

#--------------------------------------------------------------------------------------------------------------------
def crear_flechas(imagen):
    """
    Crea un conjunto de flechas con la imagen especificada.

    Args:
        imagen (pygame.Surface): La imagen a utilizar para las flechas.

    Returns:
        dict: Un diccionario que contiene el objeto de flecha con los atributos especificados.

    """
    if imagen:
        imagen = pygame.transform.scale(imagen, (flecha_ancho, flecha_alto))
    return crear_bloque(0, jugador_y, flecha_ancho, flecha_alto, BLACK, 25, 25, imagen)

#--------------------------------------------------------------------------------------------------------------------
def crear_perro(imagen=None):
    """
    Crea un objeto de perro con la imagen especificada.

    Args:
        imagen (pygame.Surface, opcional): La imagen a utilizar para el perro. Si no se proporciona, se utilizará una imagen predeterminada.

    Returns:
        dict: Un diccionario que contiene el objeto de perro con los atributos especificados.

    Raises:
        None

    """
    if imagen:
        imagen = pygame.transform.scale(imagen, (perro_ancho, perro_alto))
    return crear_bloque(randint(0, ANCHO - jugador_ancho), 0, perro_ancho, perro_alto, BLACK, 25, 25, imagen)

#--------------------------------------------------------------------------------------------------------------------