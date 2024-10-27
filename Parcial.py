class Member:
    def __init__(self, name, id, borrowed_books=None):
        self.name = name
        self.__id = id 
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
        
#prestamos libros
    def borrow_book(self, book):
        if book.is_available():
            self.borrowed_books.append(book)
            book.set_availability(False)
            print(f"{self.name} ha tomado prestado el libro '{book.title}'.")
        else:
            print(f"El libro '{book.title}' no está disponible.")

#devolvemos libros
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.set_availability(True)
            print(f"{self.name} ha devuelto el libro '{book.title}'.")
        else:
            print(f"El libro '{book.title}' no fue tomado por {self.name}.")

    def __str__(self):
        return f"Miembro: {self.name}, ID: {self.__id}, Libros prestados: {[book.title for book in self.borrowed_books]}"

    def __repr__(self):
        return self.__str__()

class MemberVIP(Member):
    def __init__(self, name, id, borrowed_books=None, limit_books=10):
        super().__init__(name, id, borrowed_books)
        self.limit_books = limit_books

#prestamos libros sin exceder los 10 libros
    def borrow_book(self, book):
        if len(self.borrowed_books) < self.limit_books:
            super().borrow_book(book)
        else:
            print(f"{self.name} ha alcanzado el límite de préstamos.")

    def __str__(self):
        return f"Miembro VIP: {self.name}, ID: {self.__id}, Libros prestados: {[book.title for book in self.borrowed_books]}, Límite de préstamos: {self.limit_books}"

    def __repr__(self):
        return self.__str__()

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.__isbn = isbn 
        self.available = available

    def is_available(self):
        return self.available

    def set_availability(self, status):
        self.available = status

    def __repr__(self):
        return f"Título del libro: {self.title}, Autor: {self.author}, ISBN: {self.__isbn}, Disponible: {self.available}"

class Library:
    def __init__(self, title, books=None):
        self.title = title
        self.books = books if books is not None else []

    def add_book(self, new_book):
        self.books.append(new_book)
        print(f"Libro '{new_book.title}' agregado a la biblioteca.")
        return new_book

    def show_book(self, index):
        return self.books[index] if index < len(self.books) else "Índice fuera de rango"

    def show_books(self):
        return self.books

    def remove_book(self, index):
        if index < len(self.books):
            removed_book = self.books.pop(index)
            print(f"Libro '{removed_book.title}' eliminado de la biblioteca.")
        else:
            print("Índice fuera de rango")

# Creamos la biblioteca
mi_biblioteca = Library("Biblioteca Central")

# Agregamos libros a la biblioteca
libro1 = mi_biblioteca.add_book(Book("1000 años de soledad", "Lina Rodríguez", "54321"))
print()
libro2 = mi_biblioteca.add_book(Book("El mundo de los sordos", "Mario Gómez", "98765"))

# Creamos miembros 
miembro = Member("Luis", "001")
miembro_vip = MemberVIP("María", "002")

# Préstamos de libros
print() 
miembro.borrow_book(libro1)
print()  
miembro_vip.borrow_book(libro2)
print()  

# Intento de préstamo de un libro no disponible
miembro.borrow_book(libro2)
print()  

# Devolución de libros
miembro.return_book(libro1)
print()  
miembro_vip.return_book(libro2)
print()  

# Mostramos todos los libros en la biblioteca con espacio entre cada libro
for book in mi_biblioteca.show_books():
    print(book)
    print()  

