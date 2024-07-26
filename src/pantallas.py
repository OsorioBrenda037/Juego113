import pygame
import sys
from settings import *
from func_archivos import *
from funciones import *
pygame.init()

def dibujar_menu(imagen_fondo):
    """
    Dibuja un menú en la pantalla.

    Args:
        imagen_fondo (pygame.Surface): La imagen de fondo a dibujar en la pantalla.

    Retorna:
        tuple: Una tupla que contiene la cadena "JUGAR!!!" y un booleano que indica si el juego sigue en ejecución.
    """
    bonton_AN = 200
    boton_AL = 50

    if imagen_fondo:
        try:
            screen.blit(imagen_fondo, (0,0))
        except TypeError:
            screen.fill(WHITE)

    texto_jugar = fuente.render("Jugar", True, BLACK) 
    boton_jugar = crear_bloque((ANCHO // 2) - 100, (ALTO // 2) - 100, bonton_AN, boton_AL, GREEN)
    pygame.draw.rect(screen, boton_jugar["color"], boton_jugar["rect"])
    texto_rect_jugar = texto_jugar.get_rect()
    texto_rect_jugar = (boton_jugar["rect"].x + ((boton_jugar["rect"].width - texto_rect_jugar.width) // 2), boton_jugar["rect"].y + ((boton_jugar["rect"].height - texto_rect_jugar.height) // 2))
    screen.blit(texto_jugar, texto_rect_jugar)

    texto_ranking = fuente.render("Highscore", True, BLACK) 
    boton_ranking = crear_bloque(boton_jugar["rect"].x, boton_jugar["rect"].y + 100, bonton_AN, boton_AL, YELLOW)
    pygame.draw.rect(screen, boton_ranking["color"], boton_ranking["rect"])
    texto_rect_ranking = texto_jugar.get_rect()
    texto_rect_ranking = (boton_ranking["rect"].x - 20 + ((boton_ranking["rect"].width - texto_rect_ranking.width) // 2), boton_ranking["rect"].y + 5 + ((boton_ranking["rect"].height - texto_rect_ranking.height) // 2))
    screen.blit(texto_ranking, texto_rect_ranking)

    texto_salir = fuente.render("Salir", True, BLACK) 
    boton_salir = crear_bloque(boton_jugar["rect"].x, boton_jugar["rect"].y + 200, bonton_AN, boton_AL, PINK)
    pygame.draw.rect(screen, boton_salir["color"], boton_salir["rect"])
    texto_rect_salir = texto_salir.get_rect()
    texto_rect_salir = (boton_salir["rect"].x + ((boton_salir["rect"].width - texto_rect_salir.width) // 2), boton_salir["rect"].y + ((boton_salir["rect"].height - texto_rect_salir.height) // 2))
    screen.blit(texto_salir, texto_rect_salir)

    screen.blit(gatito_pizza_amoldada, (50, 300))
    screen.blit(texto_titulo, (300, 50))
    running = True
    while running:
        clock.tick(FPS)
        # ----> detectar los eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if punto_en_rectangulo(evento.pos, boton_jugar["rect"]):
                        return game_loop(), False
                    if punto_en_rectangulo(evento.pos, boton_ranking["rect"]):
                        return ranking_pantalla(), False
                    if punto_en_rectangulo(evento.pos, boton_salir["rect"]):
                        pygame.quit()
                        sys.exit()
            
        pygame.display.flip()


def ranking_pantalla() -> tuple:
    """
    Muestra la pantalla de ranking del juego, permitiendo al usuario ver los puntajes más altos
    y regresar al menú principal.

    Returns:
        tuple: 
            - Si el usuario hace clic en el botón "Volver", retorna la llamada a `dibujar_menu(imagen_fondo)` y False.
            - Si el usuario cierra la ventana del juego, retorna None y False.
    """
    clock = pygame.time.Clock()
    running = True

    # Dibujar botón "Volver"
    texto_volver = fuente.render("Volver", True, BLACK)
    texto_rect_volver = texto_volver.get_rect()
    texto_rect_volver.topleft = (550, ALTO - 50)

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if texto_rect_volver.collidepoint(evento.pos):
                        return dibujar_menu(imagen_fondo), False

        screen.fill(PINK)       
        mostrar_puntajes(screen, fuente, ANCHO, ALTO)
        texto_ranking = fuente.render("Ranking", True, BLACK)
        texto_ranking_rect = texto_ranking.get_rect(center=(ANCHO // 2, 50))
        texto_subtitulo = fuente.render("Cinco mejores partidas", True, BLACK)
        texto_subtitulo_rect = texto_subtitulo.get_rect(center=(ANCHO // 2, 100))
        texto_parentesis = fuente.render("(Nombre del jugador junto a su puntaje)", True, BLACK)
        texto_parentensis_rect = texto_parentesis.get_rect(center=(ANCHO // 2, 150))
        
        screen.blit(texto_ranking, texto_ranking_rect)
        screen.blit(texto_subtitulo, texto_subtitulo_rect)
        screen.blit(texto_parentesis, texto_parentensis_rect)
        screen.blit(texto_volver, texto_rect_volver)
        screen.blit(dulce_foto_amoldada, (500, 250))
        screen.blit(tomasita_foto_amoldada, (50, 300))
    
         

        pygame.display.flip()
        clock.tick(60)

    return None, False

    

def game_over_screen(score:int):
    """
    Muestra la pantalla de juego finalizado y maneja la entrada del usuario.
    
    Args:
        score (int): El puntaje del jugador.

    Retorna: None
    """
    clock = pygame.time.Clock()
    running = True
    
    nombre = input("Ingrese su nombre/iniciales: ")
    lista_puntajes = [{"puntaje": score, "nombre": nombre}]
    guardar_archivo_csv("top_rank", lista_puntajes)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
                    dibujar_menu(imagen_fondo)
                    

        screen.fill(ORANGE)
        fuente = pygame.font.Font(None, 45)
        game_over_texto = fuente.render("GAME OVER", True, BLACK)
        puntaje_texto = fuente.render(f"NIVEL DE GORDURA: {score}", True, BLACK)
        instrucciones = fuente.render("PRESIONE TECLA RETURN PARA VOLVER AL MENÚ", True, BLACK)

        screen.blit(game_over_texto, (200, 50))
        screen.blit(puntaje_texto, (200, 100))
        screen.blit(instrucciones, (5, 300))

        pygame.display.flip()
        clock.tick(60)

def game_loop():
    """
    Controla el bucle principal del juego, gestionando eventos, actualizando el estado del juego
    y dibujando elementos en la pantalla.

    """
    global tiempo_ultima_flecha, VELOCIDAD_X, VELOCIDAD_Y, FUERZA_SALTO, GRAVEDAD, en_el_suelo, mover_derecha, mover_izquierda, saltar
    global vidas, score, jugador, jugador_ancho, jugador_alto, jugador_x, jugador_y, vidas, score, fuente, texto_score, texto_mute
    global flecha, perros, texto_mute, texto_score, comida, comidas, comida_ancho, comida_alto, cantidad_comida, flecha_ancho, flecha_alto, cantidad_flechas, flechas_izdr, INTERVALO_FLECHAS
    global perro_ancho, perro_alto, perros_arab, cantidad_perros, corazon_ancho, corazon_alto, menu, is_running, musica_sonando

    while is_running:
        tiempo_actual = pygame.time.get_ticks()
        clock.tick(FPS)

        # ----> detectar los eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                is_running = False

            #-----------------------------------
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    mover_izquierda = True
                    mover_derecha = False
                
                if evento.key == pygame.K_RIGHT:
                    mover_derecha = True
                    mover_izquierda = False
            
                if evento.key == pygame.K_SPACE and en_el_suelo:
                    saltar = True
                    en_el_suelo = False
                    VELOCIDAD_Y = -FUERZA_SALTO

                if evento.key == pygame.K_m:
                    if musica_sonando:
                        pygame.mixer.music.pause()
                        musica_sonando  = False
                        texto_mute = fuente.render("MUTE", True, RED)
                    else:
                        pygame.mixer.music.unpause()
                        musica_sonando = True
                        texto_mute = fuente.render("UNMUTE", True, RED)

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    mover_izquierda = False
                
                if evento.key == pygame.K_RIGHT:
                    mover_derecha = False
            
        if not en_el_suelo:
            VELOCIDAD_Y += GRAVEDAD
            jugador["rect"].top += VELOCIDAD_Y
            if jugador["rect"].bottom >= 536:
                jugador["rect"].bottom = 536
                en_el_suelo = True
                VELOCIDAD_Y = 0

        mover_jugador(jugador, mover_izquierda, mover_derecha)

        #-------------------------------------------------------       
        
        for item in comidas[:]:
            if detectar_colision_circulo(item["rect"], jugador["rect"]):
                comidas.remove(item)
                score = score + 1
                texto_score = fuente.render(f"gordura: {score}", True, RED)
                sonido_comer.play()
                if len(comidas) == 0:
                    cargar_lista_comida(comidas, cantidad_comida)
        
        for item in flechas_izdr[:]:
            if detectar_colision_circulo(item["rect"], jugador["rect"]):
                vidas -= 1
                sonido_flecha.play()
                flechas_izdr.remove(item)
                if vidas == 0:
                    pygame.mixer.music.stop()
                    sonido_perder.play()
                    game_over_screen(score)
                    resetear_partida()

        if tiempo_actual - tiempo_ultima_flecha >= INTERVALO_FLECHAS:
            nueva_cantidad_flechas = 1
            cargar_lista_flechas(flechas_izdr, nueva_cantidad_flechas)
            tiempo_ultima_flecha = tiempo_actual

        for item in perros_arab[:]:
            if detectar_colision_circulo(item["rect"], jugador["rect"]):
                vidas -= 1
                sonido_perro.play()
                perros_arab.remove(item)
                if vidas == 0:
                    pygame.mixer.music.stop()
                    sonido_perder.play()
                    game_over_screen(score)
                    resetear_partida()
                if len(perros_arab) == 0:
                    cargar_lista_perros(perros_arab, cantidad_perros)

        #-----------------------------------------------
        screen.fill(MAGENTA)
        screen.blit(imagen_fondo, imagen_fondo_posicion)
        screen.blit(jugador["imagen"], jugador["rect"])
        screen.blit(texto_score , (350, 20))
        screen.blit(texto_mute, (30, 20))
        
        movimiento_comida(comidas)
        movimiento_perro(perros_arab)
        movimiento_flecha(flechas_izdr)
        dibujar_vidas(vidas, corazon_imagen)
        

        pygame.display.flip()

    pygame.quit()


dibujar_menu(imagen_fondo)