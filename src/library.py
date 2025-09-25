class BookData:
    def __init__(self, author: str, year: int, ratings: list = None):
        if ratings is None:
            ratings = []
        
        self.author = author
        self.year = year
        self.ratings = ratings
    
    def add_rating(self, rating: int, author: str):
        """Добавить новую оценку"""
        if not 1 <= rating <= 5:
            raise ValueError("Рейтинг должен быть от 1 до 5")
        self.ratings.append(rating)
    
    def get_average_rating(self) -> float:
        """Получить средний рейтинг"""
        if not self.ratings:
            return 0.0
        return round(sum(self.ratings) / len(self.ratings), 2)
    
    def get_rating_count(self) -> int:
        """Получить количество оценок"""
        return len(self.ratings)

class Library:
    def __init__(self):
        self.book_dict = {}
    
    def add_book(self, name: str, author: str, year: int, ratings: list = None):
        """Добавить книгу в библиотеку"""
        if name in self.book_dict:
            raise ValueError(f"Книга с названием '{name}' уже существует")
        
        if ratings is None:
            ratings = []
        
        self.book_dict[name] = BookData(author, year, ratings)
    
    def remove_book(self, name: str):
        """Удалить книгу из библиотеки"""
        if name not in self.book_dict:
            raise ValueError(f"Книга с названием '{name}' не найдена")
        del self.book_dict[name]
    
    def find_book(self, name: str) -> BookData:
        """Найти книгу по названию"""
        if name not in self.book_dict:
            raise ValueError(f"Книга с названием '{name}' не найдена")
        return self.book_dict[name]
    
    def get_all_books(self) -> dict:
        """Получить все книги"""
        return self.book_dict.copy()
    
    def add_rating_to_book(self, book_name: str, rating: int, author: str):
        """Добавить оценку к книге"""
        if book_name not in self.book_dict:
            raise ValueError(f"Книга с названием '{book_name}' не найдена")
        
        self.book_dict[book_name].add_rating(rating, author)
    
    def get_books_after_year(self, year: int) -> dict:
        """Получить книги, выпущенные после указанного года"""
        result = {}
        for name, book in self.book_dict.items():
            if book.year > year:
                result[name] = book
        return result
    
    def get_books_above_rating(self, min_rating: float) -> dict:
        """Получить книги с рейтингом выше указанного порога"""
        result = {}
        for name, book in self.book_dict.items():
            if book.get_average_rating() > min_rating:
                result[name] = book
        return result
    
    def export_to_csv(self, filename: str):
        """Экспортировать книги в CSV файл"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("название;автор;год;оценки\n")
                for name, book in self.book_dict.items():
                    ratings_str = ','.join(map(str, book.ratings))
                    file.write(f"{name};{book.author};{book.year};{ratings_str}\n")
        except Exception as e:
            raise Exception(f"Ошибка при экспорте в CSV: {e}")
    
    def import_from_csv(self, filename: str):
        """Импортировать книги из CSV файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    parts = line.split(';')
                    if len(parts) < 4:
                        continue
                    
                    name = parts[0]
                    author = parts[1]
                    year = int(parts[2])
                    
                    ratings_str = parts[3]
                    if ratings_str:
                        ratings = [int(r) for r in ratings_str.split(',')]
                    else:
                        ratings = []
                    
                    for rating in ratings:
                        if not 1 <= rating <= 5:
                            raise ValueError(f"Некорректная оценка: {rating}")
                    
                    self.add_book(name, author, year, ratings)
                    
                except Exception as e:
                    print(f"Ошибка при обработке строки '{line}': {e}")
                    continue
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл '{filename}' не найден")
        except Exception as e:
            raise Exception(f"Ошибка при импорте из CSV: {e}")
