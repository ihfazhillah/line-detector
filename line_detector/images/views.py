from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Image
from line_detector.detector import line_detector

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
    fields = ["title", "image", "scale"]
    success_url = reverse_lazy("images:list")

    def form_valid(self, form):
        form.options = []
        return super().form_valid(form)


image_create_view = ImageCreateView.as_view()


class ImageProcessViewGet(DetailView):
    model = Image
    template_name = "images/process-image.html"


image_process_view_get = ImageProcessViewGet.as_view()


@api_view(["POST"])
def image_process_view_post(request, pk, *args, **kwargs):
    image = get_object_or_404(Image, pk=pk)
    detected = line_detector(image.image.path)
    return Response(detected)
