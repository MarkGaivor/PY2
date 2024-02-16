class PaperBook:
    def __init__(self, author:str, name: str, pages: int):
        if not type(name) is str:
            TypeError ('Название книги должно быть типа str')
        self.__name=name
        if not type(author) is str:
            TypeError (' author книги должен быть типа int')

        self.__author=author
        if not type(pages) is int:
            TypeError('pages книги должен быть типа int')
        if pages <= 0:
            TypeError ('pages книги должен быть положительным числом')
        self._pages=pages
    def __str__(self) -> str:
        return f'Книга {self.__author} "{self.__name}"'
    def __repr__(self) -> str:
        return f'PaperBook(pages={self._pages})'
    def pages(self, new_pages :int)-> None:
        if not type(new_pages) is int:
            TypeError('pages книги должен быть типа int')
        if new_pages <= 0:
            TypeError ('pages книги должен быть положительным числом')
        self._pages=new_pages


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        if not type(name) is str:
            TypeError ('Название книги должно быть типа str')
        self.__name=name
        if not type(author) is str:
            TypeError (' author книги должен быть типа int')
        self.__author=author
        if not type(duration) is float:
            TypeError('pages книги должен быть типа int')
        if duration <= 0:
            TypeError ('pages книги должен быть положительным числом')
        self._duration= duration
    def duration(self)-> int:
        return self._duration
    def duration(self, new_duration: float) -> None:
            if not type(new_duration) is int:
                TypeError('duration книги должен быть типа int')
            if new_duration <= 0:
                TypeError('duration книги должен быть положительным числом')
            self._duration = new_duration

    def __str__(self) -> str:
            return f'Книга {self.__author} "{self.__name}"'


    def __repr__(self) -> str:
            return f'AudioBook(duration={self._duration})'
class Book:
    def __init__(self, author: str, name: str):
        if not type(name) is str:
            TypeError('Название книги должно быть типа str')
        self.__name = name
        if not type(author) is str:
            TypeError(' author книги должен быть типа int')
        if author <= 0:
            TypeError('author книги должен быть положительным числом')
        self.__author = author




