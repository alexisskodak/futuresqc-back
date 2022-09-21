import environ
import pyodbc

from typing import Callable
env = environ.Env()


class DataTableRepository:
    def __init__(self):
        connection_str = (
            "DRIVER={driver};SERVER={host};DATABASE={name};UID={user};PWD={password}".format(
                driver="ODBC Driver 17 for SQL Server",
                host=env.str("DATA_DATABASE_HOST"),
                name=env.str("DATA_DATABASE_NAME"),
                user=env.str("DATA_DATABASE_USER"),
                password=env.str("DATA_DATABASE_PASSWORD"),
            )
        )
        self.connection = pyodbc.connect(connection_str)
        self.cursor = self.connection.cursor()

    def _close_connection(self):
        self.cursor.close()
        del self.cursor
        self.connection.close()

    def _run_fetch_all_procedure(self, procedure: str, param_str: str, values: tuple, handle_results: Callable):
        try:
            self.cursor.execute(f"Exec [dbo].[{procedure}] {param_str}", values)

        except Exception as exception:
            print(f"Error: {exception}")

        finally:
            self._close_connection()
