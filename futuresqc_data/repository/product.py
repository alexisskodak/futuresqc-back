from .base import BaseDataTableRepository


class ProductTableRepository(BaseDataTableRepository):
    def get_table_last_record(self, query_values):
        procedure_name = "getUltimoRegistroTabla"
        query_params_as_string = (
            ", ".join(
                [
                    "@tabla = ?",
                    "@producto = ?",
                    "@maquina = ?",
                    "@estacion = ?",
                ]
            ),
        )
        return self._run_stored_procedure(procedure_name, query_params_as_string, query_values)
