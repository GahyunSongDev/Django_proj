from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm  # Import your custom form

class UserRegisterView(generic.CreateView):
    form_class = CustomUserCreationForm  # Use the custom form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

