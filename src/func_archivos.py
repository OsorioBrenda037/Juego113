import json
import os
import pygame

pygame.mixer.init()


def get_path_actual(nombre_archivo: str)-> str:
    """Funcion que nos devuelva la ruta completa del archivo

    Args:
        nombre_archivo (str): recibe el nombre de un archivo

    Returns:
        str: ruta actual del archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


#JSON (imagen | sonido)
def crear_archivo_json_imagenes():
    """
    Crea un archivo JSON que contiene las rutas de diferentes archivos de imagen.

    Esta función crea un archivo JSON llamado 'imagenes.json' en el directorio actual. El archivo contiene un diccionario
    con claves que representan los nombres de diferentes archivos de imagen y sus valores correspondientes representan las
    rutas a esos archivos de imagen. Las rutas son relativas al directorio 'src/assets/images'.

    Parámetros: None
    Retorna: None
    
    """
    imagenes = {
        "imagen_fondo": "src/assets/images/menu_fondo.png",
        "imagen_jugador": "src/assets/images/michi_gordo.png",
        "imagen_pez": "src/assets/images/goldfish.png",
        "flecha_img": "src/assets/images/flecha.png",
        "perro_imagen": "src/assets/images/perro.png",
        "corazon_imagen": "src/assets/images/corazon.png",
        "gatito_pizza": "src/assets/images/gatito_pizza.png",
        "tomasita_foto": "src/assets/images/tomasita.jpg",
        "dulce": "src/assets/images/dulce.jpg"
    }
    
    with open(get_path_actual('imagenes.json'),'w') as file:
        json.dump(imagenes, file, indent=4)

crear_archivo_json_imagenes()

def leer_imagenes():
    """
    Lee las imágenes del archivo 'imagenes.json' y las carga utilizando Pygame.

    Esta función lee las rutas de diferentes archivos de imagen del archivo 'imagenes.json' en el directorio actual.
    Luego carga cada imagen utilizando la función image.load() de Pygame y las devuelve como una tupla.

    Retorna:
        tuple: Una tupla que contiene las imágenes cargadas.
    """
    with open(get_path_actual('imagenes.json'), 'r') as file:
        imagenes = json.load(file)
    
    imagen_fondo = pygame.image.load(imagenes["imagen_fondo"])
    imagen_jugador = pygame.image.load(imagenes["imagen_jugador"])
    imagen_pez = pygame.image.load(imagenes["imagen_pez"])
    flecha_img = pygame.image.load(imagenes["flecha_img"])
    perro_imagen = pygame.image.load(imagenes["perro_imagen"])
    corazon_imagen = pygame.image.load(imagenes["corazon_imagen"])
    gatito_pizza = pygame.image.load(imagenes["gatito_pizza"])
    tomasita_foto = pygame.image.load(imagenes["tomasita_foto"])
    dulce_foto = pygame.image.load(imagenes["dulce"])


    return imagen_fondo, imagen_jugador, imagen_pez, flecha_img, perro_imagen, corazon_imagen, gatito_pizza, tomasita_foto, dulce_foto

imagen_fondo, imagen_jugador, imagen_pez, flecha_img, perro_imagen, corazon_imagen, gatito_pizza, tomasita_foto, dulce_foto = leer_imagenes()

def cargar_archivo_sonidos():
    """
    Escribe un diccionario de rutas de archivo de música y sonidos a un archivo JSON llamado 'Sonidos.json'.
    
    Esta función crea un diccionario llamado 'musica_sonidos' con claves que representan diferentes tipos de archivos de música y sonidos,
    y sus rutas de archivo correspondientes. Las rutas de archivo son relativas al directorio actual y se encuentran en los directorios
    'src/assets/music' y 'src/assets/sounds', respectivamente. El diccionario se escribe en un archivo JSON llamado 'Sonidos.json' utilizando
    la función 'json.dump()'. El archivo se abre en modo de escritura y el diccionario se escribe en el archivo con una indentación de 4 espacios.
    
    Parámetros: None
    
    Retorna: None    
    """
    musica_sonidos = {
       "musica" : "src/assets/musica/musica.mp3",
       "sonido_comer" : "src/assets/sounds/ANIMALCAT_6003_39_1.mp3",
       "sonido_flecha" : "src/assets/sounds/arrow-impact-87260.mp3",
       "sonido_perro" : "src/assets/sounds/dog-bark-179915.mp3",
       "sonido_perder" : "src/assets/sounds/Pou_game_over_sound.mp3"
    }

    with open(get_path_actual('Sonidos.json'), 'w') as archivo:
        json.dump(musica_sonidos, archivo, indent=4)

cargar_archivo_sonidos()

def leer_sonidos_musica():
    """
    Lee archivos de sonido y música de un archivo JSON y los carga en el mezclador de Pygame.

    Retorna:
        tuple: Una tupla que contiene los archivos de música y sonido cargados.
            - pygame.mixer.music: El archivo de música cargado.
            - pygame.mixer.Sound: Los archivos de sonido cargados.

    Levanta:
        FileNotFoundError: Si el archivo 'Sonidos.json' no se encuentra en el directorio actual.
        json.JSONDecodeError: Si el archivo 'Sonidos.json' no es un archivo JSON válido.
    """
    with open(get_path_actual('Sonidos.json'), 'r') as archivo:
        sonidos_musica = json.load(archivo)

    pygame.mixer.music.load(sonidos_musica["musica"])
    sonido_comer = pygame.mixer.Sound(sonidos_musica["sonido_comer"])
    sonido_flecha = pygame.mixer.Sound(sonidos_musica["sonido_flecha"])
    sonido_perro = pygame.mixer.Sound(sonidos_musica["sonido_perro"])
    sonido_perder = pygame.mixer.Sound(sonidos_musica["sonido_perder"])

    return pygame.mixer.music.load(sonidos_musica["musica"]), sonido_comer, sonido_flecha, sonido_perro, sonido_perder

musica, sonido_comer, sonido_flecha, sonido_perro, sonido_perder = leer_sonidos_musica()

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

def swap_lista(lista:list, i:int, j: int)->None:
    """
    Intercambia los elementos en las posiciones i y j de la lista.

    Args:
        lista (list): La lista en la que se realiza el intercambio.
        i (int): El índice del primer elemento a intercambiar.
        j (int): El índice del segundo elemento a intercambiar.

    Retorna:
        None: Esta función no devuelve nada.

    """
    lista[i], lista[j] = lista[j], lista[i]

def ordenar_por_criterio(lista:list, clave:str):
    """
    Ordena una lista de diccionarios según un criterio especificado.

    Args:
        lista (list): La lista de diccionarios a ordenar.
        clave (str): La clave por la cual se ordenarán los diccionarios.

    Returns:
        None: Esta función no devuelve nada. La lista se ordena en su lugar.
    """
    tam = len(lista)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][clave] < lista[j][clave]:
                    swap_lista(lista, i, j)


def guardar_archivo_csv(archivo: str, lista: list):
    """
    Guarda los puntajes en un archivo CSV.

    Args:
        archivo (str): Nombre del archivo CSV.
        lista (list): Lista de diccionarios con los puntajes. Cada diccionario debe tener los campos 'nombre' y 'puntaje'.

    """
    file_path = get_path_actual(f"{archivo}.csv")
    
    escribir_cabecera = not os.path.exists(file_path)

    with open(file_path, 'a', encoding='utf-8', newline='') as archivo_csv:
        if escribir_cabecera:
            archivo_csv.write('nombre,puntaje\n')
        
        for item in lista:
            nombre = item['nombre'].replace(',', '\\,')
            puntaje = str(item['puntaje']).replace(',', '\\,')
            archivo_csv.write(f"{nombre},{puntaje}\n")
    file_path = get_path_actual(f"{archivo}.csv")


def cargar_archivo_csv(nombre_archivo):
    """
    Carga un archivo CSV y devuelve una lista de diccionarios con las puntuaciones. Cada diccionario debe tener los campos 'nombre' y 'puntaje'.
    
    Args:
        archivo (str): param nombre_archivo: El nombre del archivo CSV.

    Returns:
        list: Una lista de diccionarios con las puntuaciones. Cada diccionario debe tener los campos 'nombre' y 'puntaje'.
    """
    datos = []
    file_path = get_path_actual(nombre_archivo)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lineas = file.readlines()
            
            # Verifica que el archivo tenga al menos una línea de cabecera
            if not lineas or len(lineas) < 2:
                print("El archivo CSV está vacío o no tiene cabecera.")
                return datos

            # Lee la cabecera
            cabecera = lineas[0].strip().split(',')
            if len(cabecera) != 2 or cabecera[0] != 'nombre' or cabecera[1] != 'puntaje':
                return datos
            
            # Lee el contenido
            for linea in lineas[1:]:
                partes = linea.strip().split(',')
                if len(partes) == 2:
                    nombre, puntaje = partes
                    nombre = nombre.replace('\\,', ',')
                    try:
                        puntaje = int(puntaje)
                    except ValueError:
                        continue
                    datos.append({'nombre': nombre, 'puntaje': puntaje})
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encuentra.")
    except Exception as e:
        print(f"Error: {e}")

    return datos