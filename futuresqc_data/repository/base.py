import environ
import pyodbc

from typing import Fu
env = environ.Env()

DB_NAME = env.str("DATA_DATABASE_NAME")
DB_HOST = env.str("DATA_DATABASE_HOST")
DB_USER = env.str("DATA_DATABASE_USER")
DB_PASSWORD = env.str("DATA_DATABASE_PASSWORD")
DB_DRIVER = "ODBC Driver 17 for SQL Server"


class BaseDataTableRepository:
    def __init__(self):
        connection_str = (
            "DRIVER={driver};SERVER={host};DATABASE={name};UID={user};PWD={password}".format(
                driver=DB_DRIVER,
                host=DB_HOST,
                name=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
            )
        )
        self.connection = pyodbc.connect(connection_str)
        self.cursor = self.connection.cursor()

    def _close_connection(self):
        self.cursor.close()
        del self.cursor
        self.connection.close()

    def _run_fetch_all_procedure(self, procedure: str, param_str: str, values: tuple, handle_results: Function):
        try:
            self.cursor.execute(f"Exec [dbo].[{procedure}] {param_str}", values)

        except Exception as exception:
            print(f"Error: {exception}")

        else:
            return results

        finally:
            self._close_connection()
