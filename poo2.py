class student:
    def _init_(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas 

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

est1 = student("Alex", [4.0, 3.8, 4.5, 5.0])
promedio = est1.calcular_promedio()
print(f"El promedio de {est1.nombre} es {promedio:.2f}")