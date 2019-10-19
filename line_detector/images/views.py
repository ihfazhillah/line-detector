from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    success_url = reverse_lazy("images:list")


image_create_view = ImageCreateView.as_view()


class ImageProcessViewGet(DetailView):
    model = Image
    template_name = "images/process-image.html"


image_process_view_get = ImageProcessViewGet.as_view()


@api_view(["POST"])
def image_process_view_post(request, *args, **kwargs):
    return Response({})
