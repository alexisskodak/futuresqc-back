from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from scenario.models import Scenario
from scenario.serializers import ScenarioSerializer
from user.models import User


class Unauthorized(APIException):
    status_code = 401
    default_detail = "Unauthorized, verify credentials"
    default_code = "unauthorized"


class ScenarioViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("usuarioid", None)
        if user_id is None:
            raise Unauthorized()

        try:
            user = User.objects.get(usuarioid=user_id)
            return self.queryset.filter(idusuario=user.usuarioid)
        except User.DoesNotExist:
            raise NotFound(f"scenario with user id {user_id} does not exist")

    @action(detail=True, methods=["get"])
    def get_formats_from_scenario(self, request, *args, **kwargs):
        sql = "RTRIM(nombreEscenario) = %s"
        queryset = self.get_queryset().extra(
            where=[sql],
            params=(kwargs.get("scenarioname"),),
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
