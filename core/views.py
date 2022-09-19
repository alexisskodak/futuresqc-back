from rest_framework import exceptions, response, status, views

from user.models import User


class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password")

        try:
            user = User.objects.get(usuarioid=username)
        except User.DoesNotExist as not_found:
            raise exceptions.AuthenticationFailed("User not found") from not_found
        else:
            if not user.check_password(password):
                raise exceptions.AuthenticationFailed("Incorrect password")

            return response.Response({"message": "success"}, status=status.HTTP_202_ACCEPTED)
