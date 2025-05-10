class computadora:
    def __init__(self, modelo, marca, almacenamiento, ram):
        self.modelo = modelo
        self.marca = marca
        self.almacenamiento = almacenamiento
        self.ram = ram

pc = computadora("x13", "lenovo", "256", "16")

print("Datos PC:", "Modelo:", pc.modelo, "Marca:", pc.marca, "Almacenamiento:", pc.almacenamiento, "RAM:", pc.ram)