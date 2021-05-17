from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
) 
from django.urls import reverse_lazy 
from .models import Article, Comment
from .forms import CommentForm




class ArticleListView(
    ListView
):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(
    DetailView
): 
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self): 
        +360.12 
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView
): 
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(
    LoginRequiredMixin, CreateView
): 
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'


    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)


