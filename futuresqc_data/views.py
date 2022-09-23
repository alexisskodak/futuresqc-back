from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .repository import ProductTableRepository
from .serializers import FsqcTableLastRecordInputSerializer, FsqcTableLastRecourdOutputSerializer


class FsqcDataViewSet(generics.GenericAPIView, viewsets.ViewSet):
    def get_serializer_class(self):
        if self.action == "get_last_record":
            return FsqcTableLastRecourdOutputSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        request_body=FsqcTableLastRecordInputSerializer,
        responses={200: FsqcTableLastRecourdOutputSerializer()},
    )
    def get_last_record(self, request):
        repository = ProductTableRepository()
        data = repository.get_table_last_record(values=tuple(request.data.values()))
        serializer = self.get_serializer(data=data)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
