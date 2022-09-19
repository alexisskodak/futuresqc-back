from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .repository import ProductTableRepository


class FsqcDataViewSet(viewsets.ViewSet):
    @action(detail=True, methods=["post"])
    def get_data_table_last_record(self, request, pk=None):
        repository = ProductTableRepository()
        data = repository.get_table_last_record(
            query_values=(
                pk,
                request.data.get("idproducto"),
                request.data.get("idmaquina"),
                request.data.get("idestacion"),
            ),
        )
        return Response(data, status=status.HTTP_200_OK)
