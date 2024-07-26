import pygame
from pantallas import *

pygame.init()
pygame.font.init()
corriendo_juego = True
def main_principal():
    """
    Controla el bucle principal del juego, manejando eventos y actualizando la pantalla.

    Esta función se encarga de:
    - Mantener el bucle principal del juego mientras la variable 'corriendo_juego' sea True.
    - Crear un objeto de reloj para controlar la tasa de fotogramas.
    - Procesar eventos de salida del juego.
    - Dibujar el menú en la pantalla.
    - Actualizar la pantalla y limitar la tasa de fotogramas a un valor definido por la constante 'FPS'.
    """
    global dibujar_menu
    while corriendo_juego:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo_juego = False

        dibujar_menu(imagen_fondo)
        pygame.display.flip()
        clock.tick(FPS)
main_principal()