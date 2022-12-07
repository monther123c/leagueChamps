from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import champ
# Create your views here.

class champListView(ListView):
    template_name='champ/champ_list.html'
    model = champ

class champDetailView(DetailView):
    template_name="champ/champ_detail.html"
    model= champ

class champCreateView(CreateView):
    template_name="champ/champ_create.html"
    model= champ
    fields=['champ', 'champ_type', 'owner','description','img_url']

class champUpdateView(UpdateView):
    template_name="champ/champ_update.html"
    model= champ
    fields=['champ', 'champ_type', 'owner','description','img_url']

class champDeleteView(DeleteView):
    template_name='champ/champ_delete.html'
    model= champ
    success_url=reverse_lazy('champ_list')
