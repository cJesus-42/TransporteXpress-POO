import tkinter as tk

class PaginaWebTkinter:
 def __init__(self):
  # Ventana principal
  self.ventana = tk.Tk()
  self.ventana.title("TransporteXpress")
  self.ventana.geometry("1000x800")
  self.ventana.configure(bg="#FFE5B4")

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

 def crear_etiqueta_informacion(self, contenedor, modelo, patente, tipo_mantencion, fecha_inicio, fecha_termino, fila, columna):
  # Crear el texto formateado
  texto = (f"{modelo}\n"
  f"Patente: {patente}\n"
  f"Tipo de mantención: {tipo_mantencion}\n"
  f"Fecha de inicio: {fecha_inicio}\n"
  f"Fecha de término (aprox): {fecha_termino}")

  # Crear la etiqueta con el texto formateado
  etiqueta = tk.Label(
  contenedor,
  text=texto,
  font=("Arial", 10),
  bg="white",
  wraplength=250,
  justify="left"
  )
  etiqueta.grid(row=fila, column=columna, padx=0, pady=10, sticky="nsew")

 def crear_boton(self, contenedor, texto, comando, fila, columna):
  # Crear el botón con propiedades especificadas
  boton = tk.Button(
  contenedor,
  text=texto,
  font=("Arial", 10),
  bg="#FFF5E1",
  highlightbackground="#FF8C42",
  highlightthickness=2,
  command=comando
  )
  boton.grid(row=fila, column=columna, sticky="nsew", padx=10, pady=10)

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

  self.crear_etiqueta_informacion(
  self.contenido,
  modelo="Renault TruckGama D",
  patente="DDCC12",
  tipo_mantencion="Preventiva",
  fecha_inicio="02-10-24",
  fecha_termino="15-10-24",
  fila=1,
  columna=1
  )

  # Agregar un botón debajo del texto
  self.crear_boton(
  contenedor=self.contenido,
  texto="Ficha técnica",
  comando=self.mostrar_Ficha_Tecnica1,
  fila=2,
  columna=1
  )

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

  self.crear_etiqueta_informacion(
  self.contenido,
  modelo="Volvo Gama FH",
  patente="AA1122",
  tipo_mantencion="Preventiva",
  fecha_inicio="01-11-24",
  fecha_termino="02-12-24",
  fila=1,
  columna=1
  )

  self.crear_boton(
  contenedor=self.contenido,
  texto="Ficha técnica",
  comando=self.mostrar_Ficha_Tecnica1,
  fila=2,
  columna=1
  )

  self.espaciado(self.contenido,3,1)

  self.crear_etiqueta_informacion(
  self.contenido,
  modelo="Volvo Gama FH",
  patente="BBCC11",
  tipo_mantencion="Reparación",
  fecha_inicio="03-11-24",
  fecha_termino="05-12-24",
  fila=4,
  columna=1
  )

  boton = tk.Button(self.contenido, text="Ficha técnica", font=("Arial", 10),bg="#FFF5E1", highlightbackground="#FF8C42", highlightthickness=2, command= self.mostrar_Ficha_Tecnica)
  boton.grid(row=5, column=1, sticky="nsew")

  etiqueta = tk.Label(self.contenido, text="                       ", font=("Arial", 12), bg="white", wraplength=250)
  etiqueta.grid(row=6, column=1, padx=0, pady=20, sticky="nsew")

  self.crear_etiqueta_informacion(
  self.contenido,
  modelo="Renault Trucks Gama D",
  patente="CCDD22",
  tipo_mantencion="Preventiva",
  fecha_inicio="10-11-24",
  fecha_termino="25-1-25",
  fila=7,
  columna=1
  )

  boton = tk.Button(self.contenido, text="Ficha técnica", font=("Arial", 10),bg="#FFF5E1", highlightbackground="#FF8C42", highlightthickness=2, command= self.mostrar_Ficha_Tecnica)
  boton.grid(row=8, column=1, sticky="nsew")

  self.espaciado(self.contenido,9,1)

  self.espaciado(self.contenido,1,5)

  etiqueta = tk.Label(self.contenido, text="                       ", font=("Arial", 12), bg="white", wraplength=250)
  etiqueta.grid(row=1, column=2, padx=0, pady=5, sticky="nsew")

  # Segunda columna
  etiqueta = tk.Label(self.contenido, text="Mantenciones programadas", font=("Arial", 15), bg="white", fg="#FF8C42", wraplength=300, justify="left")
  etiqueta.grid(row=0, column=3, padx=0, pady=5, sticky="nsew")

  self.crear_etiqueta_informacion(
  self.contenido,
  modelo="Renault Trucks Gama D",
  patente="CCDD22",
  tipo_mantencion="Preventiva",
  fecha_inicio="04-11-24",
  fecha_termino="05-12-24",
  fila=1,
  columna=4
  )

  self.crear_boton(
  contenedor=self.contenido,
  texto="Ficha técnica",
  comando=self.mostrar_Ficha_Tecnica1,
  fila=2,
  columna=4
  )

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

 def mostrar_Fichas_Tecnicas(self):
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

 def mostrar_Ficha_Tecnica(self, contenedor, modelo, tipo, ejes, norma, longitud, ancho, alto, Dejes, peso, pesot, motor, cilindrada, Ncilindros, potencia, par, refri, caja, marchas, carga, consumo, freno, cabina, sistema, tec, fila1, columna1, fila2, columna2, fila3, columna3):

  texto = (f"{modelo}\n")

  # Crear la etiqueta con el texto formateado
  etiqueta = tk.Label(
  contenedor,
  text=texto,
  font=("Arial", 15),
  bg="white",
  fg="#FF8C42",
  wraplength=250,
  justify="left"
  )
  etiqueta.grid(row=fila1, column=columna1, padx=0, pady=10, sticky="nsew")

  texto1 = (f"Información General:\n"
   f"Modelo: {modelo}\n"
   f"Tipo de Vehiculo: {tipo}\n"
   f"Configuracion de Ejes: {ejes}\n"
   f"Norma de Emisiones: {norma}\n"
   f"\n"
   f"\n"
   f"Dimensiones:\n"
   f"Longitud Total: {longitud}\n"
   f"Anchura: {ancho}\n"
   f"Altura Cabina: {alto}\n"
   f"Distancia Entre Ejes: {Dejes}\n"
   f"Peso Máximo Autorizado (MMA): {peso}\n"
   f"Peso Total Combinado (PTAC): {pesot}\n"
   f"\n"
   f"\n"
   f"Motor:\n"
   f"Motor: {motor}\n"
   f"Cilindrada: {cilindrada}\n"
   f"Número de Cilindros: {Ncilindros}\n"
   f"Potencia Máxima: {potencia}\n"
   f"Par Máximo: {par}\n"
   f"Sistema de Refrigeración: {refri}\n"
   f"\n")

  texto2 = (f"Transmisión:\n"
   f"Caja de Cambios: {caja}\n"
   f"Número de Marchas: {marchas}\n"
   f"\n"
   f"\n"
   f"Rendimiento y Capacidad:\n"
   f"Capacidad de Carga: {carga}\n"
   f"Consumo de Combustible: {consumo}\n"
   f"Freno Motor VEb+: {freno}\n"
   f"\n"
   f"\n"
   f"Características Adicionales:\n"
   f"Cabina: {cabina}\n"
   f"Sistema de Climatización: {sistema}\n"
   f"Tecnología Avanzada: {tec}\n"
   f"\n")

  # Crear la etiqueta con el texto formateado
  etiqueta = tk.Label(
  contenedor,
  text=texto1,
  font=("Arial", 10),
  bg="white",
  wraplength=300,
  justify="left"
  )
  etiqueta.grid(row=fila2, column=columna2, padx=10, pady=10, sticky="nsew")

  etiqueta = tk.Label(
  contenedor,
  text=texto2,
  font=("Arial", 10),
  bg="white",
  wraplength=260,
  justify="left"
  )
  etiqueta.grid(row=fila3, column=columna3, padx=10, pady=10, sticky="nsew")

  self.espaciado(self.contenido,3,1)

  self.espaciado(self.contenido,3,6)

  self.espaciado(self.contenido,3,5)

  self.espaciado(self.contenido,3,4)

  self.espaciado(self.contenido,3,3)

  self.espaciado(self.contenido,3,2)

PaginaWebTkinter()

#Se crea la clase principal "camion"

class camion: 
  def __init__(self, patente, marca, modelo, ano, capacidad, km_camion, precio, tipo, peso_max, disponible, mantenciones_mes, prom_mes): #Atributos de la clase "camion"
    self.patente = patente                                            #string
    self.marca = marca                                                #string
    self.modelo = modelo                                              #string
    self.ano = ano                                                    #t
    self.capacidad = capacidad                                        #capacidad del remolque en metro cúbicos, float
    self.km_camion = km_camion                                        #kilometraje, float
    self.precio = precio                                              #int
    self.tipo = tipo                                                  #tipo de camión, string
    self.peso_max = peso_max                                          #kilo, float
    self.disponible = disponible                                      #booleano
    self.mantenciones_mes = mantenciones_mes                          #int
    self.prom_mes = prom_mes                                          #float

  #Se crean los métodos
  def ver_patente(self):
    return f"Patente: {self.patente}"

  def ver_marca(self):
    return f"Marca: {self.marca}"

  def ver_modelo(self):
    return f"Modelo: {self.modelo}"

  def ver_ano(self):
    return f"Año: {self.ano}"

  def ver_capacidad(self):
    return f"Capacidad: {self.capacidad}"

  def ver_km_camion(self):
    return f"Marca: {self.km_camion}"
 
  def actualizar_precio(self):                                #actualizar en función al año y km
    ano = 2024                                                #hacer q año vaya al día
    d=0
    if self.ano < ano:                                        #se compara el año del camión con el año actual
      ano - self.ano = d                                      #se determina si es necesario realizar una actualización de precio
    if 5>= d >= 1:                                            #si el camión excede el año se comenzarán a hacer los descuentos 
        self.precio -= self.precio * (d*0.05)                 #Se realiza el descuento acorde a los años de diferencia
    if d > 5:                                                 #si excede los 5 años
      self.precio -= self.precio * 0.25                       #se realiza un descuento fijo del 0.25
    if self.km_camion >= 850000:                              #si excede los 850.000 km se realizará otro descuento
      self.precio -= self.precio * 0.03                       #se realiza el descuento nuevamente

  def ver_precio(self):
    return f"Precio: {self.precio}"

  def ver_tipo(self):
    return f"Tipo: {self.tipo}"

#  def ver_disponible(self):
#   return f"Disponible: {self.disponible}"

  def ver_peso_max(self):
    return f"Peso maximo: {self.peso_max}"

 # def ver_mantenciones_mes(self):
 #  return f"Mantenciones del mes: {self.mantenciones_mes}"

 # def ver_prom_mes(self):
 #  return f"Promedio mensaual de mantenciones: {self.prom_mes}"

 # def ver_ficha_tecnica(self):
 #  return f"Marca: {self.marca}\nModelo: {self.modelo}"   VERRRRR

class motor(camion): #Se crea la clase motor que hereda los atributos de camion
  def __init__(self, id, patente, marca, modelo, ano, tipo, cilindrada, potencia, vel_max, lt, rendimiento, ult_rev, falla, fallas):
    self.id = id
    self.patente = patente
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.tipo = tipo
    self.cilindrada = cilindrada                      #volumento total de los cilindros del motor, se mide en cc
    self.potencia = potencia
    self.vel_max = vel_max                            #al que puede llegar el camión
    self.lt= lt                                       #litros consumidos
    self.rendimiento = rendimiento                    #km que se avanzan por litro
    self.ult_rev = ult_rev
    self.falla = falla                                #booleano, sí o no
    self.fallas = fallas                              #tipo de falla

  #def actualizar_ult_rev(self):
    

  def actualizar_rendimiento(self):
    self.km_camion/self.lt= self.rendimiento
  

class estanque (camion):
  def __init__(self, id, capacidad, lt_actuales, tipo_estanque, modificacion, ult_rev, falla, fallas):
    self.id = id
    self.capacidad = capacidad
    self.lt_actuales = lt_actuales
    self.tipo_estanque = tipo_estanque
    self.modificacion = modificacion
    self.ult_rev = ult_rev
    self.falla = falla
    self.fallas = fallas

  #def actualizar_ult_rev(self):
    

class fallas:
  def __init__(self,id, descripcion, cantidad, motor, estanque, fecha):
    self.id = id                                #Patente+letra
    self.descripcion = descripcion
    self.cantidad = cantidad                    #1 o 2
    self.motor = motor                          #booleano
    self.estanque = estanque                    #booleano
    self.fecha = fecha                          #cuándo empezó la falla

  def agregar_descripcion(self):
    self.descripcion= input("Describa la/s falla/s encontradas: ")

  #def fallas(s)

class mantencion(fallas):
  def __init__ (self, id, tipo, fecha_i, fecha_t, fecha_p, dias, detalle, responsable, prom_dias):
    self.id = id                                #contador de mantenciones realizadas que se reinicia cuando incia el sgte año(representado en letra)
    self.tipo = tipo                            #string
    self.fecha_i = fecha_i                      #fecha de inicio de la mantención, string
    self.fecha_t = fecha_t                      #fecha de término de la mantención, string
    self.fecha_p = fecha_p                      #fecha de próxima mantención, string
    self.dias = dias                            #int
    self.detalle = detalle                      #string
    self.responsable = responsable              #string
    self.prom_dias = prom_dias                  #int

#ultima revision de motor y estanque
  def registro_mantencion(self):
    self.responsable = input()

  def detalle(self):
    pass
