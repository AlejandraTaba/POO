class user:
    def __init__(self, nombre):
        self.nombre = nombre

class book:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado_a = []  

    def prestar(self, usuario):
        if not self.prestado_a: 
            self.prestado_a = usuario
            return f"El libro '{self.titulo}' fue prestado a {usuario.nombre}."
        else:
            return f"El libro '{self.titulo}' ya está prestado a {self.prestado_a.nombre}."

    def devolver(self):
        if not self.prestado_a:
            return f"El libro '{self.titulo}' no está prestado."
        else:
            usuario = self.prestado_a
            self.prestado_a = []
            return f"{usuario.nombre} devolvió el libro '{self.titulo}'."

    def estado(self):
        if self.prestado_a:
            return f"Prestado a {self.prestado_a.nombre}"
        else:
            return "Disponible"

user1 = user("Alex")
book1 = book("Los secretos de la mente millonaria")

print(book1.estado())
print(book1.prestar(user1))
print(book1.estado())
print(book1.devolver())
print(book1.estado())