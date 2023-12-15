
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
def crear_paciente():
    cedula = entry_cedula.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    POS = entry_POS.get()
    telefono = entry_telefono.get()
    celular = entry_celular.get()
    correo_electronico = entry_correo_electronico.get()
    nombre_contacto = entry_nombre_contacto.get()
    telefono_contacto = entry_telefono_contacto.get()

    try:
        cursor.execute("INSERT INTO Paciente (cedula, fecha_nacimiento, POS, telefono, celular, correo_electronico, nombre_contacto, telefono_contacto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (cedula, fecha_nacimiento, POS, telefono, celular, correo_electronico, nombre_contacto, telefono_contacto))
        conexion.commit()
        messagebox.showinfo(message="Registro exitoso", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al registrar", title="Error")

def leer_paciente():
    cedula = entry_cedula.get()
    cursor.execute("SELECT * FROM Paciente WHERE cedula = %s", (cedula,))
    row = cursor.fetchone()
    if row is not None:
        listbox.delete(0, END)  # Borra el contenido actual del Listbox
        listbox.insert(END, row)  # Añade el nuevo registro al Listbox
    else:
        messagebox.showinfo(message="No se encontró el registro", title="Error")

def actualizar_paciente():
    cedula = entry_cedula.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    POS = entry_POS.get()
    telefono = entry_telefono.get()
    celular = entry_celular.get()
    correo_electronico = entry_correo_electronico.get()
    nombre_contacto = entry_nombre_contacto.get()
    telefono_contacto = entry_telefono_contacto.get()

    try:
        cursor.execute("UPDATE Paciente SET fecha_nacimiento = %s, POS = %s, telefono = %s, celular = %s, correo_electronico = %s, nombre_contacto = %s, telefono_contacto = %s WHERE cedula = %s", (fecha_nacimiento, POS, telefono, celular, correo_electronico, nombre_contacto, telefono_contacto, cedula))
        conexion.commit()
        messagebox.showinfo(message="Actualización exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al actualizar", title="Error")

def borrar_paciente():
    cedula = entry_cedula.get()
    try:
        cursor.execute("DELETE FROM Paciente WHERE cedula = %s", (cedula,))
        conexion.commit()
        listbox.delete(0, END) 
        messagebox.showinfo(message="Eliminación exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al eliminar", title="Error")

#interfaz grafica

root = Tk()
root.title("CRUD PACIENTE")
root.geometry("400x400")


Label(root, text="Cédula:").grid(row=0, column=0)
entry_cedula = Entry(root)
entry_cedula.grid(row=0, column=1)

Label(root, text="Fecha de nacimiento:").grid(row=1, column=0)
entry_fecha_nacimiento = Entry(root)
entry_fecha_nacimiento.grid(row=1, column=1)

Label(root, text="POS:").grid(row=2, column=0)
entry_POS = Entry(root)
entry_POS.grid(row=2, column=1)

Label(root, text="Teléfono:").grid(row=3, column=0)
entry_telefono = Entry(root)
entry_telefono.grid(row=3, column=1)

Label(root, text="Celular:").grid(row=4, column=0)
entry_celular = Entry(root)
entry_celular.grid(row=4, column=1)

Label(root, text="Correo electrónico:").grid(row=5, column=0)
entry_correo_electronico = Entry(root)
entry_correo_electronico.grid(row=5, column=1)

Label(root, text="Nombre de contacto:").grid(row=6, column=0)
entry_nombre_contacto = Entry(root)
entry_nombre_contacto.grid(row=6, column=1)

Label(root, text="Teléfono de contacto:").grid(row=7, column=0)
entry_telefono_contacto = Entry(root)
entry_telefono_contacto.grid(row=7, column=1)


frame_botones = Frame(root)
frame_botones.grid(row=8, column=0, columnspan=2)


boton_crear = Button(frame_botones, text="Crear", command=crear_paciente)
boton_crear.pack(side="left")

boton_leer = Button(frame_botones, text="Leer", command=leer_paciente)
boton_leer.pack(side="left")

boton_actualizar = Button(frame_botones, text="Actualizar", command=actualizar_paciente)
boton_actualizar.pack(side="left")

boton_borrar = Button(frame_botones, text="Eliminar", command=borrar_paciente)
boton_borrar.pack(side="left")

listbox = Listbox(root)
listbox.grid(row=20, column=1, columnspan=2)

root.mainloop()
