import sqlite3
import csv


def main():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year INTEGER,
            genre TEXT,
            duration TEXT,
            origin TEXT,
            director TEXT,
            rating REAL,
            rating_count INTEGER,
            imdb_link TEXT
        )
    """)

    with open("imdb_top_250.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # пропускаем заголовок
        rows = []
        for row in reader:
            rows.append((
                row[1],
                int(row[2]),
                row[3],
                row[4],
                row[5],
                row[6],
                float(row[7]),
                int(row[8]),
                row[9]
             ))

    cursor.executemany(
        """
        INSERT INTO movies (title, year, genre, duration, origin, director, rating, rating_count, imdb_link)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )

    conn.commit()
    print(f"Добавлено фильмов: {cursor.rowcount}")

    conn.close()


if __name__ == "__main__":
    main()
