from library import Library

def show_menu():
    """Показать меню"""
    print("\n-- Библиотечная система --")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу по названию")
    print("4. Удалить книгу")
    print("5. Добавить новую оценку книге")
    print("6. Книги, выпущенные после определённого года")
    print("7. Книги с рейтингом выше порога")
    print("8. Экспортировать книги в CSV")
    print("9. Импортировать книги из CSV")
    print("0. Выход")
    print("--------------------")

def get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Получить целое число от пользователя с проверкой"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Значение должно быть не меньше {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Значение должно быть не больше {max_val}")
                continue
            return value
        except ValueError:
            print("Пожалуйста, введите целое число")

def get_ratings_input() -> list:
    """Получить список оценок от пользователя"""
    ratings = []
    print("Введите оценки читателей (1-5), пустая строка - завершение:")
    while True:
        try:
            rating_input = input("Оценка: ").strip()
            if not rating_input:
                break
            
            rating = int(rating_input)
            if not 1 <= rating <= 5:
                print("Оценка должна быть от 1 до 5")
                continue
            
            ratings.append(rating)
        except ValueError:
            print("Пожалуйста, введите целое число")
    
    return ratings

def add_book_ui(library: Library):
    """Добавить книгу (UI)"""
    try:
        name = input("Введите название книги: ").strip()
        if not name:
            print("Название не может быть пустым")
            return
        
        author = input("Введите автора: ").strip()
        if not author:
            print("Автор не может быть пустым")
            return
        
        year = get_int_input("Введите год издания: ", 1000, 2100)
        ratings = get_ratings_input()
        
        library.add_book(name, author, year, ratings)
        print(f"Книга '{name}' успешно добавлена!")
        
    except Exception as e:
        print(f"Ошибка при добавлении книги: {e}")

def show_all_books_ui(library: Library):
    """Показать все книги (UI)"""
    books = library.get_all_books()
    if not books:
        print("В библиотеке нет книг")
        return
    
    print("\n-- Все книги в библиотеке --")
    for name, book in books.items():
        avg_rating = book.get_average_rating()
        rating_count = book.get_rating_count()
        print(f"Название: {name}")
        print(f"  Автор: {book.author}")
        print(f"  Год: {book.year}")
        print(f"  Средний рейтинг: {avg_rating} ({rating_count} оценок)")
        if book.ratings:
            print(f"  Оценки: {book.ratings}")
        print("-" * 30)

def find_book_ui(library: Library):
    """Найти книгу по названию (UI)"""
    name = input("Введите название книги для поиска: ").strip()
    if not name:
        print("Название не может быть пустым")
        return
    
    try:
        book = library.find_book(name)
        avg_rating = book.get_average_rating()
        rating_count = book.get_rating_count()
        
        print(f"\n-- Найдена книга --")
        print(f"Название: {name}")
        print(f"Автор: {book.author}")
        print(f"Год: {book.year}")
        print(f"Средний рейтинг: {avg_rating} ({rating_count} оценок)")
        if book.ratings:
            print(f"Оценки: {book.ratings}")
            
    except ValueError as e:
        print(e)

def remove_book_ui(library: Library):
    """Удалить книгу (UI)"""
    name = input("Введите название книги для удаления: ").strip()
    if not name:
        print("Название не может быть пустым")
        return
    
    try:
        library.remove_book(name)
        print(f"Книга '{name}' успешно удалена!")
    except ValueError as e:
        print(e)

def add_rating_ui(library: Library):
    """Добавить оценку книге (UI)"""
    name = input("Введите название книги: ").strip()
    if not name:
        print("Название не может быть пустым")
        return
    
    try:
        rating = get_int_input("Введите оценку (1-5): ", 1, 5)
        author = input("Введите ваше имя: ").strip()
        if not author:
            author = "Аноним"
        
        library.add_rating_to_book(name, rating, author)
        print(f"Оценка {rating} успешно добавлена к книге '{name}'!")
        
    except ValueError as e:
        print(e)

def books_after_year_ui(library: Library):
    """Книги после определённого года (UI)"""
    try:
        year = get_int_input("Введите год: ", 1000, 2100)
        books = library.get_books_after_year(year)
        
        if not books:
            print(f"Нет книг, выпущенных после {year} года")
            return
        
        print(f"\n-- Книги, выпущенные после {year} года --")
        for name, book in books.items():
            avg_rating = book.get_average_rating()
            print(f"{name} - {book.author} ({book.year}), рейтинг: {avg_rating}")
            
    except Exception as e:
        print(f"Ошибка: {e}")

def books_above_rating_ui(library: Library):
    """Книги с рейтингом выше порога (UI)"""
    try:
        min_rating = float(input("Введите минимальный рейтинг (0-5): "))
        if not 0 <= min_rating <= 5:
            print("Рейтинг должен быть от 0 до 5")
            return
        
        books = library.get_books_above_rating(min_rating)
        
        if not books:
            print(f"Нет книг с рейтингом выше {min_rating}")
            return
        
        print(f"\n-- Книги с рейтингом выше {min_rating} --")
        for name, book in books.items():
            avg_rating = book.get_average_rating()
            print(f"{name} - {book.author} ({book.year}), рейтинг: {avg_rating}")
            
    except ValueError:
        print("Пожалуйста, введите число")

def export_books_ui(library: Library):
    """Экспорт в CSV (UI)"""
    filename = input("Введите имя файла для экспорта (например: books.csv): ").strip()
    if not filename:
        print("Имя файла не может быть пустым")
        return
    
    try:
        library.export_to_csv(filename)
        print(f"Книги успешно экспортированы в файл '{filename}'")
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def import_books_ui(library: Library):
    """Импорт из CSV (UI)"""
    filename = input("Введите имя файла для импорта: ").strip()
    if not filename:
        print("Имя файла не может быть пустым")
        return
    
    try:
        initial_count = len(library.get_all_books())
        library.import_from_csv(filename)
        final_count = len(library.get_all_books())
        added_count = final_count - initial_count
        print(f"Успешно импортировано {added_count} книг из файла '{filename}'")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")

def main():
    library = Library()
    
    try:
        library.add_book("Война и мир", "Л. Толстой", 1869, [5, 4, 5])
        library.add_book("Преступление и наказание", "Ф. Достоевский", 1866, [5, 5, 4])
    except:
        pass
    
    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()
        
        if choice == '1':
            add_book_ui(library)
        elif choice == '2':
            show_all_books_ui(library)
        elif choice == '3':
            find_book_ui(library)
        elif choice == '4':
            remove_book_ui(library)
        elif choice == '5':
            add_rating_ui(library)
        elif choice == '6':
            books_after_year_ui(library)
        elif choice == '7':
            books_above_rating_ui(library)
        elif choice == '8':
            export_books_ui(library)
        elif choice == '9':
            import_books_ui(library)
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()
