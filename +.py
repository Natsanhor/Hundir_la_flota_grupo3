
import numpy as np
import random 

class Tablero :
    def __init__(self , id_jugador, filas=10, columnas=10 , agua="~"):
        self.filas = filas
        self.columnas = columnas
        self.id_jugador = id_jugador
        self.agua = agua
        self.crear_tablero()  # lo creamos directamente al iniciar

    def crear_tablero(self):
        self.tablero = np.full((self.filas, self.columnas), self.agua)
        self.tablero_mascara = np.full((self.filas, self.columnas), self.agua)
        return self.tablero
    
    def coloca_barco(self, barco):
        """Coloca un barco si es válido. Devuelve tablero o False."""
        tablero_temp = self.tablero.copy()

        for fila, columna in barco:
            if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas:
                print(f"No puedo poner la pieza {fila,columna}: fuera del tablero")
                return False
            
            if self.tablero[fila, columna] == "O":  
                print(f"No puedo poner la pieza {fila,columna}: ya hay un barco")
                return False

            tablero_temp[fila, columna] = "O"

        self.tablero = tablero_temp  # guardamos el cambio
        return self.tablero

    def recibir_disparo(self, coordenadas):
        fila, columna = coordenadas

        if self.tablero[fila, columna] == "O":
            self.tablero[fila, columna] = "X"
            print("Tocado")

        elif self.tablero[fila, columna] == self.agua:
            self.tablero[fila, columna] = "-"
            print("Agua")
        else:
            print("Ya has disparado aquí")


class Barco:

    def __init__(self, nombre, eslora, id_jugador):
        self.nombre = nombre
        self.eslora = eslora
        self.id_jugador = id_jugador

    def crea_barco_aleatorio(self, tablero, num_intentos=100):
        """Genera posiciones válidas y coloca el barco."""

        for intento in range(num_intentos):

            barco = []

            fila_ini = random.randint(0, tablero.filas - 1)
            col_ini = random.randint(0, tablero.columnas - 1)

            orientacion = random.choice(["N", "S", "E", "O"])
            fila, col = fila_ini, col_ini

            barco.append((fila, col))

            for _ in range(self.eslora - 1):

                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "E":
                    col += 1
                elif orientacion == "O":
                    col -= 1

                barco.append((fila, col))

            # Intentamos colocarlo
            resultado = tablero.coloca_barco(barco)

            if isinstance(resultado, np.ndarray):
                print(f"Barco {self.nombre} colocado en:", barco)
                return barco

        print("No se pudo colocar el barco tras muchos intentos.")
        return False
    

tablero_jugador = Tablero("jugador")
tablero_maquina = Tablero("maquina")

# barco1 = Barco("Destructor", 3, "jugador")
# barco2 = Barco("Pesquero", 1, "jugador")

# barco1.crea_barco_aleatorio(tablero_jugador)
# barco2.crea_barco_aleatorio(tablero_jugador)

# print(tablero_jugador.tablero)

barcos = {
    "lancha1": 1,
    "lancha2": 1,
    "lancha3": 1,
    "lancha4": 1,
    "patrullero1": 2,
    "patrullero2": 2,
    "patrullero3": 2,
    "submarino1": 3,
    "submarino2": 3,
    "acorazado": 4
}

# COLOCAMOS TODOS LOS BARCOS
for nombre, eslora in barcos.items():
    barco = Barco(nombre, eslora, "jugador")
    barco.crea_barco_aleatorio(tablero_jugador)

print(tablero_jugador.tablero)


