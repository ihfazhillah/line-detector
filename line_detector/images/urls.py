from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "images"
urlpatterns = [
    path("list/", view=views.image_list_view, name="list"),
    path("create/", view=views.image_create_view, name="create"),
    path("<pk>/", view=views.image_detail_view, name="detail"),
    path(
        "<pk>/process/",
        view=views.image_process_view_get,
        name="process-get",
    ),
]
