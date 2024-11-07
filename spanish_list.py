#!/usr/bin/env python3
import argparse
import itertools
import random
import string
import time
from typing import List, Set

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
    
    lugares = {
        "buenosaires", "cordoba", "rosario", "mendoza", "laplata", "quilmes", "lanus",
        "avellaneda", "sanisidro", "tigre", "pilar", "moron", "municipio", "municipalidad",
        "salta", "tucuman", "neuquen", "bariloche", "mardelplata", "tandil",
        "catamarca", "chaco", "chubut", "corrientes", "entre rios", "formosa", 
        "jujuy", "lapampa", "larioja", "misiones", "neuquen", "rionegro", 
        "san juan", "san luis", "santa cruz", "santa fe", "santiago del estero", 
        "tierradelfuego", "tucuman", "rosario", "san fernando", "san miguel", "moron", 
        "tresdefebrero", "berazategui", "berisso", "lomasdezamora", "sanmartin", "marcospaz", 
        "caba", "villamaria", "bahia blanca", "parana", "posadas", "las heras", "calafate", "sanrafael", "sanjuan", 
        "tigre", "salta", "chaco", "gualeguaychu", "general roca", "trelew", "rawson", 
        "bernal", "sanvicente", "carrilobo", "bellville", "embalse", "chaque", "comodoro rivadavia",
        "viedma", "sanbernardo", "puntaalta", "villagesell", "bellavista", "villaelisa", "algarrobo", "santarosa", 
        "sanmartindelosandes", "villamaría", "villadelparque", "alvear", "lacañada", 
        "santa rosa", "elcalafate", "generalpico", "necochea", "tigre", "colón", "laprida", "mardelplata"
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
        "huracan", "talleres", "belgrano", "banfield", "lanus", "cabj", "carp", "casla",
        "cai", "platense", "ferro", "chicago", "godoycruz", "argentinos", "argentinosjuniors",
        "ferro", "ferrocarriloeste"
    }
    
    años = {str(year) for year in range(1900, 2050)}
    
    comercios = {
        "shopping", "unicenter", "abasto", "altoplata", "dotbaires", 
        "galeria", "plaza", "terminal", "estacion", "aeropuerto", 
        "alcorta", "santafeshopping", "devotoshopping", "paseoquilmes", 
        "madero shopping", "paseo la plaza", "paseo rosa", "paseozonanorte", 
        "shopping sur", "liniers", "shopping norte", "paseodelsol", 
        "buenavista shopping", "caballito shopping", "rosarioshopping", "lomasshopping", 
        "open 25", "cinepolis", "cinemark", "cines outlet", "palermo", "villages", 
        "rivadavia", "megatone", "gondolas", "mi ciudad", "falabella", "carrefour", 
        "easy", "sodimac", "coto", "disco", "jumbo", "lidl", "walmart", "yaguaron", 
        "musimundo", "pepsi", "laanonima", "thegallery", "despensa", "supermercado", 
        "unilac", "supermercados dia", "galeria zona sur", "compumundo", "i-store", 
        "la vida", "particular", "tacito", "danone", "tarea", "electro", "luis borges", 
        "factura", "maxi", "starbucks", "cafemartinez", "café de la plaza", "lattente", 
        "tucan", "café tortoni", "la panerarosa", "librosycafe", "mundocafe", 
        "teaconnection", "cafebolivar", "elclubdelamilanesa", "donado", "terraza", 
        "lacasadelte", "cafevinilo", "peña", "elhornero", "bocacafé", "bonafide", 
        "garbarino", "compumundo", "fravega", "mueblesdico", "personal", "movistar", 
        "claro", "net", "fibertel", "cablevision", "apple", "samsung", "lg", "hp", 
        "motorola", "lenovo", "dell", "asus", "acer", "xbox", "playstation", "microsoft", 
        "logitech", "kaspersky", "casio", "alcatel", "eurocom", "blu", "toshiba", 
        "ropa", "nike", "adidas", "lacoste", "le coq sportif", "puma", "reebok", 
        "complot", "cdg", "zara", "bershka", "stradivarius", "pullandbear", "gap", 
        "h&m", "mango", "kenzo", "emporioarmani", "valentino", "dior", "chanel", 
        "arcor", "marihuana", "cocacola", "fanta", "pepsi", "cerveza quilmes", 
        "heineken", "swiss", "emporio", "grido", "candy", "toblerone", "nescafé", 
        "nestlé", "lascarmelitas", "kellogg's", "molinos", "latam", "rio", 
        "easy", "sodimac", "homecenter", "falabella", "todohogar", "lafam", "tiendanaranja", 
        "mc donalds", "burgerking", "subway", "dominos", "kfc", "sushiroll", 
        "lasaña", "la parrilla", "pizzeta", "las canteras", "tequila", "helados", 
        "vips", "sushi", "la cadena", "tacobar", "bakery", "centrococina", "sushi", 
        "correoargentino", "andreani", "ocasa", "mercadolibre", "jotabe", 
        "cargill", "francini", "ypf", "shell", "pampaenergia", "telecom","lagaleria"
    }

    universidades = {
        "uba", "utn", "universidaddebuenosaires", "universidadnacionaldelaplata",
        "universidad nacional de cordoba", "universidad de la matanza", "universidadcatolica",
        "uca","um","uno","unlam","unahur","uade","up","usal","unlu","uflo","ub","untref","unsam",
        "colegio", "escuela", "escuela tecnica","unla","uai"
    }
     
    apellidos = {
        "perez", "lopez", "ramirez", "soto", "nunez", "gonzalez", "fernandez", "martinez", 
        "rodriguez", "diaz", "torres", "castro", "vazquez", "morales", "jimenez", 
        "hernandez", "pineda", "salazar", "mendoza", "carrillo", "sandoval","nuñez","castro"
    }

    nicknames = {
        "tincho", "rodo", "fran", "licha", "pato", "guille", "pipa", "tato", "chino", "lucho",
        "rama","pancho", "santi", "joaco", "rulo", "pela", "mudo", "negro", "colo", "pipi"
    }

    fechas = {f"{day:02d}{month:02d}{year}" for year in range(1960, 2051) for month in range(1, 13) for day in range(1, 32) if day <= 31}
    fechas.update({f"{day:02d}{month:02d}{str(year)[-2:]}" for year in range(1960, 2051) for month in range(1, 13) for day in range(1, 32) if day <= 31})

    frases_cortas = {
        "laverdadnoslibera", "eltiempopasa", "nuncasabremos", "siguetusalud", 
        "unmundomejor", "lavidaesbella", "nuncasinsentido", "elamorvence", 
        "sueñosyrealidad", "juntosporsiempre", "teamo","elamordemivida","miamor"
    }

    return nombres | lugares | empresas | deportes | años | comercios | universidades | apellidos | nicknames | fechas | frases_cortas

def generate_combinations(words: Set[str], max_len: int, include_special: bool) -> Set[str]:
    result = set()
    chars = string.ascii_letters + string.digits
    special_chars = "!@#$%^&*-_+=."

    if include_special:
        chars += special_chars

    for word in words:
        if len(word) <= max_len:
            result.add(word.lower())
            result.add(word.upper())
            result.add(word.title())

            for i in range(1000):
                new_word = f"{word}{i}"
                if len(new_word) <= max_len:
                    result.add(str(new_word))  

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
                        result.add(str(new_word))
                        result.add(str(f"{char}{word}"))
    words_list = list(words)
    for _ in range(min(len(words_list) * 10, 5000)):
        word1 = random.choice(words_list)
        word2 = random.choice(words_list)
        combined = f"{word1}y{word2}"
        if len(combined) <= max_len:
            result.add(combined.lower())
    
    for _ in range(5000):
        length = random.randint(6, max_len)
        random_str = ''.join(random.choices(chars, k=length))
        result.add(random_str)
    
    return result

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
        max_words = None
        include_special = True

    base_words = load_base_words()
    wordlist = generate_combinations(base_words, max_len, include_special)
    
    if max_words:
        wordlist = set(list(wordlist)[:max_words])
    
    timestamp = int(time.time())
    filename = f'spanish-dict_{timestamp}.txt'
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for word in sorted(wordlist):
                f.write(f"{word}\n")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
    
    print(f"\nDiccionario generado con {len(wordlist)} palabras")
    print(f"Archivo guardado como: {filename}")

if __name__ == "__main__":
    main()