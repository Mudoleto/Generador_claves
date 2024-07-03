#!/usr/bin/env python

#Librerias.
import string
import random
import optparse
import secrets

#Longitud de la clave.
longitud = 0

#Lista vacia para almacenar los caracteres.
clave = []

#Optencion de argumentos para trabajar.
def get_arguments():
    parser = optparse.OptionParser()
    
    
    parser.add_option("-n", "--numeros", dest="numeros",
                    help="Solo numeros o con numeros")
    
    parser.add_option("-m", "--mayusculas", dest="mayusculas",
                    help="Solo mayusculas")
    
    parser.add_option("-l", "--minusculas", dest="minusculas",
                    help="Solo minusculas")
    
    parser.add_option("-s", "--especiales", dest="especiales",
                    help="Clave especial")
    
    (options, arguments) = parser.parse_args()
    
    if not options.numeros and not options.mayusculas and not options.minusculas and not options.especiales:
        parser.error("[-] Proporcione al menos un argumento. Utilce el comando --help para obtener mas informacion")
    return options

def generador_clave_numerica(longitud):
    longitud = int(longitud)
    
    for i in range(longitud):
        numero_random = random.randint(0,9)
        clave.append(str(numero_random))
    
    s = ''.join(clave)
    return s

def generador_clave_mayusculas(longitud):
    longitud = int(longitud)
    
    for i in range(longitud):
        clave.append(random.choice(string.ascii_uppercase))
    
    s = ''.join(clave)
    return s
    
def generador_clave_minusculas(longitud):
    longitud = int(longitud)
    
    for i in range(longitud):
        clave.append(random.choice(string.ascii_lowercase))
    
    s = ''.join(clave)
    return s

def generador_clave_especial(longitud):
    longitud = int(longitud)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    clave.append(random.choice(string.ascii_lowercase))
    clave.append(random.choice(string.ascii_uppercase))
    clave.append(random.choice(string.digits))
    clave.append(random.choice(string.punctuation))

    while len(clave) < longitud:
        clave.append(secrets.choice(caracteres))
        
    s = ''.join(clave)
    return s

if __name__ == "__main__":
    options = get_arguments()
    
    if options.numeros:
        password = generador_clave_numerica(options.numeros)
        print("Tu clave numerica es:{}".format(password))
        
    elif options.mayusculas:
        password = generador_clave_mayusculas(options.mayusculas)
        print("Tu clave en letras mayusculas:{}".format(password))
    
    elif options.minusculas:
        password = generador_clave_minusculas(options.minusculas)
        print("Tu clave en letras minusculas:{}".format(password))
    
    elif options.especiales:
        password = generador_clave_especial(options.especiales)
        print("Tu clave especial es:{}".format(password))
