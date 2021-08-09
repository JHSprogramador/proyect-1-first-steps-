import random
titulo = "Bienvenido a The innocents"

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

print("Era un niño muy chiquito me levante como otros dias y se me ocurrio mirar al cielo pero note que era de un color\n"
"rojo ademas logre ver a lo lejos una figura parecida a un humano pero llevaba una armadura muy pesada y de repente sus\n"
"ojos se prendieron de un color rojizo.\n")

opcion = input("¿Que haces? Llamar a tus padres (L) o quedartele mirando (R)\n")

if opcion == "L":
    print(
        "Mis padres se dieron cuenta que algo no estaba bien e inmediantamente nos refugiamos, en el refugio escuche un fuerte estruendo\n"
        "y vi como el suelo temblaba despues de que se calmo un poco sali y descubri que la mitad de la aldea estaba en llamas y destruida cuando \n"
        "vi eso el miedo recorrio mi  cuerpo en eso me agarro alguien por la espalda.\n")
    opcion = input("¿Te dejas agarrar? S/N\n")

    if opcion == "S":
        print("Era tu padre te agarro para escapar de ese lugar.")
        opcion = input("En lo que te lleva ves a lo lejos algo en la mesa ¿Detienes a tu padre para agarrarlo? S/N\n")

        llave_en_inventario = False


        if opcion == "S":
            print("Eran unas llaves las agarras.")
            llave_en_inventario = True

        elif opcion == "N":
            print("Tal vez nunca sabremos que era.")

        else:
            print("No pasa nada sigues con tu camino.")

        print("Entonces van al garage para ir a buscar el colibri (una moto futurista) pero el padre se da cuenta que\n"
              "no tiene las llaves entonces la familia se revisa los bolsillos.")

        if llave_en_inventario:
            print("En tu bolsillo agarras las llaves que recogiste antes, !Era la llave del colibri¡,lograron arrancar el colibri\n"
                  "y asi escapar parecia que todo ya habia acabado pero ven como el soldado esta destruyendo sin problemas sus defensas\n"
                  "a los soldados los atraviesa como mantequilla igual los cañones y torres de vigilancia eran de papel para el, pero nos distrajimos\n"
                  "y uno de los escombros envolvio la moto, con eso el se dio cuenta de nuestra presencia rapidamente corrimos al edificio cercano\n"
                  "era una estacion militar y vimos a lo lejos una vitrina con equipo pero esta protegida con una cerradura.")
            numero1 = random.randint(1, 10)
            numero2 = random.randint(1, 10)
            numero3 = random.randint(1, 10)

            clave1= input("Pon un numero para abrir la cerradura\n")
            clave2 = input("Pon otro numero para abrir la cerradura\n")
            clave3 = input("Pon un ultimo numero para abrir la cerradura\n")


            if (clave1 == numero1 and clave2 == numero2 and clave3 == numero3):
                print(
                    "Tienes mucha suerte con una escopeta le disparas al soldado pero lo esquiva y te quita el arma pero hay algo raro porque no los mata al instante?\n"
                    "de hecho aunque no se ven sus ojos da un aura de tristeza y se da la vuelta la madre le pregunta gritando que porque no los\n"
                    "asesina acaso es un juego cruel hacia ellos el soldado que viendolo de cerca el nombre viene a la mente a el lo llaman \n"
                    "La muerte roja les dice que solo mata soldados y no quiere crear otros mas su sueño es acabar con esta guerra y grito que lo\n"
                    "engañaron nos pidio perdon de rodillas hace un 10 años que paso eso y en ese momento lo unico que se me vino en la mente es\n"
                    "queria ser igual de fuerte y con sus valores que aquel guerro legendario mi nombre es plateus y soy un caido y acabare con\n"
                    "esta guerra.")



            else:
                print("No diste con la clave asi que indefensos el soldado se acerca a ustedes pero hay algo raro porque no nos mata al instante?\n"
                      "de hecho aunque no se ven sus ojos da un aura de tristeza y se da la vuelta mi madre le pregunta gritando que porque no nos\n"
                      "asesina acaso es un juego cruel, el soldado que viendolo de cerca su nombre me vino a la mente a el lo llaman \n"
                      "La muerte roja le respondio a mi madre que solo mata soldados y no quiere crear otros mas su sueño es acabar con esta guerra no alargarla y grito que lo\n"
                      "engañaron nos pidio perdon hace 10 años que paso eso y en ese momento lo unico que se me vino en la mente es\n"
                      "que queria ser igual de fuerte  que aquel guerro legendario mi nombre es plateus y soy un caido que acabara con esta guerra\n"
                      "esta guerra.")








        else:
            print("al parecer nadie traia las llaves la unica opcion era ir a buscarlas pero era muy peligroso terminaron mueriendo")


    if opcion == "N":
        print("Era tu padre pero gracias a esa accion perdieron tiempo valioso la destruccion alcanzo otra vez tu casa\n"              
              "y toda tu familia acabo hecha cenizas.")






elif opcion == "R":
    print("Ves como el misterioso soldado se levanta y le salen rayos de su cuerpo da un salto de varios metros \n"
          "y lo ultimo que ves es que golpea el suelo despues eres carbonizado con la mitad de tu aldea.")


else:
    print("No hiciste nada, moriste.")