from django.urls import reverse
from django.shortcuts import redirect
from django.utils import timezone
from .models import BlogPost
from .forms import EditForm, PostForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, View
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = 'home.html'


class StudyView(ListView):
    model = BlogPost
    template_name = 'study_blog.html'
    ordering = ['-id']

class StudyDetailView(DetailView):
    model = BlogPost
    template_name = 'study_detail.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(BlogPost, pk=self.kwargs['pk'], category='study')

class DailyView(ListView):
    model = BlogPost
    template_name = 'daily_blog.html'
    ordering = ['-id']

class DailyDetailView(DetailView):
    model = BlogPost
    template_name = 'daily_detail.html'
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(BlogPost, pk=self.kwargs['pk'], category='daily')
    
class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = "add_post.html"

    def form_valid(self, form):
        # Automatically set the author to the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        # Handle redirection based on the source parameter
        source = self.request.GET.get('source', 'home')
        if source == 'daily':
            return reverse('daily-blog')
        elif source == 'study':
            return reverse('study-blog')
        else:
            return reverse('home')

class UpdatePostView(UpdateView):
    model = BlogPost
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'category', 'body']

    def form_valid(self, form):
        # Automatically set the date to now when the form is submitted
        form.instance.date = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        if post.category == 'study':
            return reverse('studyblog-article-detail', kwargs={'pk': post.pk})
        elif post.category == 'daily':
            return reverse('dailyblog-article-detail', kwargs={'pk': post.pk})
        else:
            return reverse('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = self.request.GET.get('source', 'home')
        return context
    
class DeletePostsView(View):
    def post(self, request, *args, **kwargs):
        post_ids = request.POST.getlist('posts')
        source = request.POST.get('source', 'study')
        BlogPost.objects.filter(id__in=post_ids).delete()

        if source == 'daily':
            return redirect('daily-blog')
        else:
            return redirect('study-blog')
        

class DeletePostView(View):
    def post(self, request, *args, **kwargs):
        # Get the post ID from the URL kwargs
        post_id = self.kwargs['pk']
        
        # Retrieve the post object
        post = get_object_or_404(BlogPost, pk=post_id)
        
        # Delete the post
        post.delete()
        
        # Determine the redirect URL based on the post's category or source
        source = request.POST.get('source', 'home')
        if source == 'daily':
            return redirect('daily-blog')
        elif source == 'study':
            return redirect('study-blog')
        else:
            return redirect('home')
        

class ContactsView(TemplateView):
    template_name = 'contacts.html'