from .base import DataTableRepository


class ProductTableRepository(DataTableRepository):
    def get_table_last_record(self, values):
        procedure_name = "getUltimoRegistroTabla"
        param_list = [
            "@tabla = ?",
            "@producto = ?",
            "@maquina = ?",
            "@estacion = ?",
        ]
        params_str = ", ".join(param_list)

        last_record = {}
        for row in self.run_procedure(procedure_name, params_str, values):
            (
                table_id,
                product_id,
                machine_id,
                station_id,
                datetime,
                turn,
                operator,
                *features,
            ) = row
            last_record = {
                "table_id": table_id,
                "product_id": product_id,
                "machine_id": machine_id,
                "station_id": station_id,
                "datetime": datetime,
                "turn": turn,
                "operator": operator,
                "features": features,
            }

        return last_record
