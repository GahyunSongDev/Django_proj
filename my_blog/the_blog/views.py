from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import BlogPost
from django.shortcuts import get_object_or_404

class HomeView(TemplateView):
    template_name = 'home.html'


class StudyView(ListView):
    model = BlogPost
    template_name = 'study_blog.html'

class StudyDetailView(DetailView):
    model = BlogPost
    template_name = 'study_detail.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(BlogPost, pk=self.kwargs['pk'], category='study')

class DailyView(ListView):
    model = BlogPost
    template_name = 'daily_blog.html'

class DailyDetailView(DetailView):
    model = BlogPost
    template_name = 'daily_detail.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(BlogPost, pk=self.kwargs['pk'], category='daily')
    
class AddPostView(CreateView):
    model = BlogPost
    template_name = "add_post.html"
    fields = '__all__'