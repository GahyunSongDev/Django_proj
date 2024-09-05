from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('the_blog.urls')),
    path('members/', include('django.contrib.auth.urls')), # django uses authentication package for memeber's urls page
    path('members/', include('members.urls')),
]
