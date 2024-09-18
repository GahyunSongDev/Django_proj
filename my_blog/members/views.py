from django.shortcuts import redirect, render

from django.urls import reverse_lazy
from .forms import CustomUserCreationForm 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileUpdateForm
from django.views.generic.edit import CreateView


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm  
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change') 

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your password has been updated successfully.')
        return response
    