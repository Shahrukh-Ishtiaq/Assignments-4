class Book:
    total_books = 0

    def __init__(self):
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

b1 = Book()
b2 = Book()
print(Book.total_books)
