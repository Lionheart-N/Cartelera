from tkinter import *
from tkinter import ttk

class Ventana(Frame):

    def __init__(self, master = None):
        super().__init__(master, width= 680,height=260)
        self.master = master
        self.pack()
        self.crear_widgets()

    def fNueva(self):
        pass

    def fModificar(self):
        pass

    def fEliminar(self):
        pass

    def fGuardar(self):
        pass

    def fCancelar(self):
        pass
    
    def crear_widgets(self):
        frameUno = Frame(self, bg="#bfdaff")
        frameUno.place(x=0, y=0, width=93, height=259)

        self.btnNueva = Button(frameUno,text="Nueva", command= self.fNueva,bg="blue",fg = "white")
        self.btnNueva.place(x=5,y=50, width= 80, height=30)

        self.btnModificar = Button(frameUno,text="Modificar", command= self.fModificar,bg="blue",fg = "white")
        self.btnModificar.place(x=5,y=90, width= 80, height=30)

        self.btnEliminar = Button(frameUno,text="Eliminar", command= self.fEliminar,bg="blue",fg = "white")
        self.btnEliminar.place(x=5,y=130, width= 80, height=30)

        frameCrear = Frame(self, bg="#6c90fc")
        frameCrear.place(x=95, y=0, width=150, height=259)

        lblNombrePelicula = Label(frameCrear, text="Nombre de la pelicula")
        lblNombrePelicula.place(x=3, y=5)
        self.txtNombrePelicula = Entry(frameCrear)
        self.txtNombrePelicula.place(x=3, y=25, width=100, height=20)

        lblGenero = Label(frameCrear, text="Genero")
        lblGenero.place(x=3, y=55)
        self.txtGenero = Entry(frameCrear)
        self.txtGenero.place(x=3, y=75, width=100, height=20)

        lblDuracion = Label(frameCrear, text="Duracion")
        lblDuracion.place(x=3, y=105)
        self.txtDuracion = Entry(frameCrear)
        self.txtDuracion.place(x=3, y=125, width=100, height=20)

        lblAño = Label(frameCrear, text="Año")
        lblAño.place(x=3, y=155)
        self.txtGenero = Entry(frameCrear)
        self.txtGenero.place(x=3, y=175, width=100, height=20)

        self.btnGuardar = Button(frameCrear,text="Guardar", command= self.fGuardar,bg="green",fg = "white")
        self.btnGuardar.place(x=10,y=210, width= 60, height=30)

        self.btnCancelar = Button(frameCrear,text="Cancelar", command= self.fCancelar,bg="red",fg = "white")
        self.btnCancelar.place(x=80,y=210, width= 60, height=30)

        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4"))

        self.grid.column("#0",width=50, anchor=CENTER)
        self.grid.column("col1",width=130, anchor=CENTER)
        self.grid.column("col2",width=50, anchor=CENTER)
        self.grid.column("col3",width=50, anchor=CENTER)
        self.grid.column("col4",width=50, anchor=CENTER)
  
        self.grid.heading("#0",text="id", anchor=CENTER)
        self.grid.heading("col1",text="nombrePelicula", anchor=CENTER)
        self.grid.heading("col2",text="genero", anchor=CENTER)
        self.grid.heading("col3",text="duracion", anchor=CENTER)
        self.grid.heading("col4",text="año", anchor=CENTER)

        self.grid.place(x=247,y=0, width=420, height=259)

        self.grid.insert("", END, text="1", values=("Batman","Accion","180","2001"))


