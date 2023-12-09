from django.shortcuts import render
from django.views.generic.edit import CreateView
from .form import Create
from django.urls import reverse_lazy

class SignUp(CreateView):
    form_class = Create
    success_url = reverse_lazy('home')
    template_name = 'registration/signin.html'