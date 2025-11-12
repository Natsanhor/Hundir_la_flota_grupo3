from clases import Tablero
from funciones import mostrar_tablero
from variables import TAMANO
import random

print(" Bienvenido a Hundir la Flota ")

# Inicializar tableros
jugador = Tablero("Jugador")
maquina = Tablero("Máquina")
jugador.inicializar_barcos()
maquina.inicializar_barcos()

turno_jugador = True
juego_activo = True

while juego_activo:
    if turno_jugador:
        print("\n Tu tablero:")
        mostrar_tablero(jugador.tablero_barcos)
        print("\n Tablero enemigo:")
        mostrar_tablero(maquina.tablero_disparos)
        
        except:
            print("Introduce coordenadas válidas.")
    else:
        # Turno de la máquina
    

    # Comprobar si alguien ha ganado
  