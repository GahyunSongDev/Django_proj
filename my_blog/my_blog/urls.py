from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('the_blog.urls')),
    path('members/', include('django.contrib.auth.urls')), # django uses authentication package for memeber's urls page
    path('members/', include('members.urls')),
    path('members/logout/', LogoutView.as_view(), name='logout'),
]