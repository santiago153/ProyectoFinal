from tkinter import messagebox
import psycopg2
from tkinter import *

#conexion a base de datos:
conexion = psycopg2.connect(user='postgres',
                            password='pgsql',
                            host='127.0.0.1',
                            port='5432',
                            database='LaboratorioClinicoPruebas')

cursor=conexion.cursor()

#Funciones crear,borrar,leer,actualizar
def crear_medico():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    especialidad = entry_especialidad.get()
    

    try:
        cursor.execute("INSERT INTO Medico (cedula, nombre, apellido, telefono, direccion, especialidad) VALUES (%s, %s, %s, %s, %s, %s)", (cedula, nombre, apellido, telefono, direccion, especialidad))
        conexion.commit()
        messagebox.showinfo(message="Registro exitoso", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al registrar", title="Error")

def leer_medico():
    cedula = entry_cedula.get()
    cursor.execute("SELECT * FROM Medico WHERE cedula = %s", (cedula))
    row = cursor.fetchone()
    if row is not None:
        listbox.delete(0, END)  # Borra el contenido actual del Listbox
        listbox.insert(END, row)  # Añade el nuevo registro al Listbox
    else:
        messagebox.showinfo(message="No se encontró el registro", title="Error")

def actualizar_medico():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    especialidad = entry_especialidad.get()

    try:
        cursor.execute("UPDATE Medico SET nombre = %s, apellido = %s, telefono = %s, direccion = %s, especialidad = %s WHERE cedula = %s", (nombre, apellido, telefono, direccion, especialidad, cedula))
        conexion.commit()
        messagebox.showinfo(message="Actualización exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al actualizar", title="Error")

def borrar_medico():
    cedula = entry_cedula.get()
    try:
        cursor.execute("DELETE FROM Medico WHERE cedula = %s", (cedula,))
        conexion.commit()
        listbox.delete(0, END) 
        messagebox.showinfo(message="Eliminación exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al eliminar", title="Error")

#interfaz grafica

root = Tk()
root.title("CRUD MEDICO")
root.geometry("400x400")


Label(root, text="Cédula:").grid(row=0, column=0)
entry_cedula = Entry(root)
entry_cedula.grid(row=0, column=1)

Label(root, text="Nombre:").grid(row=1, column=0)
entry_nombre = Entry(root)
entry_nombre.grid(row=1, column=1)

Label(root, text="Apellido:").grid(row=2, column=0)
entry_apellido = Entry(root)
entry_apellido.grid(row=2, column=1)

Label(root, text="Teléfono:").grid(row=3, column=0)
entry_telefono = Entry(root)
entry_telefono.grid(row=3, column=1)

Label(root, text="Direccion:").grid(row=4, column=0)
entry_direccion = Entry(root)
entry_direccion.grid(row=4, column=1)

Label(root, text="Especialidad:").grid(row=5, column=0)
entry_especialidad = Entry(root)
entry_especialidad.grid(row=5, column=1)


frame_botones = Frame(root)
frame_botones.grid(row=8, column=0, columnspan=2)


boton_crear = Button(frame_botones, text="Crear", command=crear_medico)
boton_crear.pack(side="left")

boton_leer = Button(frame_botones, text="Leer", command=leer_medico)
boton_leer.pack(side="left")

boton_actualizar = Button(frame_botones, text="Actualizar", command=actualizar_medico)
boton_actualizar.pack(side="left")

boton_borrar = Button(frame_botones, text="Eliminar", command=borrar_medico)
boton_borrar.pack(side="left")

listbox = Listbox(root)
listbox.grid(row=20, column=1, columnspan=2)

root.mainloop()
