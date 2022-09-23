import environ
import pyodbc

env = environ.Env()


class DataTableRepository:
    _procedure_strategies = {"getUltimoRegistroTabla": "FETCH"}

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
        self.connection = pyodbc.connect(connection_str, autocommit=True)
        self.cursor = self.connection.cursor()

    def _close_connection(self):
        self.cursor.close()
        del self.cursor
        self.connection.close()

    def run_procedure(self, procedure: str, param_str: str, values: tuple):
        try:
            for row in self.cursor.execute(f"Exec [dbo].[{procedure}] {param_str}", values):
                yield row

        except Exception as exception:
            print(f"Error: {exception}")

        finally:
            self._close_connection()
