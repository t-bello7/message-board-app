from django.db import models
from django.views.generic import ListView
from .models import Posts

class HomePageView(ListView):
    model = Posts
    template_name = 'posts/home.html'
    context_object_name = 'all_posts_list'