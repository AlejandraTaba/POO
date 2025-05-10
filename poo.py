class computadora:
    def __init__(self, modelo, marca, almacenamiento, ram):
        self.modelo = modelo
        self.marca = marca
        self.almacenamiento = almacenamiento
        self.ram = ram

pc = computadora("x13", "lenovo", "256", "16")

print("Datos PC:", "Modelo:", pc.modelo, "Marca:", pc.marca, "Almacenamiento:", pc.almacenamiento, "RAM:", pc.ram)

def light(self):
    if not self.inicia:
        self.inicia = True
        print(f"Laptop {self.marca} {self.modelo} esta encendida")
    else:
        print("Laptop ya está iniciando")

def off(self):
    if self.inicia:
        self.inicia = False
        print(f"Laptop {self.marca} {self.modelo} esta apagada")
    else:
        print("Laptop ya está apagando")

def update_ram(self, new_ram):
    if not self.inicia:
        print("Despues de insertar la ram, encienda el equipo para actualizar la ram")
        return
    if new_ram > self.ram:
        print(f"Actualizando RAM {self.ram} GB a {new_ram} GB")
        self.ram = new_ram
    else:
        print("La nueva RAM debe ser mayor que la actual")

mi_computadora = computadora("X13", "Lenovp", 256, 8)
mi_computadora.encender()
mi_computadora.actualizar_ram(16)
mi_computadora.apagar()