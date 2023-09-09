from django.urls import path
from .views import Home, Blog, Detail, Delete, Edit, Create, About, AddComment

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('posts/', Blog.as_view(), name='blog'),
    path('posts/detail/post_<int:pk>', Detail.as_view(), name='detail'),
    path('posts/delete/post_<int:pk>', Delete.as_view(), name='delete'),
    path('posts/edit/post_<int:pk>', Edit.as_view(), name='edit'),
    path('posts/create/post', Create.as_view(), name='create'),
    path('posts/detail/add_comment/', AddComment.as_view(), name='add_comment'),
]
