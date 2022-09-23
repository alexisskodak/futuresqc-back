from django.urls import path

from .views import FsqcDataViewSet

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("data_tables", FsqcDataViewSet.as_view({"post": "get_last_record"})),
]
