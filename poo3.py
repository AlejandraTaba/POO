class book:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if self.prestado:
            return f"El libro '{self.titulo}' ya está prestado."
        else:
            self.prestado = True
            return f"Has prestado el libro '{self.titulo}'."

    def devolver(self):
        if not self.prestado:
            return f"El libro '{self.titulo}' no estaba prestado."
        else:
            self.prestado = False
            return f"Has devuelto el libro '{self.titulo}'."

    def estado(self):
        return "Prestado" if self.prestado else "Disponible"

book1 = book("Los secretos de la mente millonaria", "T. Harv Eker")

print(book1.estado())
print(book1.prestar())
print(book1.estado())
print(book1.prestar())
print(book1.devolver())
print(book1.estado())