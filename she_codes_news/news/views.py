from django.views import generic
from .models import NewsStory
from django.urls import reverse_lazy

from .forms import StoryForm
from users.models import CustomUser
#from django.contrib.auth.mixins import get_user_model

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    def get_queryset(self):
        return NewsStory.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story' 

class AddStoryView(generic.CreateView):
    form_class=StoryForm
    context_object_name ='storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super() .form_valid(form)


class AuthorsView(generic.ListView):
    login_url= '/users/login/'
    template_name = 'news/author.html'
    model = CustomUser
    context_object_name = "authors"

class AuthorProfileView(generic.DetailView):
    login_url= '/users/login/'
    template_name = 'news/profile.html'
    model = CustomUser
    context_object_name = "author"