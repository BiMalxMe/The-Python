class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):#str methos are automatically called 
        return f"'{self.title}' by {self.author}"

b = Book("1984", "George Orwell")
print(b)  # Output: '1984' by George Orwell