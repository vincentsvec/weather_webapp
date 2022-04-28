from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("city-results", views.city_results),
    path("cities/<str:city_name>", views.city_view),
    path("change-unit", views.change_unit),
    path("add-city/<str:city_id>", views.add_city),
    path("remove-city/<str:city_id>", views.remove_city),
]
