import psycopg2


class DatabaseConnector:
    def __init__(self, user: str, password: str, host: str, port: str, database: str) -> None:
        self.connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
        )

    def close(self):
        self.connection.close()

    def execute(self, query: str, value: tuple):
        cursor = self.connection.cursor()
        cursor.execute(query, value)
        cursor.close()

    def execute_and_return(self, query: str, value: tuple):
        cursor = self.connection.cursor()
        cursor.execute(query, value)
        result = cursor.fetchall()
        cursor.close()
        return result
