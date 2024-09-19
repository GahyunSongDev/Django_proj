from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max
from django.utils import timezone
from ckeditor.fields import RichTextField

class BlogPostManager(models.Manager):
    def get_next_id(self):
        max_id = self.aggregate(Max('id'))['id__max']
        return max_id + 1 if max_id is not None else 1

    def get_reusable_id(self):
        # Get all IDs that are not currently in use
        used_ids = set(self.values_list('id', flat=True))
        max_id = self.aggregate(Max('id'))['id__max'] or 0 
        all_ids = set(range(1, max_id + 2))
        available_ids = list(all_ids - used_ids)
        if available_ids:
            return min(available_ids)
        else:
            return max_id + 1

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('study', 'Study'),
        ('daily', 'Daily'),
    ]

    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    objects = BlogPostManager()

    def __str__(self):

        return f'{self.title} | {self.author} | {self.post_date}'
        # return f'{self.title} | {self.author} | {self.date.strftime("%Y-%m-%d")}'

    def get_absolute_url(self):
        if self.category == 'daily':
            return reverse('dailyblog-article-detail', args=(str(self.id)))
        else:
            return reverse('studyblog-article-detail', args=(str(self.id)))
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only set ID if not already set (i.e., for new objects)
            self.pk = BlogPost.objects.get_reusable_id()
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)