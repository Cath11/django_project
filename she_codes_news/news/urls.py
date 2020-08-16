from django.urls import path
from . import views
# from .views import AuthorsView
# from .views import AuthorProfileView


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('authors/', views.AuthorsView.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorProfileView.as_view(), name='authorProfile'),
    
]
