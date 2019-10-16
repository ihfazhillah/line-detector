from django.urls import path
from . import views


app_name = "images"
urlpatterns = [
    path("list/", view=views.image_list_view, name="list"),
]
