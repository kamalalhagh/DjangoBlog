from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.views.generic.edit import UpdateView, CreateView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class Blog(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


class Detail(DetailView):
    model = Post
    template_name = 'detail.html'


class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('blog')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class Edit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class Create(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    temp = Post
    template_name = 'comment.html'
    fields = ['post', 'comment']
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
