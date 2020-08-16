from django.urls import path
from .views import CreateAccountView, ProfileView
from . import views

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name = 'createAccount'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/update/<int:pk>', views.AccountUpdateView.as_view(), name='accountUpdate'),
    
]



