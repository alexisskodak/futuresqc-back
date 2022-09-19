from rest_framework import mixins, viewsets
from rest_framework.exceptions import APIException, NotFound
from rest_framework.permissions import IsAuthenticated

from scenario.models import Scenario
from scenario.serializers import ScenarioSerializer
from user.models import User


class Unauthorized(APIException):
    status_code = 401
    default_detail = "Unauthorized, verify credentials"
    default_code = "unauthorized"


class ScenarioViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = ScenarioSerializer
    queryset = Scenario.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get("usuarioid", None)
        if not user_id:
            raise Unauthorized()

        try:
            user = User.objects.get(usuarioid=user_id)
        except User.DoesNotExist as does_not_exist:
            raise NotFound(
                f"scenario with user id {user_id} does not exist"
            ) from does_not_exist
        else:
            return self.queryset.filter(idusuario=user.usuarioid)
