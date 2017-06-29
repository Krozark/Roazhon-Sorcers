import math
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from website.models import ArticleCategory, Article


class ArticleListView(ListView):
    template_name = "website/home.html"
    model = Article
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # top bar
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['last_object'] = context["object_list"][0]
        context['object_list'] = context["object_list"][1:]
        context["number_per_row"] = math.ceil(context["object_list"].count() / 3)
        return context

class ArticleDetailView(DetailView):
    template_name = "website/article.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context

