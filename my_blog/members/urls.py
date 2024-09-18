from django.urls import path
from .views import PasswordsChangeView, UserRegisterView, update_profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),

    # required logged in
    path('edit_profile/', update_profile, name='update_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_pwd.html'), name='password_change'),

]
