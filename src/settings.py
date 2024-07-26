import pygame
from func_archivos import *
pygame.font.init()
pygame.mixer.init()
#Ajustes de pantalla
ANCHO = 800
ALTO = 600
TAM_PANTALLA = (ANCHO, ALTO)
CENTRO_PANTALLA = (ANCHO // 2, ALTO // 2)
FPS = 60


#Colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (244, 157, 62)
PINK = (255, 174, 201)


#Variables de pantalla
screen = pygame.display.set_mode(TAM_PANTALLA)
pygame.display.set_caption("Dulce Tomasita")
screen.fill(MAGENTA)
clock = pygame.time.Clock()
imagen_fondo_posicion = (0,0)


#direcciones
VELOCIDAD_X = 7
VELOCIDAD_Y = 5
FUERZA_SALTO = 15
GRAVEDAD = 1


#banderas de movimiento
en_el_suelo = True
mover_derecha = False
mover_izquierda = False
saltar = False


#Jugador
jugador_ancho = 50
jugador_alto = 50
jugador_x = 34
jugador_y = 485
vidas = 3
score = 0


#Texto
fuente = pygame.font.SysFont(None, 45, False, True)
texto_score = fuente.render(f"gordura: {score}", True, RED)
texto_mute = fuente.render("UNMUTE", True, RED)
tiempo_ultima_flecha = pygame.time.get_ticks()
texto_titulo = fuente.render("Dulce Tomasita", True, BLACK)

#Variables de comida
comidas = []
comida_ancho = 50
comida_alto = 50
cantidad_comida = 7


#Flechas (enemigo 1)
flecha_ancho = 80
flecha_alto = 80
cantidad_flechas = 0
flechas_izdr = []
INTERVALO_FLECHAS = 5000


#Perro (enemigo 2)
perro_ancho = 50
perro_alto = 50
perros_arab = []
cantidad_perros = 3


#vidas
corazon_ancho = 50
corazon_alto = 50
menu = True
is_running = True

#MUSICA
musica_sonando = True

#imagenes adicionales
gatito_pizza_amoldada = pygame.transform.scale(gatito_pizza, (150, 250))
tomasita_foto_amoldada = pygame.transform.scale(tomasita_foto, (200, 250))
dulce_foto_amoldada = pygame.transform.scale(dulce_foto, (250, 250))