import doctest


# TODO: Подробно описать три произвольных класса


class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        pages (int): Количество страниц в книге.
        current_page (int): Номер текущей прочитанной страницы.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц в книге.

        Raises:
            TypeError: Если название или автор не являются строками
             или если количество страниц не является целым числом.
            ValueError: Если количество страниц не является положительным числом.

        Examples:
            >>> book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1200)
        """
        if not isinstance(title, str):
            raise TypeError
        if not isinstance(author, str):
            raise TypeError
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError

        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

# TODO: описать класс
    def is_read(self) -> bool:
        """
        Функция, которая проверяет, прочитана ли книга до конца.

        Returns:
            bool: True, если книга прочитана до конца, False - если нет.

        Examples:
            >>> book = Book("The Hobbit", "J.R.R. Tolkien", 300)
            >>> book.is_read()
            False
            >>> book.current_page = 300
            >>> book.is_read()
            True
        """
        return self.current_page == self.pages

# TODO: описать ещё класс
    def read_pages(self, pages_to_read: int) -> None:
        """
        Увеличение количества прочитанных страниц.

        Args:
             pages_to_read (int): Количество страниц для прочтения.

        Raises:
            TypeError: Если количество страниц для прочтения не является целым числом.
            ValueError: Если количество страниц для прочтения не является положительным числом
            или превышает количество страниц в книге.

        Examples:
            >>> book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)
            >>> book.read_pages(100)
            >>> book.current_page
            100
            >>> book.read_pages(300)
            Traceback (most recent call last):
            ...
            ValueError: Количество страниц для прочтения превышает количество страниц в книге
        """
        if not isinstance(pages_to_read, int):
            raise TypeError("Количество страниц для прочтения должно быть целым числом")
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для прочтения должно быть положительным числом")
        if self.current_page + pages_to_read > self.pages:
            raise ValueError("Количество страниц для прочтения превышает количество страниц в книге")
        self.current_page += pages_to_read
# TODO: и ещё один

    def get_progress(self) -> float:
        """
        Возвращает прогресс чтения книги в процентах.

        Returns:
            float: Прогресс чтения книги в процентах.

        Examples:
            >>> book = Book("Devils", "Fyodor Dostoevksy", 641)
            >>> book.read_pages(164)
            >>> book.get_progress()
            50.0
            >>> book.current_page = 328
            >>> book.get_progress()
            100.0
        """
        return (self.current_page / self.pages) * 100


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
