from django.urls import path
from .views import SignUp, Profile

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', Profile.as_view(), name='profile'),
]
