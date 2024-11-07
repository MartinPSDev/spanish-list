#!/usr/bin/env python3
import argparse
import itertools
import random
import string
import time
from typing import List, Set
import threading
import sys 

def print_banner():
    banner = """
    ███████╗██████╗  █████╗ ███╗   ██╗██╗███████╗██╗  ██╗    ██╗     ██╗███████╗████████╗
    ██╔════╝██╔══██╗██╔══██╗████╗  ██║██║██╔════╝██║  ██║    ██║     ██║██╔════╝╚══██╔══╝
    ███████╗██████╔╝███████║██╔██╗ ██║██║███████╗███████║    ██║     ██║███████╗   ██║   
    ╚════██║██╔═══╝ ██╔══██║██║╚██╗██║██║╚════██║██╔══██║    ██║     ██║╚════██║   ██║   
    ███████║██║     ██║  ██║██║ ╚████║██║███████║██║  ██║    ███████╗██║███████║   ██║   
    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝╚══════╝   ╚═╝   
                     by @M4rt1n_0x1337
    """
    print(banner)

def load_base_words() -> Set[str]:
    nombres = {
    "abigail", "abel", "abraham", "adalberto", "adela", "adelaida", "adrian", "adriana", 
    "agustin", "alba", "alberto", "alejandra", "alejandro", "alex", "alexander", "alexandra", 
    "alicia", "alma", "alvaro", "amalia", "amanda", "ana", "andrea", "andres", "angel", 
    "angela", "anibal", "anita", "antonio", "araceli", "ariel", "armando", "arturo", 
    "augusto", "aurora", "axel", "barbara", "beatriz", "belen", "benito", "benjamin", 
    "bianca", "blanca", "brenda", "bruno", "camila", "candela", "carla", "carlos", 
    "carmen", "carolina", "catalina", "cecilia", "celeste", "celia", "claudio", 
    "claudia", "cristian", "cristina", "cynthia", "daniel", "daniela", "dario", 
    "deborah", "delia", "diego", "diana", "dina", "doris", "eduardo", "efrain", 
    "elena", "elias", "elisa", "elizabeth", "elvira", "emilia", "emiliano", "emilio", 
    "encarnacion", "erick", "ernesto", "esperanza", "esteban", "estela", "eugenia", 
    "eugenio", "eva", "facundo", "fabiola", "felipe", "felix", "fernanda", "fernando", 
    "fidel", "flor", "florencia", "francisco", "franco", "fredy", "frida", "gabriel", 
    "gabriela", "genaro", "gerardo", "gloria", "graciela", "guillermo", "gustavo", 
    "hector", "herman", "herminia", "hilda", "hugo", "ignacio", "ilaria", "iliana", 
    "inés", "irene", "irina", "isabel", "isabella", "isidro", "ivan", "jacinta", 
    "jaime", "javier", "jessica", "jimena", "joaquin", "jorge", "josé", "josefa", 
    "josefina", "juan", "juana", "julia", "juliana", "julieta", "justina", "karina", 
    "karen", "karla", "laura", "leandro", "leonardo", "leonor", "leticia", "lidia", 
    "liliana", "lorena", "lourdes", "lucas", "lucia", "luciana", "luis", "luisa", 
    "luz", "magdalena", "manuela", "manuel", "marcela", "marcia", "marcos", "margarita", 
    "maria", "mariana", "mariano", "marisol", "marta", "martin", "martina", "mateo", 
    "matias", "maximiliano", "melisa", "mercedes", "micaela", "miguel", "miriam", 
    "mireya", "mirta", "monica", "montserrat", "nancy", "natalia", "natasha", "nelson", 
    "nicolas", "nicole", "nina", "noelia", "nora", "norberto", "norma", "olga", 
    "omar", "oscar", "pablo", "pamela", "paola", "paulina", "patricia", "paula", 
    "pedro", "pilar", "rafael", "ramiro", "raquel", "rebecca", "reina", "renata", 
    "ricardo", "roberto", "rocio", "rodolfo", "romina", "rosa", "rosario", "rubén", 
    "sabrina", "salvador", "samanta", "samuel", "sandra", "sara", "sebastian", "selena", 
    "sergio", "silvana", "silvia", "simón", "sofia", "sonia", "susana", "tamara", 
    "teodoro", "teresa", "tomás", "ulises", "ursula", "valentina", "valeria", "vanessa", 
    "verónica", "vicente", "victor", "victoria", "viviana", "wilfredo", "ximena", 
    "yolanda", "yvette", "zaida", "zoe", "zulema"
    }
    
    apellidos = {
        "perez", "lopez", "ramirez", "soto", "nunez", "gonzalez", "fernandez", "martinez", 
        "rodriguez", "diaz", "torres", "castro", "vazquez", "morales", "jimenez", 
        "hernandez", "pineda", "salazar", "mendoza", "carrillo", "sandoval","nuñez"
    }


    
    nicknames = {
        "tincho", "rodo", "fran", "licha", "pato", "guille", "pipa", "tato", "chino", "lucho",
        "rama","pancho", "santi", "joaco", "rulo", "pela", "mudo", "negro", "colo", "pipi"
    }



    lugares = {
        "buenosaires", "cordoba", "rosario", "mendoza", "laplata", "quilmes", "lanus",
        "avellaneda", "sanisidro", "tigre", "pilar", "moron", "municipio", "municipalidad",
        "salta", "tucuman", "neuquen", "bariloche", "mardelplata", "tandil",
        "catamarca", "chaco", "chubut", "corrientes", "entre rios", "formosa", 
        "jujuy", "lapampa", "larioja", "misiones", "neuquen", "rionegro", 
        "san juan", "sanluis", "santacruz", "santafe", "santiagodelestero", 
        "tierradelfuego", "tucuman", "rosario", "san fernando", "sanmiguel", "moron", 
        "tresdefebrero", "berazategui", "berisso", "lomasdezamora", "sanmartin", "marcospaz", 
        "caba", "villamaria", "bahiablanca", "parana", "posadas", "lasheras", "calafate", "sanrafael", "sanjuan", 
        "salta", "chaco", "gualeguaychu", "generalroca", "trelew", "rawson", 
        "bernal", "sanvicente", "carrilobo", "bellville", "embalse", "chaque", "comodororivadavia",
        "viedma", "sanbernardo", "puntaalta", "villagesell", "bellavista", "villaelisa", "algarrobo", "santarosa", 
        "sanmartindelosandes", "villamaría", "villadelparque", "alvear", "lacañada", 
        "elcalafate", "generalpico", "necochea", "colon", "laprida", "mardelplata"
    }


    empresas = {
        "claro", "personal", "movistar", "fibertel", "flow", "telecentro",
        "adidas", "nike", "samsung", "philips", "sony", "lg", "whirlpool",
        "garbarino", "falabella", "coto", "carrefour", "walmart", "easy",
        "mercadolibre", "amazon", "apple", "microsoft", "google",
        "starbucks", "mcdonalds", "burguerking", "mostaza", "wendys", "cafe",
        "cafe tortoni", "iluminacion", "cafedelosartistas"
    }
    
    deportes = {
        "campeon", "campeones", "futbol", "racing", "river", "boca", "independiente",
        "estudiantes", "velez", "sanlorenzo", "newells", "central", "gimnasia",
        "huracan", "talleres", "belgrano", "banfield", "lanus"
    }
    
    
    comercios = {
    "shopping", "unicenter", "abasto", "altoplata", "dotbaires", 
    "galeria", "plaza", "terminal", "estacion", "aeropuerto", 
    "alcorta", "santafeshopping", "devotoshopping", "paseoquilmes", 
    "maderoshopping", "paseolaplaza", "paseorosa", "paseozonanorte", 
    "shoppingsur", "liniers", "shoppingnorte", "paseodelsol", 
    "buenavista shopping", "caballito shopping", "rosarioshopping", "lomasshopping", 
    "open 25", "cinepolis", "cinemark", "cinesoutlet", "palermo", "villages", 
    "rivadavia", "megatone", "gondolas", "miciudad", "falabella", "carrefour", 
    "easy", "sodimac", "coto", "disco", "jumbo", "lidl", "walmart", "yaguaron", 
    "musimundo", "pepsi", "laanonima", "thegallery", "despensa", "supermercado", 
    "unilac", "supermercados dia", "galeriazonasur", "compumundo", "i-store", 
    "lavida", "particular", "tacito", "danone", "tarea", "electro", "luisborges", 
    "factura", "maxi", "starbucks", "cafemartinez", "cafedelaplaza", "lattente", 
    "tucan", "cafetortoni", "lapanerarosa", "librosycafe", "mundocafe", 
    "teaconnection", "cafebolivar", "elclubdelamilanesa", "donado", "terraza", 
    "lacasadelte", "cafevinilo", "peña", "elhornero", "bocacafe", "bonafide", 
    "garbarino", "compumundo", "fravega", "mueblesdico", "personal", "movistar", 
    "claro", "net", "fibertel", "cablevision", "apple", "samsung", "lg", "hp", 
    "motorola", "lenovo", "dell", "asus", "acer", "xbox", "playstation", "microsoft", 
    "logitech", "kaspersky", "casio", "alcatel", "eurocom", "blu", "toshiba", 
    "ropa", "nike", "adidas", "lacoste", "lecoqsportif", "puma", "reebok", 
    "complot", "cdg", "zara", "bershka", "stradivarius", "pullandbear", "gap", 
    "h&m", "mango", "kenzo", "emporio armani", "valentino", "dior", "chanel", 
    "arcor", "marihuana", "cocacola", "fanta", "pepsi", "cervezaquilmes", 
    "heineken", "swiss", "emporio", "grido", "candy", "toblerone", "nescafe", 
    "nestle", "lascarmelitas", "kellogg's", "molinos", "latam", "rio", 
    "easy", "sodimac", "homecenter", "falabella", "todo hogar", "lafam", "tiendanaranja", 
    "mc donalds", "burgerking", "subway", "dominos", "kfc", "sushiroll", "sushiclub"
    "lasaña", "laparrilla", "pizzeta", "lascanteras", "tequila", "helados", 
    "vips", "sushi", "lacadena", "tacobar", "bakery", "centrococina",  
    "correoargentino", "andreani", "ocasa", "mercadolibre", "jotabe", 
    "cargill", "francini", "ypf", "shell", "pampaenergia", "telecom", "lagaleria", "lagalera",
    "braga","charlotte"
    }

    

    universidades = {
        "uba", "utn", "universidaddebuenosaires", "universidadnacionaldelaplata",
        "universidadnacionaldecordoba", "universidaddelamatanza", "universidadcatolica",
        "uca","um","uno","unlam","unahur","uade","up","usal","unlu","uflo","ub","untref","unsam",
        "colegio", "escuela", "escuela tecnica","unla","uai"
    }

    frases_cortas = {
        "laverdadnoslibera", "eltiempopasa", "nuncasabremos", "siguetusalud", 
        "unmundomejor", "lavidaesbella", "nuncasinsentido", "elamorvence", 
        "sueñosyrealidad", "juntosporsiempre","teamo","elamordemivida"
    }


    anios = {str(year) for year in range(1900, 2050)}
     
    return nombres | apellidos | nicknames | lugares | empresas | deportes | comercios | universidades | frases_cortas | anios



def generate_combinations(words: Set[str], max_len: int, include_special: bool) -> Set[str]:
    result = set()
    chars_upper = string.ascii_uppercase + string.digits
    chars_lower = string.ascii_lowercase + string.digits
    special_chars = "!@#$%^&*-_+=."
    
    if include_special:
        chars_upper += special_chars
        chars_lower += special_chars
        
    fechas = {f"{day:02d}{month:02d}{year}" for year in range(1960, 2051) for month in range(1, 13) for day in range(1, 32) if day <= 31}
    fechas.update({f"{day:02d}{month:02d}{str(year)[-2:]}" for year in range(1960, 2051) for month in range(1, 13) for day in range(1, 32) if day <= 31})
     
    for word in words:
        if len(word) <= max_len:
            result.add(word.lower())
            result.add(word.upper())
            result.add(word.title())
            
            for i in range(1000):
                new_word = f"{word}{i}"
                if len(new_word) <= max_len:
                    result.add(new_word)
            
            leetspeak = (word.lower()
                        .replace('a', '4')
                        .replace('e', '3')
                        .replace('i', '1')
                        .replace('o', '0')
                        .replace('s', '5'))
            if len(leetspeak) <= max_len:
                result.add(leetspeak)
            
            if include_special:
                for char in special_chars:
                    new_word = f"{word}{char}"
                    if len(new_word) <= max_len:
                        result.add(new_word)
                        result.add(f"{char}{word}")
    
    words_list = list(words)

    
    if not words_list:
        return result  

    for _ in range(min(len(words_list) * 10, 5000)):
        word1 = random.choice(words_list)
        word2 = random.choice(words_list)
        combined = f"{word1}y{word2}"
        if len(combined) <= max_len:
            result.add(combined.lower())
         
            for fecha in fechas:
                combined_with_date = f"{combined}_{fecha}"
                if len(combined_with_date) <= max_len:
                    result.add(combined_with_date.lower())

        for sign in ['*', '&']:
            combined_with_sign = f"{word1}{sign}{word2}"
            if len(combined_with_sign) <= max_len:
                result.add(combined_with_sign.lower())             

    for _ in range(5000):
        seq_10_upper = ''.join(random.choices(chars_upper, k=10))
        seq_10_lower = ''.join(random.choices(chars_lower, k=10))
        result.add(seq_10_upper)
        result.add(seq_10_lower)

        seq_8_upper = ''.join(random.choices(chars_upper, k=8))
        seq_8_lower = ''.join(random.choices(chars_lower, k=8))
        result.add(seq_8_upper)
        result.add(seq_8_lower)

        seq_12_upper = ''.join(random.choices(chars_upper, k=12))
        seq_12_lower = ''.join(random.choices(chars_lower, k=12))
        result.add(seq_12_upper)
        result.add(seq_12_lower)             
    
    return result

def spinning_cursor():
    while not stop_spinner.is_set():
        for cursor in '|/-\\':
            sys.stdout.write(f'\r{cursor} Generando diccionario...')
            sys.stdout.flush()
            time.sleep(0.1)

def main():
    parser = argparse.ArgumentParser(description='Generador de diccionario en español')
    parser.add_argument('-s', action='store_true', help='Diccionario corto (20k palabras, max 8 chars)')
    parser.add_argument('-m', action='store_true', help='Diccionario mediano (100k palabras, max 12 chars)')
    parser.add_argument('-l', action='store_true', help='Diccionario completo (sin límite, max 20 chars)')
    args = parser.parse_args()

    print_banner()
    
    if args.s:
        max_len = 8
        max_words = 20000
        include_special = False
    elif args.m:
        max_len = 12
        max_words = 100000
        include_special = True
    else:  
        max_len = 20
        max_words = 800000  
        include_special = True

    base_words = load_base_words()
    
    global stop_spinner
    stop_spinner = threading.Event()
    spinner_thread = threading.Thread(target=spinning_cursor)
    spinner_thread.start()

    try:
        wordlist = generate_combinations(base_words, max_len, include_special)
        
        if max_words:
            wordlist = set(list(wordlist)[:max_words])
        
        timestamp = int(time.time())
        filename = f'spanish-dict_{timestamp}.txt'
        
        with open(filename, 'w', encoding='utf-8') as f:
            for word in sorted(wordlist):
                f.write(f"{word}\n")
        
        print(f"\nDiccionario generado con {len(wordlist)} palabras")
        print(f"Archivo guardado como: {filename}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        
        stop_spinner.set()
        spinner_thread.join()  

        
        sys.stdout.write('\r' + ' ' * 30 + '\r')
        sys.stdout.flush()  

if __name__ == "__main__":
    main()