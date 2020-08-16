#from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name='profile'
    

class AccountUpdateView(UpdateView):
    model = CustomUser
    form_class= CustomUserChangeForm
    template_name = 'users/accountUpdate.html'
