from audioop import reverse
from dataclasses import field
from pyexpat.errors import messages
from re import template
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from cities.models import City
from django.views.generic.detail import DetailView
from .forms import HtmlForm, CityForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin


__all__ = (
    'home',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
    'CityListView',
    

    
)

def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid(): 
            print(form.cleaned_data)
            form.save()
    # if pk:
    #     city = get_object_or_404(City, id=pk)
    #     context = {'object': city}
    #     return render(request, 'cities/detail.html', context)
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 7)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
    

class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно создан"
    
    
class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно отредактирован"
    
    
class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
    
    def get(self, request, *args, **kwargs):
        # messages.success(request, 'Город успешно удален')
        return self.post(request, *args, **kwargs)
    
    
class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = 'cities/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = City.objects.all()
        context["form"] = form
        return context
    