import pygame
from pantallas import *

pygame.init()
pygame.font.init()
corriendo_juego = True
def main_principal():
    """
    Controla el bucle principal del juego, manejando eventos y actualizando la pantalla.

    Args:
        None

    Retorna:
        None

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