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
def crear_examen():
    id = entry_id.get()
    tipo_examen = entry_tipo_examen.get()
    fecha_cita = entry_fecha_cita.get()
    fecha_realizacion = entry_fecha_realizacion.get()
    observaciones = entry_observaciones.get()
    orden_id = entry__orden_id.get()
    
    try:
        cursor.execute("INSERT INTO Examen (id, tipo_examen, fecha_cita, fecha_realizacion, observaciones, orden_id) VALUES (%s, %s, %s, %s, %s, %s)", (id, tipo_examen, fecha_cita, fecha_realizacion, observaciones, orden_id))
        conexion.commit()
        messagebox.showinfo(message="Registro exitoso", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al registrar", title="Error")

def leer_examen():
    id = entry_id.get()
    cursor.execute("SELECT * FROM Examen WHERE id = %s", (id))
    row = cursor.fetchone()
    if row is not None:
        listbox.delete(0, END)  # Borra el contenido actual del Listbox
        listbox.insert(END, row)  # Añade el nuevo registro al Listbox
    else:
        messagebox.showinfo(message="No se encontró el registro", title="Error")

def actualizar_examen():
    id = entry_id.get()
    tipo_examen = entry_tipo_examen.get()
    fecha_cita = entry_fecha_cita.get()
    fecha_realizacion = entry_fecha_realizacion.get()
    observaciones = entry_observaciones.get()
    orden_id = entry__orden_id.get()


    try:
        cursor.execute("UPDATE Examen SET tipo_examen = %s, fecha_cita = %s, fecha_realizacion = %s, observaciones = %s, orden_id = %s WHERE id = %s", (tipo_examen, fecha_cita, fecha_realizacion, observaciones, orden_id, id))
        conexion.commit()
        messagebox.showinfo(message="Actualización exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al actualizar", title="Error")

def borrar_examen():
    id = entry_id.get()
    try:
        cursor.execute("DELETE FROM Examen WHERE id = %s", (id))
        conexion.commit()
        listbox.delete(0, END) 
        messagebox.showinfo(message="Eliminación exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al eliminar", title="Error")

#interfaz grafica

root = Tk()
root.title("CRUD MEDICO")
root.geometry("400x400")


Label(root, text="id:").grid(row=0, column=0)
entry_id = Entry(root)
entry_id.grid(row=0, column=1)

Label(root, text="tipo de examen:").grid(row=1, column=0)
entry_tipo_examen = Entry(root)
entry_tipo_examen.grid(row=1, column=1)

Label(root, text="fecha de la cita:").grid(row=2, column=0)
entry_fecha_cita = Entry(root)
entry_fecha_cita.grid(row=2, column=1)

Label(root, text="fecha realizacion:").grid(row=3, column=0)
entry_fecha_realizacion = Entry(root)
entry_fecha_realizacion.grid(row=3, column=1)

Label(root, text="observaciones:").grid(row=4, column=0)
entry_observaciones = Entry(root)
entry_observaciones.grid(row=4, column=1)

Label(root, text="orden id:").grid(row=5, column=0)
entry__orden_id = Entry(root)
entry__orden_id.grid(row=5, column=1)


frame_botones = Frame(root)
frame_botones.grid(row=8, column=0, columnspan=2)


boton_crear = Button(frame_botones, text="Crear", command=crear_examen)
boton_crear.pack(side="left")

boton_leer = Button(frame_botones, text="Leer", command=leer_examen)
boton_leer.pack(side="left")

boton_actualizar = Button(frame_botones, text="Actualizar", command=actualizar_examen)
boton_actualizar.pack(side="left")

boton_borrar = Button(frame_botones, text="Eliminar", command=borrar_examen)
boton_borrar.pack(side="left")

listbox = Listbox(root)
listbox.grid(row=20, column=1, columnspan=2)

root.mainloop()
