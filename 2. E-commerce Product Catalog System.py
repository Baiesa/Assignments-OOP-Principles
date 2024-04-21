'''
Task 2: Implement Subclasses for Specific Products

Create subclasses Book, Electronic, and Clothing that inherit from Product.
Each subclass should have additional attributes relevant to its category (e.g., author for books, 
specs for electronics, size for clothing).
Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to
 the product type.
Task 3: Override Display Method in Subclasses

Override the method to display product information in each subclass to include specific attributes.
For example, the Book class should display the author, Electronic should display specs, etc.
Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.
Task 4: Test Product Catalog Functionality

Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating 
inheritance and method overriding.
'''


# is very hard assigments 

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print("Author:", self.author)


class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print("Specifications:", self.specs)


class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print("Size:", self.size)



book = Book("B001", "Python Programming", 39.99, "John Doe")
book.display_info()

electronic = Electronic("E001", "Laptop", 999.99, "Intel i7, 16GB RAM")
electronic.display_info()

clothing = Clothing("C001", "T-Shirt", 19.99, "Large")
clothing.display_info()