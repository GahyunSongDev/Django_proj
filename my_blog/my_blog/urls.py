from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('the_blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('members/logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)