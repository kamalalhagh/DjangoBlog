from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Profile(TemplateView):
    template_name = 'registration/profile.html'
