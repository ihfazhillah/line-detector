from django.shortcuts import render
from django.views.generic import ListView

from .models import Image

# Create your views here.


class ImageListView(ListView):
    model = Image
    template_name = "images/list.html"


image_list_view = ImageListView.as_view()
