import sqlite3


class DatabaseManager:
    """
    Менеджер для работы с базой данных SQLite.
    Использует контекстный менеджер для безопасного открытия и закрытия соединения.
    """

    def __init__(self, db_path: str):
#        print("Создан объект DatabaseManager")
        """
        Инициализация менеджера базой данных.

        Args:
            db_path: Путь к файлу базы данных.
        """
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Открывает соединение с базой данных и создает курсор.
        Возвращает экземпляр класса для использования в блоке 'with'.
        """
#        print("Подключение к базе...")
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
#        print("Подключение успешно.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрывает соединение с базой данных.
        Если произошла ошибка, выполняется откат изменений (rollback).
        Иначе изменения сохраняются (commit).
        """
        if exc_type:
            print("Ошибка. Выполняется откат изменений.")
            self.connection.rollback()
        else:
#            print("Сохранение изменений.")
            self.connection.commit()
        
        self.connection.close()
#        print("Соединение закрыто.")

    def execute(self, sql: str, params=()):
        """
        Выполняет SQL-запрос с необязательными параметрами.

        Args:
            sql: SQL-запрос для выполнения.
            params: Кортеж параметров для подстановки в запрос.
        """
#        print(f"Выполняется SQL: {sql}")
        self.cursor.execute(sql, params)

    def select_all(self, sql: str, params=()):
        """
        Выполняет SELECT-запрос и возвращает найденные записи.
        """

#        print(f"Выполняется SQL: {sql}")

        self.cursor.execute(sql, params)

        return self.cursor.fetchall()
