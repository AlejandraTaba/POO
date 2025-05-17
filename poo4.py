class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado_a = None  

    def prestar(self, usuario):
        if self.prestado_a is None:
            self.prestado_a = usuario
            return f"El libro '{self.titulo}' fue prestado a {usuario.nombre}."
        else:
            return f"El libro '{self.titulo}' ya está prestado a {self.prestado_a.nombre}."

    def devolver(self):
        if self.prestado_a is None:
            return f"El libro '{self.titulo}' no está prestado."
        else:
            usuario = self.prestado_a
            self.prestado_a = None
            return f"{usuario.nombre} devolvió el libro '{self.titulo}'."

    def estado(self):
        if self.prestado_a:
            return f"Prestado a {self.prestado_a.nombre}"
        else:
            return "Disponible"

usuario1 = Usuario("Alex")
libro1 = Libro("Los secretos de la mente millonaria")

print(libro1.estado())
print(libro1.prestar(usuario1))
print(libro1.estado())
print(libro1.devolver())
print(libro1.estado())