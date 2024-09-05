from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('study', 'Study'),
        ('daily', 'Daily'),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.title} | {self.author} | {self.date.strftime("%Y-%m-%d")}'
    
    def get_absolute_url(self):
        if self.category == 'daily':
            return reverse('dailyblog-article-detail', args=(str(self.id)))
        else:
            return reverse('studyblog-article-detail', args=(str(self.id)))
