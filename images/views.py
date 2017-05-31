from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, ListView
from .forms import ImageCreateForm
from .models import Image


class ImageCreateView(CreateView):
    template_name = 'images/create.html'
    form_class = ImageCreateForm

    def form_valid(self, form):
        image = form.save(commit=False)
        image.user = self.request.user
        image.save()
        return redirect(image.get_absolute_url())

    def get_form_kwargs(self):
        kwargs = super(ImageCreateView, self).get_form_kwargs()
        if self.request.method == 'GET':
            kwargs.update({
                'data': self.request.GET})
        return kwargs


class ImageDetailView(DetailView):
    template_name = 'images/detail.html'
    model = Image
    pk_url_kwarg = 'pk'


class ImageListView(ListView):
    template_name = 'images/list.html'
    model = Image
