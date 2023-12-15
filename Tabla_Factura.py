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
def crear_factura():
    numero_factura = entry_numero_factura.get()
    valor_pagar = entry_valor_pagar.get()
    cedula_paciente= entry_cedula_paciente.get()
    fecha_realizacion= entry_fecha_realizacion.get()
    

    try:
        cursor.execute("INSERT INTO Factura (numero_factura, valor_pagar, cedula_paciente, fecha_realizacion) VALUES (%s, %s, %s, %s)", (numero_factura, valor_pagar, cedula_paciente, fecha_realizacion))
        conexion.commit()
        messagebox.showinfo(message="Registro exitoso", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al registrar", title="Error")

def leer_factura():
    numero_factura = entry_numero_factura.get()
    cursor.execute("SELECT * FROM Factura WHERE numero_factura = %s", (numero_factura))
    row = cursor.fetchone()
    if row is not None:
        listbox.delete(0, END)  # Borra el contenido actual del Listbox
        listbox.insert(END, row)  # Añade el nuevo registro al Listbox
    else:
        messagebox.showinfo(message="No se encontró el registro", title="Error")

def actualizar_factura():
    numero_factura = entry_numero_factura.get()
    valor_pagar = entry_valor_pagar.get()
    cedula_paciente= entry_cedula_paciente.get()
    fecha_realizacion= entry_fecha_realizacion.get()

    try:
        cursor.execute("UPDATE Medico SET  valor_pagar = %s, cedula_paciente = %s, fecha_realizacion = %s WHERE numero_factura = %s", (valor_pagar, cedula_paciente, fecha_realizacion, numero_factura))
        conexion.commit()
        messagebox.showinfo(message="Actualización exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al actualizar", title="Error")

def borrar_factura():
    numero_factura = entry_numero_factura.get()
    try:
        cursor.execute("DELETE FROM Factura WHERE numero_factura = %s", (numero_factura,))
        conexion.commit()
        listbox.delete(0, END) 
        messagebox.showinfo(message="Eliminación exitosa", title="Success")
    except Exception as e:
        messagebox.showinfo(message="Error al eliminar", title="Error")

#interfaz grafica

root = Tk()
root.title("CRUD Factura")
root.geometry("400x400")


Label(root, text="numero factura:").grid(row=0, column=0)
entry_numero_factura = Entry(root)
entry_numero_factura.grid(row=0, column=1)

Label(root, text="valor a pagar:").grid(row=1, column=0)
entry_valor_pagar = Entry(root)
entry_valor_pagar.grid(row=1, column=1)

Label(root, text="cedula paciente:").grid(row=2, column=0)
entry_cedula_paciente = Entry(root)
entry_cedula_paciente.grid(row=2, column=1)

Label(root, text="fecha realizacion:").grid(row=3, column=0)
entry_fecha_realizacion = Entry(root)
entry_fecha_realizacion.grid(row=3, column=1)



frame_botones = Frame(root)
frame_botones.grid(row=8, column=0, columnspan=2)


boton_crear = Button(frame_botones, text="Crear", command=crear_factura)
boton_crear.pack(side="left")

boton_leer = Button(frame_botones, text="Leer", command=leer_factura)
boton_leer.pack(side="left")

boton_actualizar = Button(frame_botones, text="Actualizar", command=actualizar_factura)
boton_actualizar.pack(side="left")

boton_borrar = Button(frame_botones, text="Eliminar", command=borrar_factura)
boton_borrar.pack(side="left")

listbox = Listbox(root)
listbox.grid(row=20, column=1, columnspan=2)

root.mainloop()
