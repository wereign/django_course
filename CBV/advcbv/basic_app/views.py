from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView,DetailView, 
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")