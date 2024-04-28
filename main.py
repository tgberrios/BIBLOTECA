class Book:
    def __init__(self, title):
        self.title = title

    def to_string(self):
        return self.title

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"El libro '{book.title}' ha sido agregado correctamente.")

    def remove_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            book = found_books[0]
            self.books.remove(book)
            self.save_books()
            print(f"El libro '{book.title}' ha sido eliminado correctamente.")
        else:
            print("No se encontró el libro en la biblioteca.")

    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print("Libros encontrados: ")
            for book in found_books:
                print(f"Título: {book.title}")
        else:
            print("No se encontraron libros con ese título.")

    def display_books(self):
        if self.books:
            print("Lista de libros en la biblioteca:")
            for book in self.books:
                print(f"Título: {book.title}")
        else:
            print("La biblioteca está vacía. No hay libros para mostrar.")

    def save_books(self):
        with open("database.txt", "w") as file:
            for book in self.books:
                file.write(book.to_string() + "\n")

    def load_books(self):
        try:
            with open("database.txt", "r") as file:
                for line in file:
                    title = line.strip()
                    book = Book(title)
                    self.books.append(book)
        except FileNotFoundError:
            print("No se encontró la base de datos. Se creará una nueva.")

def main():
    library = Library()

    while True:
        print("\n*** Biblioteca ***")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Buscar libro")
        print("4. Mostrar todos los libros")
        print("5. Salir")

        choice = input("Ingrese su elección: ")

        if choice == '1':
            title = input("Ingrese el título del libro: ")
            book = Book(title)
            library.add_book(book)
        elif choice == '2':
            title = input("Ingrese el título del libro que desea eliminar: ")
            library.remove_book(title)
        elif choice == '3':
            title = input("Ingrese el título del libro que desea buscar: ")
            library.search_book(title)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, elija nuevamente.")

if __name__ == "__main__":
    main()
