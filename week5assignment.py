# Assignment 1: Design Your Own Class

class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self._pages = pages  
        self.genre = genre

    def read(self):
        print(f"Reading '{self.title}' by {self.author}.")

    def get_summary(self):
        print(f"'{self.title}' is a {self.genre} book with {self._pages} pages.")

    def get_pages(self):  
        return self._pages


# Subclass with inheritance and polymorphism
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size):
        super().__init__(title, author, pages, genre)
        self.file_size = file_size

    def read(self):  # Polymorphism (overridden method)
        print(f"Reading the eBook '{self.title}' on a digital device.")

    def download(self):
        print(f"Downloading '{self.title}'... File size: {self.file_size}MB")
# Creating instances
physical_book = Book("1984", "George Orwell", 328, "Dystopian")
ebook = EBook("Digital Minimalism", "Cal Newport", 254, "Self-Help", 3.5)


physical_book.read()
physical_book.get_summary()
print(f"Pages: {physical_book.get_pages()}")


ebook.read()          # Overridden method
ebook.get_summary()   # Inherited method
ebook.download()      # New method in subclass
print(f"Pages: {ebook.get_pages()}")


#Activity 2: Polymorphism Challenge! 


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclasses with different implementations of move()
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴‍♀️")

vehicles = [Car(), Plane(), Boat(), Bicycle()]


for vehicle in vehicles:
    vehicle.move()
