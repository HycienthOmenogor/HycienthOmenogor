from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import(ListView, DetailView)
from .models import Sold

# Create a login url so you are directed to it
class LockedView(LoginRequiredMixin):
    login_url = "admin:login"

# Creates a view of list of products sold 
class SoldListView(ListView):
    model = Sold
    queryset = Sold.objects.all()

# Creates a detailed information of products sold
class SoldDetailView(LockedView, DetailView):
    #class SoldDetailView(DetailView):
    model = Sold
