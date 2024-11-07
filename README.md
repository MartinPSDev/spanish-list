# Spanish List 

![image](./screenshot.png)

**Generador de diccionarios en español**

Este script Python crea diccionarios en español con un enfoque en el vocabulario argentino, pero es fácilmente adaptable a cualquier región.
Sientete libre modificar el codigo y agregar las palabras que sean necesarias de acuerdo a tu ciudad, estado, pais.
Puedes agregar, si es necesario, centros educativos, cafeterias, equipos deportivos, nombres, apodos (nick) que creas conveniente.


## Características
* **Tres tamaños de diccionario:** Short (20K palabras), Medium (100K palabras) y Large (todas las combinaciones posibles).
* **Personalizable:** Agrega tus propias palabras para adaptar el diccionario a tus necesidades específicas.
* Se limitó el maximo de palabras en la opcion por defecto a 500.000 palabras por temas de rendimiento. Si su cpu lo permite puede modificar
    la linea 275 donde dice max_words = 500000 y aumentarlo si lo desea


## Uso
```bash
chmod +x spanish_list.py
python spanish_list.py  # sin parametros genera todas las combinaciones posibles
-s # genera 20.000 palabras
-m # genera 100.000 palabras 
