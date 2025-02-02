from task_1 import Book  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":  # TODO: инстанцировать все описанные классы, создав три объекта.C()

    book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1200)
    book2 = Book("The Hobbit", "J.R.R. Tolkien", 300)
    book3 = Book("1984", "George Orwell", 328)

    try:
        book1.read_pages("abc")  # TODO: вызвать метод с некорректными аргументами(b)
    except (TypeError, ValueError):
        print('Ошибка: неправильные данные')

    try:
        book2.read_pages(-100)

    except (TypeError, ValueError):
        print('Ошибка: неправильные данные')

    try:
        book3.read_pages(500)
    except (TypeError, ValueError):
        print('Ошибка: неправильные данные')
