import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time
from datetime import datetime, timedelta
import json
import os

class Camion:
 """
 Clase que representa un camión individual
 """
 def __init__(self, motor, patente, marca, modelo, ano, capacidad, km_camion, precio, tipo, peso_max):
  self.motor = motor
  self.patente = patente
  self.marca = marca
  self.modelo = modelo
  self.ano = ano
  self.capacidad = capacidad
  self.km_camion = km_camion
  self.precio =precio
  self.tipo = tipo
  self.peso_max = peso_max
  self.estado = "Disponible"
  self.ultima_mantencion = datetime.now()


 def necesita_mantencion(self, dias=30):
  """
  Determina si el camión necesita mantención basado en la última fecha.
  :param dias: Número de días entre mantenciones.
  :return: True si necesita mantención, False de lo contrario.
  """
  return datetime.now() - self.ultima_mantencion >= timedelta(days=dias)
    
 def arrendar(self):
  if self.estado == "Disponible":
   self.estado = "Arrendado"
   return True
  return False

 def realizar_mantencion(self, parte=None, detalles=None):
  """
  Realiza la mantención del camión, actualizando el estado de una parte específica.
  :param parte: La parte del camión que requiere reparación.
  :param detalles: Detalles adicionales sobre la reparación.
  """
  if parte:
   if parte == "capacidad":
    self.capacidad = f"{self.capacidad}" if detalles else "Reparado"
   elif parte == "kilometraje":
    self.km_camion = f"{self.km_camion}" if detalles else "Reparado"
   elif parte == "motor":
    None

   self.ultima_mantencion = datetime.now()

 def to_dict(self):
  return {
   "motor": self.motor.to_dict(),
   "patente": self.patente,
   "marca": self.marca,
   "modelo": self.modelo,
   "ano": self.ano,
   "capacidad": self.capacidad,
   "km_camion": self.km_camion,
   "precio": self.precio,
   "tipo": self.tipo,
   "peso_max": self.peso_max,
   "estado": self.estado,
   "ultima_mantencion": self.ultima_mantencion.isoformat(),
  }

 @staticmethod
 def from_dict(data):
  motor = Motor.from_dict(data["motor"])
  camion = Camion(
   motor, data["patente"], data["marca"], data["modelo"], data["ano"],
   data["capacidad"], data["km_camion"], data["precio"], data["tipo"], data["peso_max"]
  )
  camion.estado = data["estado"]
  camion.ultima_mantencion = datetime.fromisoformat(data["ultima_mantencion"])
  return camion

 def __str__(self):
  return (f"patente: {self.patente}, Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, "
          f"Volumen: {self.volumen}, Kilometraje: {self.kilometraje}, Precio: {self.precio}, "
          f"Tipo: {self.tipo}, Capacidad: {self.capacidad}, {self.motor}")

class Motor:
 def __init__(self, id, tipo, cilindrada, potencia, km_lt, vel_max, rendimiento, ult_rev):
  self.id = id
  self.tipo = tipo
  self.cilindrada = cilindrada
  self.potencia = potencia
  self.km_lt =km_lt
  self.vel_max = vel_max
  self.rendimiento = rendimiento
  self.ult_rev = ult_rev
  self.falla = False

 def to_dict(self):
  return {
   "id": self.id,
   "tipo": self.tipo,
   "cilindrada": self.cilindrada,
   "potencia": self.potencia,
   "km_lt": self.km_lt,
   "vel_max": self.vel_max,
   "rendimiento": self.rendimiento,
   "ult_rev": self.ult_rev,
   "falla": self.falla,
  }

 @staticmethod
 def from_dict(data):
  return Motor(
   data["id"], data["tipo"], data["cilindrada"], data["potencia"],
   data["km_lt"], data["vel_max"], data["rendimiento"], data["ult_rev"]
  )

 def __str__(self):
  return (f"id: {self.id}, Motor: {self.tipo}, cilindrada: {self.cilindrada},"
          f"Potencia: {self.potencia}, km_lt: {self.km_lt}, vel_max: {self.vel_max},"
          f"rendimiento: {self.rendimiento}, ult_rev: {self.ult_rev}")

class LoginApp(tk.Tk):  # Heredamos de Tk
 def __init__(self):
  super().__init__()  # Inicializamos la clase base Tk
  self.title("Inicio de sesión")
  # Cargar usuarios desde el archivo JSON (si existe)
  self.usuarios = self.cargar_usuarios()  
  # Preguntar si es usuario o administrador
  self.mostrar_tipo_usuario()
  # Método para cargar los usuarios desde el archivo JSON
  self.centrar_ventana(345, 280)  # Cambia el tamaño según tus necesidades
        # Preguntar si es usuario o administrador
  
 def centrar_ventana(self, ancho, alto):
        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        
        # Calcular la posición x e y para centrar
        x = (ancho_pantalla - ancho) // 2
        y = (alto_pantalla - alto) // 2
        
        
        # Establecer las dimensiones y posición de la ventana
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
 def cargar_usuarios(self):
  if os.path.exists("usuarios.json"):
   with open("usuarios.json", "r") as archivo:
    return json.load(archivo)
  return {}
 # Método para guardar los usuarios en el archivo JSON
 def guardar_usuarios(self):
  with open("usuarios.json", "w") as archivo:
   json.dump(self.usuarios, archivo, indent=4)
 # Método para limpiar la ventana
 def limpiar_ventana(self):
  # Limpiar los widgets existentes en la ventana
  for widget in self.winfo_children():
   widget.grid_forget()
 # Método para preguntar si desea entrar como usuario o administrador
 def mostrar_tipo_usuario(self):
  self.limpiar_ventana()
  # Mostrar opciones
  self.label_opcion = tk.Label(self, text="¿Quieres entrar como Usuario o Administrador?")
  self.label_opcion.grid(row=0, column=0, columnspan=2, pady=10)

  self.boton_usuario = tk.Button(self, text="Usuario", command=self.mostrar_inicio_sesion_usuario)
  self.boton_usuario.grid(row=1, column=0, padx=10, pady=10)

  self.boton_administrador = tk.Button(self, text="Administrador", command=self.mostrar_inicio_sesion_admin)
  self.boton_administrador.grid(row=1, column=1, padx=10, pady=10)

 # Método para mostrar la interfaz de inicio de sesión de usuario
 def mostrar_inicio_sesion_usuario(self):
  self.limpiar_ventana()

  # Crear los widgets de inicio de sesión para el usuario
  self.label_usuario = tk.Label(self, text="Usuario:")
  self.label_usuario.grid(row=0, column=0, padx=10, pady=10)

  self.entry_usuario = tk.Entry(self)
  self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)

  self.label_contrasena = tk.Label(self, text="Contraseña:")
  self.label_contrasena.grid(row=1, column=0, padx=10, pady=10)

  self.entry_contrasena = tk.Entry(self, show="*")
  self.entry_contrasena.grid(row=1, column=1, padx=10, pady=10)

  self.boton_iniciar_sesion = tk.Button(self, text="Iniciar sesión", command=self.verificar_credenciales_usuario)
  self.boton_iniciar_sesion.grid(row=2, column=0, columnspan=2, pady=10)

  self.boton_crear_usuario = tk.Button(self, text="Crear usuario", command=self.mostrar_crear_usuario)
  self.boton_crear_usuario.grid(row=3, column=0, columnspan=2, pady=10)

  self.boton_volver = tk.Button(self, text="Volver", command=self.mostrar_tipo_usuario)
  self.boton_volver.grid(row=4, column=0, columnspan=2, pady=10)

 # Método para mostrar la interfaz de inicio de sesión de administrador
 def mostrar_inicio_sesion_admin(self):
  self.limpiar_ventana()

  # Crear los widgets de inicio de sesión para el administrador
  self.label_admin_usuario = tk.Label(self, text="Usuario Admin:")
  self.label_admin_usuario.grid(row=0, column=0, padx=10, pady=10)

  self.entry_admin_usuario = tk.Entry(self)
  self.entry_admin_usuario.grid(row=0, column=1, padx=10, pady=10)

  self.label_admin_contrasena = tk.Label(self, text="Contraseña Admin:")
  self.label_admin_contrasena.grid(row=1, column=0, padx=10, pady=10)

  self.entry_admin_contrasena = tk.Entry(self, show="*")
  self.entry_admin_contrasena.grid(row=1, column=1, padx=10, pady=10)

  self.boton_iniciar_admin = tk.Button(self, text="Iniciar sesión como Admin", command=self.verificar_credenciales_admin)
  self.boton_iniciar_admin.grid(row=2, column=0, columnspan=2, pady=10)

  self.boton_volver = tk.Button(self, text="Volver", command=self.mostrar_tipo_usuario)
  self.boton_volver.grid(row=3, column=0, columnspan=2, pady=10)

 # Método para verificar las credenciales del usuario
 def verificar_credenciales_usuario(self):
  usuario = self.entry_usuario.get()
  contrasena = self.entry_contrasena.get()

  if usuario in self.usuarios and self.usuarios[usuario] == contrasena:
   messagebox.showinfo("Éxito", "Inicio de sesión como Usuario exitoso")
   self.destroy()
   PaginaUsuario()
  else:
   messagebox.showerror("Error", "Credenciales incorrectas")

 # Método para verificar las credenciales del administrador
 def verificar_credenciales_admin(self):
  admin_usuario = "admin"
  admin_contrasena = "admin123"  # Credenciales predeterminadas para el administrador

  usuario = self.entry_admin_usuario.get()
  contrasena = self.entry_admin_contrasena.get()

  if usuario == admin_usuario and contrasena == admin_contrasena:
   messagebox.showinfo("Éxito", "Inicio de sesión como Administrador exitoso")
   self.destroy()
   PaginaWebTkinter()
  else:
   messagebox.showerror("Error", "Credenciales incorrectas")

 # Método para mostrar la interfaz de creación de usuario
 def mostrar_crear_usuario(self):
  self.limpiar_ventana()

  # Crear los widgets para la creación de usuario
  self.label_nuevo_usuario = tk.Label(self, text="Nuevo Usuario:")
  self.label_nuevo_usuario.grid(row=0, column=0, padx=10, pady=10)

  self.entry_nuevo_usuario = tk.Entry(self)
  self.entry_nuevo_usuario.grid(row=0, column=1, padx=10, pady=10)

  self.label_nueva_contrasena = tk.Label(self, text="Nueva Contraseña:")
  self.label_nueva_contrasena.grid(row=1, column=0, padx=10, pady=10)

  self.entry_nueva_contrasena = tk.Entry(self, show="*")
  self.entry_nueva_contrasena.grid(row=1, column=1, padx=10, pady=10)

  self.boton_crear = tk.Button(self, text="Crear Usuario", command=self.crear_usuario)
  self.boton_crear.grid(row=2, column=0, columnspan=2, pady=20)

  # Botón para volver al inicio de sesión de usuario
  self.boton_volver = tk.Button(self, text="Volver a Iniciar sesión", command=self.mostrar_inicio_sesion_usuario)
  self.boton_volver.grid(row=3, column=0, columnspan=2, pady=10)

 # Método para crear un nuevo usuario
 def crear_usuario(self):
  nuevo_usuario = self.entry_nuevo_usuario.get()
  nueva_contrasena = self.entry_nueva_contrasena.get()

  if nuevo_usuario and nueva_contrasena:
   # Agregar el nuevo usuario al diccionario
   self.usuarios[nuevo_usuario] = nueva_contrasena
   self.guardar_usuarios()  # Guardar los usuarios actualizados en el archivo JSON

   messagebox.showinfo("Éxito", f"Usuario {nuevo_usuario} creado exitosamente.")
   self.mostrar_inicio_sesion_usuario()  # Volver a la pantalla de inicio de sesión de usuario
  else:
   messagebox.showerror("Error", "Por favor, ingrese un nombre de usuario y una contraseña.")

class PaginaWebTkinter:
 def __init__(self):
  # Ventana principal
  self.ventana = tk.Tk()
  self.ventana.title("TransporteXpress")
  # Obtener el tamaño de la pantalla
  pantalla_ancho = self.ventana.winfo_screenwidth()  # Ancho de la pantalla
  pantalla_alto = self.ventana.winfo_screenheight()  # Alto de la pantalla
  # Establecer el tamaño de la ventana al tamaño de la pantalla
  self.ventana.geometry(f"{pantalla_ancho}x{pantalla_alto}")
  # Evitar redimensionar la ventana
  self.ventana.resizable(False, False)
  self.ventana.configure(bg="#FFE5B4")
  self.camiones = self.cargar_camiones()  
  self.hilo_mantencion = threading.Thread(target=self.gestion_mantencion, daemon=True)
  self.hilo_mantencion.start()  
  # Crear el canvas y el frame que contendrá todos los widgets
  self.canvas = tk.Canvas(self.ventana, bg="white")
  self.scrollable_frame = tk.Frame(self.canvas, bg="white")  
  # Crear scrollbar vertical y asociarlo al canvas
  self.scrollbar = tk.Scrollbar(self.ventana, orient="vertical", command=self.canvas.yview)
  self.canvas.configure(yscrollcommand=self.scrollbar.set)  
  # Colocar scrollbar y canvas en la ventana
  self.scrollbar.pack(side="right", fill="y")
  self.canvas.pack(side="left", fill="both", expand=True)
  # Configurar el frame dentro del canvas
  self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
  self.scrollable_frame.bind("<Configure>", self.actualizar_scrollregion)
  # Construir la interfaz de la "página web"
  self.crear_encabezado()
  self.crear_menu_superior()
  self.crear_contenido_principal()
  # Iniciar el bucle principal de la aplicación
  self.ventana.mainloop()

 def actualizar_scrollregion(self, event):
  # Actualizar la región de desplazamiento del canvas
  self.canvas.configure(scrollregion=self.canvas.bbox("all"))

 def espaciado(self, contenedor, fila, columna):
  # Crear el texto formateado
  texto = ("                                       ")

  # Crear la etiqueta con el texto formateado
  etiqueta = tk.Label(
  contenedor,
  text=texto,
  font=("Arial", 20),
  bg="white",
  wraplength=250,
  justify="left"
  )
  etiqueta.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

 def crear_encabezado(self):
  # Encabezado
  encabezado = tk.Frame(self.scrollable_frame, bg="#FF8C42", height=80)
  encabezado.pack(fill="x")


  encabezado.grid_columnconfigure(0, weight=1)
  titulo = tk.Label(encabezado, text="TransporteXpress", fg="white", bg="#FF8C42", font=("Arial", 24))
  titulo.grid(row=0, column=0, padx=20, pady=20, sticky="w")

 def crear_menu_superior(self):
  # Menú Superior
  menu_superior = tk.Frame(self.scrollable_frame, bg="#FFA559", height=40)  # Menú superior en naranja suave
  menu_superior.pack(fill="x")

  # Botones del menú superior
  botones = {
  "Disponibles": self.mostrar_disponibles,
  "Mantención": self.mostrar_mantención,
  "Fichas técnicas": self.mostrar_Fichas_Tecnicas,
  "Admin": self.prueba,
  "buscador": self.buscador,
  }

  for texto, comando in botones.items():
   btn = tk.Button(menu_superior, text=texto, bg="#FFA559", font=("Arial", 14), fg="white", relief="flat", command=comando)
   btn.pack(side="left", padx=20, pady=10)

 def crear_contenido_principal(self):
  # Contenido Principal
  self.contenido = tk.Frame(self.scrollable_frame, bg="white")
  self.contenido.pack(expand=True, fill="both", side="top")

  # Mostrar contenido inicial
  self.mostrar_disponibles()

 def limpiar_contenido(self):
  # Eliminar el contenido actual del área principal
  for widget in self.contenido.winfo_children():
   widget.destroy()

 def mostrar_disponibles(self):
  self.limpiar_contenido()

  etiqueta = tk.Label(self.contenido, text="Camiones disponibles", font=("Arial", 15), bg="white", fg="#FF8C42")
  etiqueta.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")

  # Configurar el peso de las filas y columnas para que se expandan
  total_columns = 6  # Número de columnas que deseas abarcar

  for i in range(total_columns):
   self.contenido.grid_columnconfigure(i, weight=1)

  #self.detalles_camion(self.camiones[0])

  self.mostrar_camiones_disponibles(self.contenido,1)

  etiqueta = tk.Label(self.contenido, text="                                                                             ", 
  font=("Arial", 12), bg="white", wraplength=250)
  etiqueta.grid(row=1, column=2, columnspan=total_columns, padx=0, pady=5, sticky="nsew")

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def mostrar_mantención(self):
  self.limpiar_contenido()

  etiqueta = tk.Label(self.contenido, text="Camiones en mantención", font=("Arial", 15), bg="white", fg="#FF8C42")
  etiqueta.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")
  
  self.mostrar_camiones_en_mantencion(self.contenido)

  self.espaciado(self.contenido,9,1)

  self.espaciado(self.contenido,1,5)

  etiqueta = tk.Label(self.contenido, text="                       ", font=("Arial", 12), bg="white", wraplength=250)
  etiqueta.grid(row=1, column=2, padx=0, pady=5, sticky="nsew")

  # Segunda columna
  etiqueta = tk.Label(self.contenido, text="Mantenciones programadas", font=("Arial", 15), bg="white", fg="#FF8C42", wraplength=300, justify="left")
  etiqueta.grid(row=0, column=3, padx=0, pady=5, sticky="nsew")

  self.mostrar_camiones_fmantencion(self.contenido,4)

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def mostrar_Fichas_Tecnicas(self):
  self.limpiar_contenido()
  

  camiones_disponibles = [camion for camion in self.camiones]

  marca = -3
  t = -2

  if camiones_disponibles:
         
         for camion in camiones_disponibles:
          marca += 3
          t += 3
          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text= f"{camion.marca} {camion.modelo}",
           font=("Arial", 20),
           bg="white",
           fg="#FF8C42",
           wraplength=250,
           justify="left"
          )
          etiqueta.grid(row=marca,column=0, pady=5, sticky="w")

          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text= f"Patente: {camion.patente}\n"
                 f"Marca: {camion.marca}\n"
                 f"Modelo: {camion.modelo}\n"
                 f"Año: {camion.ano}\n"
                 f"Capacidad: {camion.capacidad}\n"
                 f"Kilometraje: {camion.km_camion}\n"
                 f"Precio: {camion.precio}\n"
                 f"Tipo: {camion.tipo}\n"
                 f"Peso Máximo: {camion.peso_max}\n"
                 f"Estado: {camion.estado}\n"
                 f"Última Mantención: {camion.ultima_mantencion.strftime('%Y-%m-%d')}\n"
                 f"\n"
                 "--------------------------------------",
           font=("Arial", 12),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row=t,column=0, pady=5, sticky="w")

          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text= f"--- Motor ---\n"
                 f"ID: {camion.motor.id}\n"
                 f"Tipo: {camion.motor.tipo}\n"
                 f"Cilindrada: {camion.motor.cilindrada}\n"
                 f"Potencia: {camion.motor.potencia}\n"
                 f"Km/Lt: {camion.motor.km_lt}\n"
                 f"Velocidad Máxima: {camion.motor.vel_max}\n"
                 f"Rendimiento: {camion.motor.rendimiento}\n"
                 f"Última Revisión: {camion.motor.ult_rev}\n"
                 "--------------------------------------",
           font=("Arial", 12),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row=t, column=1, pady=5, sticky="w")
  
  self.espaciado(self.contenido,(t+1),1)

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def cargar_camiones(self):
   try:
    with open("camiones.json", "r") as file:
     data = json.load(file)
     return [Camion.from_dict(camion) for camion in data]
   except FileNotFoundError:
    motor1 = Motor(1, "mecánico", "6", "mucha", 10.9, "200Km", "mucho", "2024-05-10")
    return [
     Camion(motor1, "AA1122", "Volvo", "Gama FH", 2011, "20m^3", "123.403Km", "$25.000", "camion", "10T"),
     Camion(motor1, "CCDD22", "Renault", "trucks gamma D", 2010, "20m^3", "200.430Km", "$25.000", "camion", "10T")
    ]

 def mostrar_camiones(self, listbox):
  # Limpia el contenido previo del Listbox
  listbox.delete(0, tk.END)
  
  # Agrega información sobre los camiones al Listbox
  for camion in self.camiones:
   listbox.insert(tk.END, f"{camion.marca} {camion.modelo} - Estado: {camion.estado}")

 def prueba(self):
  self.limpiar_contenido()
  # Lista de camiones
  self.label_lista = tk.Label(self.contenido, text="Lista de Camiones:")
  self.label_lista.grid()

  self.lista_camiones = tk.Listbox(self.contenido, height=6, width=50)
  self.lista_camiones.grid()
  self.actualizar_lista_camiones()

  # Buscador de camiones
  self.label_buscador = tk.Label(self.contenido, text="Buscar Camiones:")
  self.label_buscador.grid(pady=5)

  self.entrada_buscador = tk.Entry(self.contenido, width=50)
  self.entrada_buscador.grid()

  self.boton_buscar = tk.Button(self.contenido, text="Buscar", command=self.buscar_camion)
  self.boton_buscar.grid(pady=5)

  # Botón para arrendar un camión
  self.boton_arrendar = tk.Button(self.contenido, text="Arrendar Camión", command=self.arrendar_camion)
  self.boton_arrendar.grid(pady=5)

  # Botón para devolver un camión
  self.boton_devolver = tk.Button(self.contenido, text="Devolver Camión", command=self.devolver_camion)
  self.boton_devolver.grid(pady=5)

  self.boton_devolver = tk.Button(self.contenido, text="agragar Camión", command=self.agregar_camion)
  self.boton_devolver.grid(pady=5)

  # Botón para realizar mantención no programada
  self.boton_mantencion = tk.Button(self.contenido, text="Mantención No Programada", command=self.mantencion_no_programada)
  self.boton_mantencion.grid(pady=5)

  # Botón para realizar mantención no programada
  self.boton_mantencion = tk.Button(self.contenido, text="finalizar mantención", command=self.fin_mantencion_camion)
  self.boton_mantencion.grid(pady=5)

  # Etiqueta de información
  self.label_estado = tk.Label(self.contenido, text="", fg="green")
  self.label_estado.grid(pady=10)

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def buscador(self):
  # Limpia el contenido actual
  self.limpiar_contenido()

  # Etiqueta para el buscador
  self.label_buscador = tk.Label(
   self.contenido,
   text="Buscar Camiones:",
   font=("Arial", 14, "bold"),
   bg="#F8F9FA",
   fg="#4B4B4B"
  )
  self.label_buscador.grid(row=0, column=0, pady=(10, 5), sticky="w")

  # Entrada para buscar camiones
  self.entrada_buscador = tk.Entry(
   self.contenido,
   width=112,
   font=("Arial", 14),
   relief="groove",
   bd=3,
   bg="#FFFFFF",
   fg="#333333"
  )
  self.entrada_buscador.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

  # Botón para realizar la búsqueda
  self.boton_buscar = tk.Button(
   self.contenido,
   text="🔍 Buscar",
   command=self.buscar_camion,
   font=("Arial", 12, "bold"),
   bg="#48C9B0",
   fg="white",
   relief="flat",
   padx=10,
   pady=5
  )
  self.boton_buscar.grid(row=1, column=1, padx=(95, 20), pady=(0, 10), sticky="w")

  # Etiqueta para la lista de camiones
  self.label_lista = tk.Label(
   self.contenido,
   text="Lista de Camiones:",
   font=("Arial", 16, "bold"),
   bg="#F8F9FA",
   fg="#4B4B4B"
  )
  self.label_lista.grid(row=2, column=0, pady=(10, 5), sticky="w")

  # Scrollbar personalizada
  scrollbar = tk.Scrollbar(self.contenido, orient="vertical", bg="#D6EAF8", troughcolor="#F8F9FA")

  # Listbox para mostrar los camiones
  self.lista_camiones = tk.Listbox(
   self.contenido,
   height=12,
   width=40,
   font=("Arial", 12),
   fg="#2C3E50",
   bg="#EAF2F8",
   selectbackground="#48C9B0",
   selectforeground="white",
   relief="ridge",
   bd=3,
   yscrollcommand=scrollbar.set
  )
  self.lista_camiones.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

  # Configuración del scrollbar
  scrollbar.config(command=self.lista_camiones.yview)
  scrollbar.grid(row=3, column=1, sticky="ns")

  # Conecta el evento de selección con un método
  self.lista_camiones.bind("<<ListboxSelect>>", self.redirigir_detalles_camion)

  # Actualiza la lista con los camiones
  self.actualizar_lista_camiones()

  # Configuración para que la lista se adapte
  self.contenido.grid_rowconfigure(3, weight=1)
  self.contenido.grid_columnconfigure(0, weight=1)

 def mostrar_camiones_disponibles(self, contenedor,column):

        # Filtrar camiones disponibles       
        camiones_disponibles = [camion for camion in self.camiones if camion.estado=="Disponible"]

        if camiones_disponibles:
         
         row = 1
         for camion in camiones_disponibles:
          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text=f"{camion.marca} {camion.modelo}\n"
                f"Patente: {camion.patente}\n"
                f"Año: {camion.ano}\n"
                f":Kilometraje {camion.km_camion}\n"
                f"Precio de arriendo: {camion.precio}",
           font=("Arial", 10),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row= row, column=column, pady=5, sticky="w")

          row+=1

          boton = tk.Button(
          contenedor,
          text="Mostrar ficha técnica",
          font=("Arial", 10),
          bg="#FFF5E1",
          highlightbackground="#FF8C42",
          highlightthickness=2,
          command=self.mostrar_Fichas_Tecnicas
          )
          boton.grid(row= row, column=column, pady=10)

          self.boton_arrendar = tk.Button(self.contenido, text="Arrendar Camión", command=self.arrendar_)
          self.boton_arrendar.grid(row=row, column=(column-1))

          row+=2

          # Crear botón asociado al camión

 def mostrar_camiones_fmantencion(self, contenedor,column):

        # Filtrar camiones disponibles       
        camiones_disponibles = [camion for camion in self.camiones if camion.estado=="Disponible"]

        if camiones_disponibles:
         
         row = 1
         for camion in camiones_disponibles:
          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text=f"{camion.marca} {camion.modelo}\n"
                f"Patente: {camion.patente}\n"
                f"Año: {camion.ano}\n"
                f":Kilometraje {camion.km_camion}\n"
                f"Precio de arriendo: {camion.precio}",
           font=("Arial", 10),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row= row, column=column, pady=5, sticky="w")

          row+=1

          boton = tk.Button(
          contenedor,
          text="Mostrar ficha técnica",
          font=("Arial", 10),
          bg="#FFF5E1",
          highlightbackground="#FF8C42",
          highlightthickness=2,
          command=self.mostrar_Ficha_Tecnica1
          )
          boton.grid(row= row, column=column, pady=10)

          row+=2

          # Crear botón asociado al camión

 def mostrar_camiones_en_mantencion(self, contenedor):

        # Filtrar camiones en mantención       
        camiones_en_mantencion = [camion for camion in self.camiones if camion.estado=="en mantención"]
        
        if camiones_en_mantencion:
         
         row = 1
         for camion in camiones_en_mantencion:
          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text=f"{camion.marca} {camion.modelo}\n"
                f"Patente: {camion.patente}\n"
                f"Año: {camion.ano}\n"
                f":Kilometraje {camion.km_camion}\n"
                f"Precio de arriendo: {camion.precio}",
           font=("Arial", 10),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row= row, column=1, pady=5, sticky="w")

          row+=1

          boton = tk.Button(
          contenedor,
          text="Mostrar ficha técnica",
          font=("Arial", 10),
          bg="#FFF5E1",
          highlightbackground="#FF8C42",
          highlightthickness=2,
          command=self.mostrar_Fichas_Tecnicas
          )
          boton.grid(row= row, column=1, pady=10)

          row+=2

          # Crear botón asociado al camión

 def redirigir_detalles_camion(self, event):
  """Método que se llama al seleccionar un camión en la lista."""
  seleccion = self.lista_camiones.curselection()
  if seleccion:
   index = seleccion[0]
   camion = self.camiones[index]
   self.detalles_camion(camion)

 def detalles_camion(self, camion):
  """Muestra los detalles del camión seleccionado."""
  self.limpiar_contenido()
    
  detalles = f"""
  Marca: {camion.marca}
  Modelo: {camion.modelo}
  Año: {camion.ano}
  Capacidad: {camion.capacidad}
  Motor: {camion.motor.tipo}
  Estado: {camion.estado}
  """
  etiqueta_detalles = tk.Label(
   self.contenido,
   text=detalles,
   font=("Arial", 14),
   bg="#EAF2F8",
   justify="left"
  )
  etiqueta_detalles.grid(pady=20, padx=20)

  # Botón para regresar a la lista
  boton_regresar = tk.Button(
   self.contenido,
   text="⬅ Volver",
   font=("Arial", 12, "bold"),
   bg="#48C9B0",
   fg="white",
   command=self.buscador
  )
  boton_regresar.grid(pady=10)

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def mostrar_Ficha_Tecnica1(self):
  self.limpiar_contenido()
  self.mostrar_Ficha_Tecnica(
  self.contenido, modelo="Volvo Gama FH", tipo="Cabeza Tractora",
  ejes="6x4", norma="Euro 6", longitud="6,190 m", ancho="2,495 m",
  alto="3,324 m", Dejes="4,000 m", peso="20,500 Kg", pesot="44,000 Kg",
  motor="D13C540", cilindrada="12.8 Litros", Ncilindros="6 en línea",
  potencia="540 CV (397 kW) a 1,400 rpm", par="2,600 Nm a 1,000 - 1,400 rpm",
  refri="Volumen Total de 38 Litros", caja="I-Shift", marchas="12 Marchas con Opcion de Cambio Manual",
  carga="Hasta 26 Toneladas", consumo="Optimizado Para Reducir el Impacto Ambiental",
  freno="Sistema de Frenado Eficiente que Mejora la Seguridad y el Control del Vehículo",
  cabina="Globetroter XL, Diseñada Para Ofrecer Comodidad y Ergonomía el Conductor",
  sistema="Alta Capacidad Para Mantener un Ambiente Confortable",
  tec="Equipado con Computadora a Bordo Para Monitoreo y Gestión del Remdimiento",
  fila1=0, columna1=0,
  fila2=1, columna2=0,
  fila3=1, columna3=1
  )

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def actualizar(self):
  self.actualizar_lista_camiones(self)

 def actualizar_lista_camiones(self, filtro=None):
  """
  Actualiza la lista de camiones en la interfaz, aplicando un filtro opcional.
  :param filtro: Texto de búsqueda para filtrar los camiones.
  """
  self.lista_camiones.delete(0, tk.END)
  for camion in self.camiones:
   # Aplicar el filtro si existe
   if filtro:
    atributos = f"{camion.marca} {camion.modelo} {camion.ano} {camion.capacidad} {camion.km_camion} {camion.precio} {camion.tipo} {camion.peso_max}".lower()
    if filtro.lower() not in atributos:
     continue

   estado = camion.estado
   ultima_mantencion = camion.ultima_mantencion.strftime("%Y-%m-%d %H:%M:%S")
   self.lista_camiones.insert(
    tk.END,
    f'{camion.marca} {camion.modelo} - {estado} (Última Mantención: {ultima_mantencion})'
   )

 def buscar_camion(self):
  """Realiza una búsqueda de camiones según el texto ingresado."""
  filtro = self.entrada_buscador.get().strip()
  if filtro:
   self.actualizar_lista_camiones(filtro=filtro)
  else:
   self.actualizar_lista_camiones()

 def arrendar_camion(self):
  """Permite arrendar un camión disponible."""
  seleccion = self.lista_camiones.curselection()
  if not seleccion:
   messagebox.showwarning("Advertencia", "Seleccione un camión para arrendar.")
   return

  index = seleccion[0]
  camion = self.camiones[index]

  if camion.estado == "Disponible":
   camion.estado = "Arrendado"
   self.actualizar_lista_camiones()
   messagebox.showinfo("Éxito", f'El {camion.marca} {camion.modelo} ha sido arrendado.')
  else:
   messagebox.showerror("Error", f'El {camion.marca} {camion.modelo} no está disponible para arriendo.')
  self.guardar_camiones()

 def fin_mantencion_camion(self):
  """Permite arrendar un camión disponible."""
  seleccion = self.lista_camiones.curselection()
  if not seleccion:
   messagebox.showwarning("Advertencia", "Seleccione un camión para arrendar.")
   return

  index = seleccion[0]
  camion = self.camiones[index]

  if camion.estado == "en mantención":
   camion.estado = "Disponible"
   self.actualizar_lista_camiones()
   messagebox.showinfo("Mantención Completada", f' del {camion.marca} {camion.modelo} ha sido reparado.')
  else:
   messagebox.showerror("Error", f'El {camion.marca} {camion.modelo} no está disponible para mantención.')
  self.guardar_camiones()

 def arrendar_(self):
  """Arrendar específicamente el Camión 1."""
  camion = self.camiones[0]  # Camión 1 está en el índice 0
  if camion.arrendar():
   messagebox.showinfo("Éxito", f"{camion.marca} ha sido arrendado.")
  else:
   messagebox.showerror("Error", f"{camion.marca} ya está arrendado.")

  self.actualizar_lista_camiones()        

 def devolver_camion(self):
  """Permite devolver un camión arrendado."""
  seleccion = self.lista_camiones.curselection()
  if not seleccion:
   messagebox.showwarning("Advertencia", "Seleccione un camión para devolver.")
   return

  index = seleccion[0]
  camion = self.camiones[index]

  if camion.estado == "Arrendado":
   camion.estado = "Disponible"
   self.actualizar_lista_camiones()
   messagebox.showinfo("Éxito", f'El {camion.marca} {camion.modelo} ha sido devuelto.')
  else:
   messagebox.showerror("Error", f'El {camion.marca} {camion.modelo} no está arrendado.')
  self.guardar_camiones()

 def mantencion_no_programada(self):
  """Permite realizar una mantención no programada, seleccionando una parte específica."""
  seleccion = self.lista_camiones.curselection()
  if not seleccion:
   messagebox.showwarning("Advertencia", "Seleccione un camión para realizar mantención.")
   return

  index = seleccion[0]
  camion = self.camiones[index]

  if camion.estado == "Disponible":
            
   parte = simpledialog.askstring(
    "Parte a Reparar",
    f"Seleccione la parte del {camion.marca} {camion.modelo} a reparar (capacidad, kilometraje, motor):"
   )
   if parte not in ["capacidad","kilometraje","motor"]:
    messagebox.showerror("Error", "Parte seleccionada inválida.")
    return

   detalles = simpledialog.askstring(
    "Detalles de Reparación",
    f"Ingrese los detalles de la reparación para la parte {parte}:"
   )

   
   camion.realizar_mantencion(parte, detalles)
   camion.estado = "en mantención"
   self.actualizar_lista_camiones()
   messagebox.showinfo("Éxito", f'El {camion.marca} {camion.modelo} está en mantencion.')
   self.guardar_camiones()
   
 def gestion_mantencion(self):
  """Programa mantenciones cada 30 días (simulado como 30 segundos)."""
  while True:
   time.sleep(1)  # Revisar cada segundo
   for camion in self.camiones:
    if camion.estado == "Disponible" and camion.necesita_mantencion(dias=30):
     camion.estado = "En Mantención"
     self.actualizar_lista_camiones()
     self.label_estado.config(text=f'{camion.marca} está en mantención...')
     camion.realizar_mantencion()
     camion.estado = "Disponible"
     self.actualizar_lista_camiones()

 def guardar_camiones(self):
   with open("camiones.json", "w") as file:
    json.dump([camion.to_dict() for camion in self.camiones], file, indent=4)
   messagebox.showinfo("Guardado", "Datos guardados correctamente.")

 def agregar_camion(self):
  """
  Solicita datos al usuario para agregar un nuevo camión.
  """
  try:
   motor_id = simpledialog.askinteger("Motor", "ID del motor:")
   motor_tipo = simpledialog.askstring("Motor", "Tipo de motor:")
   motor_cilindrada = simpledialog.askstring("Motor", "Cilindrada:")
   motor_potencia = simpledialog.askstring("Motor", "Potencia:")
   motor_km_lt = simpledialog.askfloat("Motor", "Km por litro:")
   motor_vel_max = simpledialog.askstring("Motor", "Velocidad máxima:")
   motor_rendimiento = simpledialog.askstring("Motor", "Rendimiento:")
   motor_ult_rev = simpledialog.askstring("Motor", "Última revisión:")

   motor = Motor(motor_id, motor_tipo, motor_cilindrada, motor_potencia, motor_km_lt, motor_vel_max, motor_rendimiento, motor_ult_rev)

   patente = simpledialog.askstring("Camión", "Patente:")
   marca = simpledialog.askstring("Camión", "Marca:")
   modelo = simpledialog.askstring("Camión", "Modelo:")
   ano = simpledialog.askinteger("Camión", "Año:")
   capacidad = simpledialog.askstring("Camión", "Capacidad:")
   km_camion = simpledialog.askstring("Camión", "Kilometraje:")
   precio = simpledialog.askstring("Camión", "Precio:")
   tipo = simpledialog.askstring("Camión", "Tipo:")
   peso_max = simpledialog.askstring("Camión", "Peso máximo:")

   nuevo_camion = Camion(motor, patente, marca, modelo, ano, capacidad, km_camion, precio, tipo, peso_max)
   self.camiones.append(nuevo_camion)
   self.guardar_camiones()
   messagebox.showinfo("Éxito", "Camión agregado correctamente.")
  except Exception as e:
   messagebox.showerror("Error", f"No se pudo agregar el camión: {e}")

class PaginaUsuario:
 def __init__(self):
  # Ventana principal
  self.ventana = tk.Tk()
  self.ventana.title("TransporteXpress")
  # Obtener el tamaño de la pantalla
  pantalla_ancho = self.ventana.winfo_screenwidth()  # Ancho de la pantalla
  pantalla_alto = self.ventana.winfo_screenheight()  # Alto de la pantalla
  # Establecer el tamaño de la ventana al tamaño de la pantalla
  self.ventana.geometry(f"{pantalla_ancho}x{pantalla_alto}")
  # Evitar redimensionar la ventana
  self.ventana.resizable(False, False)
  self.ventana.configure(bg="#FFE5B4")
  self.camiones = self.cargar_camiones()  
  self.hilo_mantencion = threading.Thread(target=self.gestion_mantencion, daemon=True)
  self.hilo_mantencion.start()  
  # Crear el canvas y el frame que contendrá todos los widgets
  self.canvas = tk.Canvas(self.ventana, bg="white")
  self.scrollable_frame = tk.Frame(self.canvas, bg="white")  
  # Crear scrollbar vertical y asociarlo al canvas
  self.scrollbar = tk.Scrollbar(self.ventana, orient="vertical", command=self.canvas.yview)
  self.canvas.configure(yscrollcommand=self.scrollbar.set)  
  # Colocar scrollbar y canvas en la ventana
  self.scrollbar.pack(side="right", fill="y")
  self.canvas.pack(side="left", fill="both", expand=True)
  # Configurar el frame dentro del canvas
  self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
  self.scrollable_frame.bind("<Configure>", self.actualizar_scrollregion)
  # Construir la interfaz de la "página web"
  self.crear_encabezado()
  self.crear_menu_superior()
  self.crear_contenido_principal()
  # Iniciar el bucle principal de la aplicación
  self.ventana.mainloop()

 def actualizar_scrollregion(self, event):
  # Actualizar la región de desplazamiento del canvas
  self.canvas.configure(scrollregion=self.canvas.bbox("all"))

 def espaciado(self, contenedor, fila, columna):
  # Crear el texto formateado
  texto = ("                                       ")

  # Crear la etiqueta con el texto formateado
  etiqueta = tk.Label(
  contenedor,
  text=texto,
  font=("Arial", 20),
  bg="white",
  wraplength=250,
  justify="left"
  )
  etiqueta.grid(row=fila, column=columna, padx=10, pady=10, sticky="nsew")

 def crear_encabezado(self):
  # Encabezado
  encabezado = tk.Frame(self.scrollable_frame, bg="#FF8C42", height=80)
  encabezado.pack(fill="x")


  encabezado.grid_columnconfigure(0, weight=1)
  titulo = tk.Label(encabezado, text="TransporteXpress", fg="white", bg="#FF8C42", font=("Arial", 24))
  titulo.grid(row=0, column=0, padx=20, pady=20, sticky="w")

 def crear_menu_superior(self):
  # Menú Superior
  menu_superior = tk.Frame(self.scrollable_frame, bg="#FFA559", height=40)  # Menú superior en naranja suave
  menu_superior.pack(fill="x")

  # Botones del menú superior
  botones = {
  "Disponibles": self.mostrar_disponibles,
  "Mantención": self.mostrar_mantención,
  "Fichas técnicas": self.mostrar_Fichas_Tecnicas,
  "buscador": self.buscador,
  }

  for texto, comando in botones.items():
   btn = tk.Button(menu_superior, text=texto, bg="#FFA559", font=("Arial", 14), fg="white", relief="flat", command=comando)
   btn.pack(side="left", padx=20, pady=10)

 def crear_contenido_principal(self):
  # Contenido Principal
  self.contenido = tk.Frame(self.scrollable_frame, bg="white")
  self.contenido.pack(expand=True, fill="both", side="top")

  # Mostrar contenido inicial
  self.mostrar_disponibles()

 def limpiar_contenido(self):
  # Eliminar el contenido actual del área principal
  for widget in self.contenido.winfo_children():
   widget.destroy()

 def mostrar_disponibles(self):
  self.limpiar_contenido()

  etiqueta = tk.Label(self.contenido, text="Camiones disponibles", font=("Arial", 15), bg="white", fg="#FF8C42")
  etiqueta.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")

  # Configurar el peso de las filas y columnas para que se expandan
  total_columns = 6  # Número de columnas que deseas abarcar

  for i in range(total_columns):
   self.contenido.grid_columnconfigure(i, weight=1)

  self.mostrar_camiones_disponibles(self.contenido,1)

  etiqueta = tk.Label(self.contenido, text="                                                                             ", 
  font=("Arial", 12), bg="white", wraplength=250)
  etiqueta.grid(row=1, column=2, columnspan=total_columns, padx=0, pady=5, sticky="nsew")

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def mostrar_mantención(self):
  self.limpiar_contenido()

  etiqueta = tk.Label(self.contenido, text="Camiones en mantención", font=("Arial", 15), bg="white", fg="#FF8C42")
  etiqueta.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")
  
  self.mostrar_camiones_en_mantencion(self.contenido)

  self.espaciado(self.contenido,9,1)

  self.espaciado(self.contenido,1,5)

  etiqueta = tk.Label(self.contenido, text="                       ", font=("Arial", 12), bg="white", wraplength=250)
  etiqueta.grid(row=1, column=2, padx=0, pady=5, sticky="nsew")

  # Segunda columna
  etiqueta = tk.Label(self.contenido, text="Mantenciones programadas", font=("Arial", 15), bg="white", fg="#FF8C42", wraplength=300, justify="left")
  etiqueta.grid(row=0, column=3, padx=0, pady=5, sticky="nsew")

  self.mostrar_camiones_fmantencion(self.contenido,4)

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def mostrar_Fichas_Tecnicas(self):
  self.limpiar_contenido()
  

  camiones_disponibles = [camion for camion in self.camiones]

  marca = -3
  t = -2

  if camiones_disponibles:
         
         for camion in camiones_disponibles:
          marca += 3
          t += 3
          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text= f"{camion.marca} {camion.modelo}",
           font=("Arial", 20),
           bg="white",
           fg="#FF8C42",
           wraplength=250,
           justify="left"
          )
          etiqueta.grid(row=marca,column=0, pady=5, sticky="w")

          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text= f"Patente: {camion.patente}\n"
                 f"Marca: {camion.marca}\n"
                 f"Modelo: {camion.modelo}\n"
                 f"Año: {camion.ano}\n"
                 f"Capacidad: {camion.capacidad}\n"
                 f"Kilometraje: {camion.km_camion}\n"
                 f"Precio: {camion.precio}\n"
                 f"Tipo: {camion.tipo}\n"
                 f"Peso Máximo: {camion.peso_max}\n"
                 f"Estado: {camion.estado}\n"
                 f"Última Mantención: {camion.ultima_mantencion.strftime('%Y-%m-%d')}\n"
                 f"\n"
                 "--------------------------------------",
           font=("Arial", 12),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row=t,column=0, pady=5, sticky="w")

          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text= f"--- Motor ---\n"
                 f"ID: {camion.motor.id}\n"
                 f"Tipo: {camion.motor.tipo}\n"
                 f"Cilindrada: {camion.motor.cilindrada}\n"
                 f"Potencia: {camion.motor.potencia}\n"
                 f"Km/Lt: {camion.motor.km_lt}\n"
                 f"Velocidad Máxima: {camion.motor.vel_max}\n"
                 f"Rendimiento: {camion.motor.rendimiento}\n"
                 f"Última Revisión: {camion.motor.ult_rev}\n"
                 "--------------------------------------",
           font=("Arial", 12),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row=t, column=1, pady=5, sticky="w")
  
  self.espaciado(self.contenido,(t+1),1)

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def cargar_camiones(self):
   try:
    with open("camiones.json", "r") as file:
     data = json.load(file)
     return [Camion.from_dict(camion) for camion in data]
   except FileNotFoundError:
    motor1 = Motor(1, "mecánico", "6", "mucha", 10.9, "200Km", "mucho", "2024-05-10")
    return [
     Camion(motor1, "AA1122", "Volvo", "Gama FH", 2011, "20m^3", "123.403Km", "$25.000", "camion", "10T"),
     Camion(motor1, "CCDD22", "Renault", "trucks gamma D", 2010, "20m^3", "200.430Km", "$25.000", "camion", "10T")
    ]

 def mostrar_camiones(self, listbox):
  # Limpia el contenido previo del Listbox
  listbox.delete(0, tk.END)
  
  # Agrega información sobre los camiones al Listbox
  for camion in self.camiones:
   listbox.insert(tk.END, f"{camion.marca} {camion.modelo} - Estado: {camion.estado}")

 def buscador(self):
  # Limpia el contenido actual
  self.limpiar_contenido()

  # Etiqueta para el buscador
  self.label_buscador = tk.Label(
   self.contenido,
   text="Buscar Camiones:",
   font=("Arial", 14, "bold"),
   bg="#F8F9FA",
   fg="#4B4B4B"
  )
  self.label_buscador.grid(row=0, column=0, pady=(10, 5), sticky="w")

  # Entrada para buscar camiones
  self.entrada_buscador = tk.Entry(
   self.contenido,
   width=112,
   font=("Arial", 14),
   relief="groove",
   bd=3,
   bg="#FFFFFF",
   fg="#333333"
  )
  self.entrada_buscador.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

  # Botón para realizar la búsqueda
  self.boton_buscar = tk.Button(
   self.contenido,
   text="🔍 Buscar",
   command=self.buscar_camion,
   font=("Arial", 12, "bold"),
   bg="#48C9B0",
   fg="white",
   relief="flat",
   padx=10,
   pady=5
  )
  self.boton_buscar.grid(row=1, column=1, padx=(95, 20), pady=(0, 10), sticky="w")

  # Etiqueta para la lista de camiones
  self.label_lista = tk.Label(
   self.contenido,
   text="Lista de Camiones:",
   font=("Arial", 16, "bold"),
   bg="#F8F9FA",
   fg="#4B4B4B"
  )
  self.label_lista.grid(row=2, column=0, pady=(10, 5), sticky="w")

  # Scrollbar personalizada
  scrollbar = tk.Scrollbar(self.contenido, orient="vertical", bg="#D6EAF8", troughcolor="#F8F9FA")

  # Listbox para mostrar los camiones
  self.lista_camiones = tk.Listbox(
   self.contenido,
   height=12,
   width=40,
   font=("Arial", 12),
   fg="#2C3E50",
   bg="#EAF2F8",
   selectbackground="#48C9B0",
   selectforeground="white",
   relief="ridge",
   bd=3,
   yscrollcommand=scrollbar.set
  )
  self.lista_camiones.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

  # Configuración del scrollbar
  scrollbar.config(command=self.lista_camiones.yview)
  scrollbar.grid(row=3, column=1, sticky="ns")

  # Conecta el evento de selección con un método
  self.lista_camiones.bind("<<ListboxSelect>>", self.redirigir_detalles_camion)

  # Actualiza la lista con los camiones
  self.actualizar_lista_camiones()

  # Configuración para que la lista se adapte
  self.contenido.grid_rowconfigure(3, weight=1)
  self.contenido.grid_columnconfigure(0, weight=1)

 def mostrar_camiones_disponibles(self, contenedor,column):

        # Filtrar camiones disponibles       
        camiones_disponibles = [camion for camion in self.camiones if camion.estado=="Disponible"]

        if camiones_disponibles:
         
         row = 1
         for camion in camiones_disponibles:
          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text=f"{camion.marca} {camion.modelo}\n"
                f"Patente: {camion.patente}\n"
                f"Año: {camion.ano}\n"
                f":Kilometraje {camion.km_camion}\n"
                f"Precio de arriendo: {camion.precio}",
           font=("Arial", 10),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row= row, column=column, pady=5, sticky="w")

          row+=1

          boton = tk.Button(
          contenedor,
          text="Mostrar ficha técnica",
          font=("Arial", 10),
          bg="#FFF5E1",
          highlightbackground="#FF8C42",
          highlightthickness=2,
          command=self.mostrar_Fichas_Tecnicas
          )
          boton.grid(row= row, column=column, pady=10)

          self.boton_arrendar = tk.Button(self.contenido, text="Arrendar Camión", command=self.arrendar_)
          self.boton_arrendar.grid(row=row, column=(column-1))

          row+=2

          # Crear botón asociado al camión

 def mostrar_camiones_fmantencion(self, contenedor,column):

        # Filtrar camiones disponibles       
        camiones_disponibles = [camion for camion in self.camiones if camion.estado=="Disponible"]

        if camiones_disponibles:
         
         row = 1
         for camion in camiones_disponibles:
          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text=f"{camion.marca} {camion.modelo}\n"
                f"Patente: {camion.patente}\n"
                f"Año: {camion.ano}\n"
                f":Kilometraje {camion.km_camion}\n"
                f"Precio de arriendo: {camion.precio}",
           font=("Arial", 10),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row= row, column=column, pady=5, sticky="w")

          row+=1

          boton = tk.Button(
          contenedor,
          text="Mostrar ficha técnica",
          font=("Arial", 10),
          bg="#FFF5E1",
          highlightbackground="#FF8C42",
          highlightthickness=2,
          command=self.mostrar_Ficha_Tecnica1
          )
          boton.grid(row= row, column=column, pady=10)

          row+=2

          # Crear botón asociado al camión

 def mostrar_camiones_en_mantencion(self, contenedor):

        # Filtrar camiones en mantención       
        camiones_en_mantencion = [camion for camion in self.camiones if camion.estado=="en mantención"]
        
        if camiones_en_mantencion:
         
         row = 1
         for camion in camiones_en_mantencion:
          
          # Crear etiqueta para el camión
          etiqueta = tk.Label(
           self.contenido,
           text=f"{camion.marca} {camion.modelo}\n"
                f"Patente: {camion.patente}\n"
                f"Año: {camion.ano}\n"
                f":Kilometraje {camion.km_camion}\n"
                f"Precio de arriendo: {camion.precio}",
           font=("Arial", 10),
           bg="white",
           justify="left"
          )
          etiqueta.grid(row= row, column=1, pady=5, sticky="w")

          row+=1

          boton = tk.Button(
          contenedor,
          text="Mostrar ficha técnica",
          font=("Arial", 10),
          bg="#FFF5E1",
          highlightbackground="#FF8C42",
          highlightthickness=2,
          command=self.mostrar_Fichas_Tecnicas
          )
          boton.grid(row= row, column=1, pady=10)

          row+=2

          # Crear botón asociado al camión

 def redirigir_detalles_camion(self, event):
  """Método que se llama al seleccionar un camión en la lista."""
  seleccion = self.lista_camiones.curselection()
  if seleccion:
   index = seleccion[0]
   camion = self.camiones[index]
   self.detalles_camion(camion)

 def detalles_camion(self, camion):
  """Muestra los detalles del camión seleccionado."""
  self.limpiar_contenido()
    
  detalles = f"""
  Marca: {camion.marca}
  Modelo: {camion.modelo}
  Año: {camion.ano}
  Capacidad: {camion.capacidad}
  Motor: {camion.motor.tipo}
  Estado: {camion.estado}
  """
  etiqueta_detalles = tk.Label(
   self.contenido,
   text=detalles,
   font=("Arial", 14),
   bg="#EAF2F8",
   justify="left"
  )
  etiqueta_detalles.grid(pady=20, padx=20)

  # Botón para regresar a la lista
  boton_regresar = tk.Button(
   self.contenido,
   text="⬅ Volver",
   font=("Arial", 12, "bold"),
   bg="#48C9B0",
   fg="white",
   command=self.buscador
  )
  boton_regresar.grid(pady=10)
  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def mostrar_Ficha_Tecnica1(self):
  self.limpiar_contenido()
  self.mostrar_Ficha_Tecnica(
  self.contenido, modelo="Volvo Gama FH", tipo="Cabeza Tractora",
  ejes="6x4", norma="Euro 6", longitud="6,190 m", ancho="2,495 m",
  alto="3,324 m", Dejes="4,000 m", peso="20,500 Kg", pesot="44,000 Kg",
  motor="D13C540", cilindrada="12.8 Litros", Ncilindros="6 en línea",
  potencia="540 CV (397 kW) a 1,400 rpm", par="2,600 Nm a 1,000 - 1,400 rpm",
  refri="Volumen Total de 38 Litros", caja="I-Shift", marchas="12 Marchas con Opcion de Cambio Manual",
  carga="Hasta 26 Toneladas", consumo="Optimizado Para Reducir el Impacto Ambiental",
  freno="Sistema de Frenado Eficiente que Mejora la Seguridad y el Control del Vehículo",
  cabina="Globetroter XL, Diseñada Para Ofrecer Comodidad y Ergonomía el Conductor",
  sistema="Alta Capacidad Para Mantener un Ambiente Confortable",
  tec="Equipado con Computadora a Bordo Para Monitoreo y Gestión del Remdimiento",
  fila1=0, columna1=0,
  fila2=1, columna2=0,
  fila3=1, columna3=1
  )

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def actualizar(self):
  self.actualizar_lista_camiones(self)

 def actualizar_lista_camiones(self, filtro=None):
  """
  Actualiza la lista de camiones en la interfaz, aplicando un filtro opcional.
  :param filtro: Texto de búsqueda para filtrar los camiones.
  """
  self.lista_camiones.delete(0, tk.END)
  for camion in self.camiones:
   # Aplicar el filtro si existe
   if filtro:
    atributos = f"{camion.marca} {camion.modelo} {camion.ano} {camion.capacidad} {camion.km_camion} {camion.precio} {camion.tipo} {camion.peso_max}".lower()
    if filtro.lower() not in atributos:
     continue

   estado = camion.estado
   ultima_mantencion = camion.ultima_mantencion.strftime("%Y-%m-%d %H:%M:%S")
   self.lista_camiones.insert(
    tk.END,
    f'{camion.marca} {camion.modelo} - {estado} (Última Mantención: {ultima_mantencion})'
   )

 def buscar_camion(self):
  """Realiza una búsqueda de camiones según el texto ingresado."""
  filtro = self.entrada_buscador.get().strip()
  if filtro:
   self.actualizar_lista_camiones(filtro=filtro)
  else:
   self.actualizar_lista_camiones()

 def arrendar_camion(self):
  """Permite arrendar un camión disponible."""
  seleccion = self.lista_camiones.curselection()
  if not seleccion:
   messagebox.showwarning("Advertencia", "Seleccione un camión para arrendar.")
   return

  index = seleccion[0]
  camion = self.camiones[index]

  if camion.estado == "Disponible":
   camion.estado = "Arrendado"
   self.actualizar_lista_camiones()
   messagebox.showinfo("Éxito", f'El {camion.marca} {camion.modelo} ha sido arrendado.')
  else:
   messagebox.showerror("Error", f'El {camion.marca} {camion.modelo} no está disponible para arriendo.')
  self.guardar_camiones()

 def fin_mantencion_camion(self):
  """Permite arrendar un camión disponible."""
  seleccion = self.lista_camiones.curselection()
  if not seleccion:
   messagebox.showwarning("Advertencia", "Seleccione un camión para arrendar.")
   return

  index = seleccion[0]
  camion = self.camiones[index]

  if camion.estado == "en mantención":
   camion.estado = "Disponible"
   self.actualizar_lista_camiones()
   messagebox.showinfo("Mantención Completada", f' del {camion.marca} {camion.modelo} ha sido reparado.')
  else:
   messagebox.showerror("Error", f'El {camion.marca} {camion.modelo} no está disponible para mantención.')
  self.guardar_camiones()

 def arrendar_(self,m):
  """Arrendar específicamente el Camión 1."""
  camion = self.camiones[m]  # Camión 1 está en el índice 0
  if camion.arrendar():
   messagebox.showinfo("Éxito", f"{camion.marca} ha sido arrendado.")
  else:
   messagebox.showerror("Error", f"{camion.marca} ya está arrendado.")
  self.guardar_camiones()

  self.actualizar_lista_camiones()        

 def devolver_camion(self):
  """Permite devolver un camión arrendado."""
  seleccion = self.lista_camiones.curselection()
  if not seleccion:
   messagebox.showwarning("Advertencia", "Seleccione un camión para devolver.")
   return

  index = seleccion[0]
  camion = self.camiones[index]

  if camion.estado == "Arrendado":
   camion.estado = "Disponible"
   self.actualizar_lista_camiones()
   messagebox.showinfo("Éxito", f'El {camion.marca} {camion.modelo} ha sido devuelto.')
  else:
   messagebox.showerror("Error", f'El {camion.marca} {camion.modelo} no está arrendado.')
  self.guardar_camiones()

 def mantencion_no_programada(self):
  """Permite realizar una mantención no programada, seleccionando una parte específica."""
  seleccion = self.lista_camiones.curselection()
  if not seleccion:
   messagebox.showwarning("Advertencia", "Seleccione un camión para realizar mantención.")
   return

  index = seleccion[0]
  camion = self.camiones[index]

  if camion.estado == "Disponible":
            
   parte = simpledialog.askstring(
    "Parte a Reparar",
    f"Seleccione la parte del {camion.marca} {camion.modelo} a reparar (capacidad, Ruedas, Frenos, Carrocería, Suspensión):"
   )
   if parte not in ["capacidad", "Ruedas", "Frenos", "Carrocería", "Suspensión"]:
    messagebox.showerror("Error", "Parte seleccionada inválida.")
    return

   detalles = simpledialog.askstring(
    "Detalles de Reparación",
    f"Ingrese los detalles de la reparación para la parte {parte}:"
   )

   camion.realizar_mantencion(parte, detalles)
   camion.estado = "en mantención"
   self.actualizar_lista_camiones()
   messagebox.showinfo("Éxito", f'El {camion.marca} {camion.modelo} está en mantencion.')
   self.guardar_camiones()
   
 def gestion_mantencion(self):
  """Programa mantenciones cada 30 días (simulado como 30 segundos)."""
  while True:
   time.sleep(1)  # Revisar cada segundo
   for camion in self.camiones:
    if camion.estado == "Disponible" and camion.necesita_mantencion(dias=30):
     camion.estado = "En Mantención"
     self.actualizar_lista_camiones()
     self.label_estado.config(text=f'{camion.marca} está en mantención...')
     camion.realizar_mantencion()
     camion.estado = "Disponible"
     self.actualizar_lista_camiones()

 def guardar_camiones(self):
   with open("camiones.json", "w") as file:
    json.dump([camion.to_dict() for camion in self.camiones], file, indent=4)
   messagebox.showinfo("Guardado", "Datos guardados correctamente.")

 def agregar_camion(self):
  """
  Solicita datos al usuario para agregar un nuevo camión.
  """
  try:
   motor_id = simpledialog.askinteger("Motor", "ID del motor:")
   motor_tipo = simpledialog.askstring("Motor", "Tipo de motor:")
   motor_cilindrada = simpledialog.askstring("Motor", "Cilindrada:")
   motor_potencia = simpledialog.askstring("Motor", "Potencia:")
   motor_km_lt = simpledialog.askfloat("Motor", "Km por litro:")
   motor_vel_max = simpledialog.askstring("Motor", "Velocidad máxima:")
   motor_rendimiento = simpledialog.askstring("Motor", "Rendimiento:")
   motor_ult_rev = simpledialog.askstring("Motor", "Última revisión:")

   motor = Motor(motor_id, motor_tipo, motor_cilindrada, motor_potencia, motor_km_lt, motor_vel_max, motor_rendimiento, motor_ult_rev)

   patente = simpledialog.askstring("Camión", "Patente:")
   marca = simpledialog.askstring("Camión", "Marca:")
   modelo = simpledialog.askstring("Camión", "Modelo:")
   ano = simpledialog.askinteger("Camión", "Año:")
   capacidad = simpledialog.askstring("Camión", "Capacidad:")
   km_camion = simpledialog.askstring("Camión", "Kilometraje:")
   precio = simpledialog.askstring("Camión", "Precio:")
   tipo = simpledialog.askstring("Camión", "Tipo:")
   peso_max = simpledialog.askstring("Camión", "Peso máximo:")

   nuevo_camion = Camion(motor, patente, marca, modelo, ano, capacidad, km_camion, precio, tipo, peso_max)
   self.camiones.append(nuevo_camion)
   self.guardar_camiones()
   messagebox.showinfo("Éxito", "Camión agregado correctamente.")
  except Exception as e:
   messagebox.showerror("Error", f"No se pudo agregar el camión: {e}")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()  # Llamar al bucle principal de la ventana
