from settings import *
from bloques import *
from func_archivos import *
import math
pygame.init()
pygame.font.init()


#--------------------------------------------------------------------------------------------------------------------

def punto_en_rectangulo(punto, rect):
    """
    Comprueba si un punto está dentro de un rectángulo.

    Args:
        punto (tuple): Las coordenadas del punto (x, y).
        rect (pygame.Rect): El objeto rectángulo.

    Returns:
        bool: True si el punto está dentro del rectángulo, False en caso contrario.
    """
    x = punto[0]
    y = punto[1]

    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def distancia_entre_puntos(punto_1:tuple, punto_2:tuple) -> int:
    """
    Calcula la distancia entre dos puntos.

    Args:
        punto_1 (tuple): Las coordenadas del primer punto en el formato (x1, y1).
        punto_2 (tuple): Las coordenadas del segundo punto en el formato (x2, y2).

    Returns:
        float: La distancia entre los dos puntos.
    """
    base = punto_1[0] - punto_2[0]
    altura = punto_1[1] - punto_2[1]
    return math.sqrt(base ** 2 + altura ** 2)


def detectar_colision_circulo(rect_1:tuple, rect_2:tuple) -> bool:
    """
    Detecta si dos objetos circulares están colisionando.

    Args:
        rect_1 (tuple): Una tupla que contiene las coordenadas x e y del centro del primer objeto.
        rect_2 (tuple): Una tupla que contiene las coordenadas x e y del centro del segundo objeto.

    Returns:
        bool: True si los objetos están colisionando, False en caso contrario.
    """
    r1 = rect_1.width // 2
    r2 = rect_2.width // 2
    distancia = distancia_entre_puntos(rect_1.center, rect_2.center)

    if distancia <= r1 + r2:
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------------------------------
def cargar_lista_comida(lista:list, cant:int):
    """
    Agrega una cantidad especificada de objetos comida a una lista dada.

    Args:
        lista (list): La lista a la que se agregarán los objetos comida.
        cant (int): La cantidad de objetos comida a agregar.

    Retorna:
        None
    """
    for _ in range(cant):
        lista.append(crear_comida(imagen_pez))

comida = crear_comida(imagen_pez)
cargar_lista_comida(comidas, cantidad_comida)

def movimiento_comida(lista:list):
    """
    Mueve los elementos en la lista de los alimentos en la pantalla.

    Args:
        lista (list): Una lista de diccionarios, cada uno conteniendo las siguientes claves:
            - "imagen" (pygame.Surface): La imagen del alimento.
            - "rect" (pygame.Rect): El rectángulo que representa la posición y tamaño del alimento.

    Returns:
        None
    """
    for item in lista:
        screen.blit(item["imagen"], item["rect"])
        item["rect"].y += 3

        if item["rect"].y > ALTO:
            y = randrange(-50, -10)
            item["rect"].y = y
            x = randrange(0, 750)
            item["rect"].x = x

#--------------------------------------------------------------------------------------------------------------------
def cargar_lista_flechas(lista:list, cant:int):
    """
    Agrega una cantidad especificada de objetos flecha a una lista dada.

    Args:
        lista (list): La lista a la que se agregarán los objetos flecha.
        cant (int): La cantidad de objetos comida a agregar.

    Retorna:
        None
    """
    for _ in range(cant):
        lista.append(crear_flechas(flecha_img))

flecha = crear_flechas(flecha_img)
cargar_lista_flechas(flechas_izdr, cantidad_flechas)

def movimiento_flecha(lista:list):
    """
    Mueve las flechas en la lista dada a lo largo de la pantalla.

    Args:
        lista (list): Una lista de diccionarios, cada uno conteniendo las siguientes claves:
            - "imagen" (pygame.Surface): La imagen de la flecha.
            - "rect" (pygame.Rect): El rectángulo que representa la posición y tamaño de la flecha.

    Returns:
        None
    """
    for flecha in lista[:]:
        screen.blit(flecha["imagen"], flecha["rect"])
        flecha["rect"].x += VELOCIDAD_X

#--------------------------------------------------------------------------------------------------------------------
def cargar_lista_perros(lista:list, cant:int):
    """
    Agrega una cantidad especificada de objetos perro a una lista dada.

    Args:
        lista (list): La lista a la que se agregarán los objetos perro.
        cant (int): La cantidad de objetos comida a agregar.

    Retorna:
        None
    """
    for _ in range(cant):
        lista.append(crear_perro(perro_imagen))

perros = crear_perro(perro_imagen)
cargar_lista_perros(perros_arab, cantidad_perros)

def movimiento_perro(lista:list):
    """
    Mueve la lista de perros en la lista dada.

    Args:
        lista (list): Una lista de diccionarios, cada uno con las siguientes claves:
            - "imagen" (pygame.Surface): La imagen del perro.
            - "rect" (pygame.Rect): El rectángulo que representa la posición y tamaño del perro.

    Returns:
        None
    """
    for ataque in lista:
        screen.blit(ataque["imagen"], ataque["rect"])
        ataque["rect"].y += 4

        if ataque["rect"].y > ALTO:
            y = randrange(-50, -10)
            ataque["rect"].y = y
            x = randrange(0, 750)
            ataque["rect"].x = x

#--------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
def mover_jugador(jugador:dict, mover_izquierda:bool, mover_derecha:bool):
    """
    Mueve al jugador en la dirección especificada.

    Args:
        jugador (dict): Un diccionario que representa al jugador.
        mover_izquierda (bool): Un booleano que indica si el jugador debe moverse hacia la izquierda.
        mover_derecha (bool): Un booleano que indica si el jugador debe moverse hacia la derecha.

    Returns:
        None
    """
    if mover_izquierda and jugador["rect"].left > 0:
        jugador["rect"].left -= VELOCIDAD_X
        if jugador["rect"].left < 0:
            jugador["rect"].left = 0

    if mover_derecha and jugador["rect"].right < ANCHO:
        jugador["rect"].right += VELOCIDAD_X
        if jugador["rect"].right > ANCHO:
            jugador["rect"].right = ANCHO


def dibujar_vidas(vidas:int, imagen:pygame.surface):
    """Dibuja las vidas en la pantalla.

    Args:
        vidas (int): Cantidad de vidas
        imagen (pygame.surface): imagen de la vida
    """
    x = 700
    y = 20
    for i in range(vidas):
        try:
            imagen = pygame.transform.scale(imagen, (corazon_ancho, corazon_alto))
            screen.blit(imagen, (x - i * 40, y))
        except:
            pygame.draw.rect(screen, RED, (x - i * 40, y, 30, 30))

corazon = dibujar_vidas(vidas, corazon_imagen)

#-------------------------------------------------------------------------------------------------------------------

def resetear_partida():
    """
    Reinicia el estado del juego al estado inicial.

    Args:
        None

    Retorna:
        None
    """
    global tiempo_ultima_flecha, VELOCIDAD_X, VELOCIDAD_Y, FUERZA_SALTO, GRAVEDAD, en_el_suelo, mover_derecha, mover_izquierda, saltar
    global vidas, score, jugador, jugador_ancho, jugador_alto, jugador_x, jugador_y, vidas, score, fuente, texto_score, texto_mute
    global flecha, perros, texto_mute, texto_score, comida, comidas, comida_ancho, comida_alto, cantidad_comida, flecha_ancho, flecha_alto, cantidad_flechas, flechas_izdr, INTERVALO_FLECHAS
    global perro_ancho, perro_alto, perros_arab, cantidad_perros, corazon_ancho, corazon_alto, menu, is_running, musica_sonando

    # Reiniciar variables booleanas
    en_el_suelo = True
    mover_derecha = False
    mover_izquierda = False
    saltar = False
    menu = True
    is_running = True
    musica_sonando = True

    # Reiniciar listas
    comidas = []
    flechas_izdr = []
    perros_arab = []

    # Reiniciar bloques
    vidas = 3
    score = 0
    VELOCIDAD_X = 7
    VELOCIDAD_Y = 5
    FUERZA_SALTO = 15
    GRAVEDAD = 1
    jugador_x = 34
    jugador_y = 485
    jugador_ancho = 50
    jugador_alto = 50
    jugador = crear_jugador(imagen_jugador)
    comida_ancho = 50
    comida_alto = 50
    cantidad_comida = 7
    comida = crear_comida(imagen_pez)
    cargar_lista_comida(comidas, cantidad_comida)
    flecha = crear_flechas(flecha_img)
    cantidad_flechas = 1
    flecha_ancho = 50
    flecha_alto = 50
    perro_ancho = 50
    perro_alto = 50
    perros = crear_perro(perro_imagen)
    cantidad_perros = 3
    corazon_ancho = 50
    corazon_alto = 50
    dibujar_vidas(vidas, corazon_imagen)
    pygame.mixer.music.play()
    texto_score = fuente.render(f"gordura: {score}", True, RED)
    texto_mute = fuente.render("UNMUTE", True, RED)
    tiempo_ultima_flecha = pygame.time.get_ticks()
#_______________________________________________________

def mostrar_puntajes(screen, fuente, ANCHO, ALTO):
    """
    Muestra los puntajes más altos en la pantalla.

    Args:
        screen (pygame.Surface): La superficie de la pantalla donde se dibujarán los puntajes.
        fuente (pygame.font.Font): La fuente utilizada para renderizar el texto de los puntajes.
        ANCHO (int): El ancho de la pantalla.
        ALTO (int): La altura de la pantalla.
    """
    puntajes = cargar_archivo_csv("top_rank.csv") 
    ordenar_por_criterio(puntajes, "puntaje")
    top_5 = puntajes[:5]
    y = 250
    for puntaje in top_5:
        texto = f"{puntaje['nombre']} {puntaje['puntaje']}"
        puntaje_text = fuente.render(texto, True, (0,0,0))
        screen.blit(puntaje_text, (ANCHO // 2 - 100, y))
        y += 50
