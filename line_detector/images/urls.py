from django.urls import path
from . import views


app_name = "images"
urlpatterns = [
    path("list/", view=views.image_list_view, name="list"),
    path("create/", view=views.image_create_view, name="create"),
    path("<pk>/", view=views.image_detail_view, name="detail"),
]
