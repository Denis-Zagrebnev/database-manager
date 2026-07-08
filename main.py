from database import DatabaseManager


def insert_movie(movie):
    """Добавление фильма в базу."""

    with DatabaseManager("base.db") as db:
        db.execute("""
            INSERT INTO movies
            (title, year, genre, duration, origin, director, rating, rating_count, imdb_link)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            movie["title"],
            movie["year"],
            movie["genre"],
            movie["duration"],
            movie["origin"],
            movie["director"],
            movie["rating"],
            movie["rating_count"],
            movie["imdb_link"]
        ))


def count_movies():
    """Показать количество фильмов."""

    with DatabaseManager("base.db") as db:
        result = db.select_all("SELECT COUNT(*) FROM movies")

    print(f"\nФильмов в базе: {result[0][0]}")


def search_by_genre():
    """Поиск фильмов по жанру."""

    genre = input("Введите жанр: ")

    with DatabaseManager("base.db") as db:
        movies = db.select_all(
            "SELECT title, year FROM movies WHERE genre LIKE ?",
            (f"%{genre}%",)
        )

    for movie in movies:
        print(movie)


def search_by_title():
    """Поиск фильма по слову в названии."""

    word = input("Введите слово: ")

    with DatabaseManager("base.db") as db:
        movies = db.select_all(
            "SELECT title, year FROM movies WHERE title LIKE ?",
            (f"%{word}%",)
        )

    if movies:
        for movie in movies:
            print(movie)
    else:
        print(f'По фразе "{word}" ничего не найдено.')


def top5():
    """Топ-5 фильмов по рейтингу."""

    with DatabaseManager("base.db") as db:
        movies = db.select_all("""
            SELECT title, rating
            FROM movies
            ORDER BY rating DESC
            LIMIT 5
        """)

    for movie in movies:
        print(movie)


def delete_before_year():
    """Удаление фильмов старше указанного года."""

    year = int(input("Удалить фильмы старше какого года? "))

    with DatabaseManager("base.db") as db:
        db.execute(
            "DELETE FROM movies WHERE year < ?",
            (year,)
        )

    print("Удаление выполнено.")


def main():

    while True:

        print("\n===== МЕНЮ =====")
        print("1. Добавить фильм")
        print("2. Поиск по жанру")
        print("3. Удалить фильмы старше года")
        print("4. Показать количество фильмов")
        print("5. Топ-5 фильмов по рейтингу")
        print("6. Поиск фильма по слову в названии")
        print("0. Выход")

        choice = input("\nВыберите пункт: ")

        if choice == "1":

            movie = {
                "title": input("Название: "),
                "year": int(input("Год: ")),
                "genre": input("Жанр: "),
                "duration": input("Длительность: "),
                "origin": input("Страна: "),
                "director": input("Режиссёр: "),
                "rating": float(input("Рейтинг: ")),
                "rating_count": int(input("Количество голосов: ")),
                "imdb_link": input("Ссылка: ")
            }

            insert_movie(movie)
            print("Фильм добавлен.")

        elif choice == "2":
            search_by_genre()

        elif choice == "3":
            delete_before_year()

        elif choice == "4":
            count_movies()

        elif choice == "5":
            top5()

        elif choice == "6":
            search_by_title()

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()