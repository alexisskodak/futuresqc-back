from django.urls import path, include
from rest_framework import routers

from .views import FsqcDataViewSet

router = routers.DefaultRouter()
router.register(
    r"data_tables",
    FsqcDataViewSet,
    basename="data_tables",
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r"", include(router.urls)),
]
