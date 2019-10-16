from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Image

# Create your views here.


class ImageListView(ListView):
    model = Image
    template_name = "images/list.html"


image_list_view = ImageListView.as_view()


class ImageDetailView(DetailView):
    model = Image
    template_name = "images/detail.html"


image_detail_view = ImageDetailView.as_view()


class ImageCreateView(CreateView):
    model = Image
    template_name = "images/create.html"
    fields = "__all__"


image_create_view = ImageCreateView.as_view()
