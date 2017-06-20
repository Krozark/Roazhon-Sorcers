from django.shortcuts import render
from django.views.generic import TemplateView

from website.models import Article


class HomeView(TemplateView):
    template_name = "website/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['last_article'] = Article.objects.all()[0]
        context['articles_list'] = Article.objects.all()[1:10]
        return context
