from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from website.models import Article


class HomeView(TemplateView):
    template_name = "website/home.html"

    def get_context_data(self, **kwargs):
        # top bar
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_article'] = Article.objects.all()[0]
        context['articles_list'] = Article.objects.all()[1:10]
        return context

class ArticleDetailView(DetailView):
    template_name = "website/article.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context
