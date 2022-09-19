from rest_framework import mixins, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from user.models import User
from user.serializers import SmallUserSerializer, UserSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.order_by("usuarioid").all()

    def get_serializer_class(self):
        if self.action == "list":
            return SmallUserSerializer
        return UserSerializer

    @permission_classes([AllowAny])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @permission_classes([IsAuthenticated])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
