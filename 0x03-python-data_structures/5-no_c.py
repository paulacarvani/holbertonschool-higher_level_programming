#!/usr/bin/python3
def no_c(my_string):
    return my_string.translate(str.maketrans(dict.fromkeys('cC')))

# str.maketrans permite crear una tabla que será usada para substituir 
# cada carácter por el que le corresponda. Recibe un diccionario dónde 
# las parejas clave: valor son:
# caracter_a_substituir: carácter que lo substituye 
# como en este caso queremos eliminarlos basta con que sea de la forma:
# {"a": None, "b": None, ...}
# que es lo que crea dict.fromkeys('aeiouAEIOUüáéíóúÜÁÉÍÓÚ'). 
# Por su lado str.maketrans retorna un diccionario similar pero 
# convirtiendo las claves en valores numéricos (codepoints unicode 
# de cada carácter).
# str.translate se limita a recorrer la cadena y usar la tabla para 
# cambiar cada carácter por el que le pertenece, retornando la nueva 
# cadena al terminar.
