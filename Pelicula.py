class Pelicula:
    
    def __init__(self, nombre,genero,duracion,año, codigo):
        self.nombre = nombre;
        self.genero = genero;
        self.duracion = duracion;
        self.año = año;
        self.codigo = codigo;

    def setNombre(self):
        return self.nombre;

    def setGenero(self):
        return self.genero;

    def setDuracion(self):
        return self.duracion;

    def setAño(self):
        return self.año;

    def setCodigo(self):
        return self.codigo;