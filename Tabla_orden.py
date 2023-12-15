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
def crear_orden():
    id = entry_id.get()
    fecha_solicitud = entry_fecha_solicitud.get()
    fecha_ingreso_sistema = entry_fecha_ingreso_sistema.get()
    medico_tratante = entry_medico_tratante.get()
    numero_orden_medico = entry_numero_orden_medico.get()


    try:
        cursor.execute("INSERT INTO Orden (id, fecha_solicitud, fecha_ingreso_sistema, medico_tratante, numero_orden_medico) VALUES (%s, %s, %s, %s, %s)", (id, fecha_solicitud, fecha_ingreso_sistema, medico_tratante, numero_orden_medico))
        conexion.commit()
        messagebox.showinfo(message="Registro exitoso", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al registrar", title="Error")

def leer_orden():
    id = entry_id.get()
    cursor.execute("SELECT * FROM Orden WHERE id = %s", (id))
    row = cursor.fetchone()
    if row is not None:
        listbox.delete(0, END)  # Borra el contenido actual del Listbox
        listbox.insert(END, row)  # Añade el nuevo registro al Listbox
    else:
        messagebox.showinfo(message="No se encontró el registro", title="Error")

def actualizar_orden():
    id = entry_id.get()
    fecha_solicitud = entry_fecha_solicitud.get()
    fecha_ingreso_sistema = entry_fecha_ingreso_sistema.get()
    medico_tratante = entry_medico_tratante.get()
    numero_orden_medico = entry_numero_orden_medico.get()

    try:
        cursor.execute("UPDATE Orden SET  fecha_solicitud = %s, fecha_ingreso_sistema = %s, medico_tratante = %s, numero_orden_medico = %s WHERE id = %s", (fecha_solicitud, fecha_ingreso_sistema, medico_tratante, numero_orden_medico, id))
        conexion.commit()
        messagebox.showinfo(message="Actualización exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al actualizar", title="Error")

def borrar_orden():
    id = entry_id.get()
    try:
        cursor.execute("DELETE FROM Orden WHERE id = %s", (id))
        conexion.commit()
        listbox.delete(0, END) 
        messagebox.showinfo(message="Eliminación exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al eliminar", title="Error")

#interfaz grafica

root = Tk()
root.title("CRUD ORDEN")
root.geometry("400x400")


Label(root, text="Id:").grid(row=0, column=0)
entry_id = Entry(root)
entry_id.grid(row=0, column=1)

Label(root, text="Fecha Solicitud:").grid(row=1, column=0)
entry_fecha_solicitud = Entry(root)
entry_fecha_solicitud.grid(row=1, column=1)

Label(root, text="Fecha ingreso sistema:").grid(row=2, column=0)
entry_fecha_ingreso_sistema = Entry(root)
entry_fecha_ingreso_sistema.grid(row=2, column=1)

Label(root, text="Medico tratante (Cedula):").grid(row=3, column=0)
entry_medico_tratante = Entry(root)
entry_medico_tratante.grid(row=3, column=1)

Label(root, text="numero orden medico:").grid(row=4, column=0)
entry_numero_orden_medico = Entry(root)
entry_numero_orden_medico.grid(row=4, column=1)


frame_botones = Frame(root)
frame_botones.grid(row=8, column=0, columnspan=2)


boton_crear = Button(frame_botones, text="Crear", command=crear_orden)
boton_crear.pack(side="left")

boton_leer = Button(frame_botones, text="Leer", command=leer_orden)
boton_leer.pack(side="left")

boton_actualizar = Button(frame_botones, text="Actualizar", command=actualizar_orden)
boton_actualizar.pack(side="left")

boton_borrar = Button(frame_botones, text="Eliminar", command=borrar_orden)
boton_borrar.pack(side="left")

listbox = Listbox(root)
listbox.grid(row=20, column=1, columnspan=2)

root.mainloop()