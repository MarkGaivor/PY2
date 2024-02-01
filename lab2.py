class Book:
    def __init__(self, id: int, name:str, page: int ):
        if not isinstance(self, id):
            raise TypeError('Айди книги должен быть типа int')
        if id < 0:
            raise ValueError("Айди книги должно быть положительным числом")
        self.id = id
        if not isinstance(self, name):
            raise TypeError('Название книги должен быть типа str')
        self.name=name
        if not isinstance(self, page):
            raise TypeError('Количество страниц книги должен быть типа int')
        if page < 0:
            raise ValueError("Количество страниц книги должно быть положительным числом")
        self.page = page
    def __str__(self)->str:
        return f'Книга "{self.name}"'
    def __repr__(self)->str:
        return f'Книга (id={self.id}, name={ self.name!r} pages={self.page})'
class Library:
    def __init__(self, books: list):
        if len(books) == 0:
           return books
        else:
            self.books=books
    def get_next_book_id(self, id: int):
        if len(books) == 0:
            return 1
        else:
            id+=1
            return id
    def get_index_by_book_id(self, id:int):
        if id in self.books:
            return self.books.index[id]
        else:
            raise ValueError('книга не найдена')











