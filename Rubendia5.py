################################### raspberry############################

import Rpi .    GPIO as gpio # libreria para utilizar los puertos de entrada 

from time import sleep  # es para dar pausas 

led1 = 23         # definimos los pines de GPIO a utilizar

gpio . setmode(gpio . BCM) # modo BCM de la raspberry pi (Broadcom soc channel)

gpio . setup(led1, gpio . out)  # configuramos los puertos conectados a los leds como salida

while True:                 # bucle infinito
    gpio . out(led1,True)              # encendemos el led
    sleep(1)                            # paus de un segundo
    gpio . output(led1 , False)         # apagamos el led1
    sleep(1)                            # pausa de un segundo

    ###########################################################################################
    

while true: 
    condicion = gpio.input(entrada)
    sleep(0.3)
    if condicion==True: # si se preciona es true . entra en esa linea 

        contador = contador + 1   #aumentamos la variable contador   
        # como solo tenemos un led , contador debe tomar los valores 0 , 1
        if contador = 2:
            contador=0 # pero usamos el 0 para apagar el led 
    if contador ==0:
        gpio.output(led1,False)               # apagamos el led1
    if contador==1:
        gpio.output(led1,True)                #  encendemos el led


        # ejercicio: con la primera pulsacion , encender solo el primer led 
        #            con la segunda pulsacion , ensencder solo el segundo led 
        #             con la tercera pulsacion , enceder solo el tercer led 
        #            conla cuarta pulsacion , apagar todo...................

        