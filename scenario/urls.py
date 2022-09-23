from django.urls import path
from rest_framework import routers

from .views import ScenarioViewSet

router = routers.DefaultRouter()
router.register(r"scenarios", ScenarioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r"<str:usuarioid>/scenarios/", ScenarioViewSet.as_view({"get": "list"})),
    path(
        r"<str:usuarioid>/scenarios/<str:scenarioname>",
        ScenarioViewSet.as_view({"get": "get_formats_from_scenario"}),
    ),
]
