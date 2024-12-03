#Se crea la clase principal "camion"

class camion: 
 def __init__(self, patente, marca, modelo, ano, capacidad, km_camion, precio, tipo, peso_max, disponible, mantenciones_mes, prom_mes): #Atributos de la clase "camion"
  self.patente = patente
  self.marca = marca
  self.modelo = modelo
  self.ano = ano
  self.capacidad = capacidad
  self.km_camion = km_camion
  self.precio = precio
  self.tipo = tipo
  self.peso_max = peso_max
  self.disponible = disponible
  self.mantenciones_mes = mantenciones_mes
  self.prom_mes = prom_mes

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
 
 def actualizar_precio(self): #actualizar en función al año y km
  ano = 2024 #hacer q año vaya al día
  d=0
  if self.ano < ano:
   ano - self.ano = d
   if 5<= d >= 1:
    self.precio -= self.precio * (d*0.05)
    if self.km_camion >= 850000:
     self.precio -= self.precio * 0.03

 def ver_precio(self):
  return f"Precio: {self.precio}"

 def ver_tipo(self):
  return f"Tipo: {self.tipo}"

#  def disponible(self): VERRRRRR
  
#   pass

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

class motor(camion):
 def __init__(self, id, patente, marca, modelo, ano, tipo, cilindrada, potencia, km_lt, vel_max, rendimiento, ult_rev, falla, fallas):
  self.id = id
  self.patente = patente
  self.marca = marca
  self.modelo = modelo
  self.ano = ano
  self.tipo = tipo
  self.cilindrada = cilindrada
  self.potencia = potencia
  self.km_lt = km_lt
  self.vel_max = vel_max
  self.rendimiento = rendimiento
  self.ult_rev = ult_rev
  self.falla = falla
  self.fallas = fallas

 def actualizar_ult_rev(self):
   
  pass