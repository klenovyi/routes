from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from .models import Route

class RouteListView(ListView):
    model = Route
    template_name = 'route_list.html'

class RouteDetailView(DetailView):
    model = Route
    template_name = 'route_detail.html'

class CreateRouteView(CreateView):
    model = Route
    fields = ['date', 'collector_group', 'atms']
    template_name = 'create_route.html'