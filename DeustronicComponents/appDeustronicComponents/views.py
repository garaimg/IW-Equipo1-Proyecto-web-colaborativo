from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Cliente


# Create your views here.
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'base.html', {'clientes': clientes})
