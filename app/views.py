from django.shortcuts import render
from django.views.generic import *
from app.models import *
from django.urls import reverse_lazy
# Create your views here.

class Home(TemplateView):
    template_name='app/home.html'

class List(ListView):
    model=School
    context_object_name='schools'

class Detail(DetailView):
    model=School
    context_object_name='sc'

class Create(CreateView):
    model=School
    fields='__all__'

class Update(UpdateView):
    model=School
    fields='__all__'

class Delete(DeleteView):
    model=School
    context_object_name='sc'
    success_url=reverse_lazy('list')