
import psycopg2
from Pelicula import *

class Conexion:

    def __init__(self) :
        
        self.conexion = psycopg2.connect(user = 'postgres',
                                    password = '14074871G',
                                    host = '127.0.0.1',
                                    port = '5432',
                                    database = 'Carteleras'
                                    )
    def __str__(self):

        datos = self.consultarPeliculas()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consultarPeliculas(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM peliculas"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()
        return datos




