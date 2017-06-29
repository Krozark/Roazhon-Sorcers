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
        object_list = context["object_list"]
        context['last_object'] = None
        context['object_list'] = []
        if object_list.count() > 0:
            context['last_object'] = object_list[0]

        if object_list.count() > 1:
            context['object_list'] = object_list[1:]

        context["number_per_row"] = math.ceil((object_list.count() -1) / 3)
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        category = self.request.GET.get("category", None)
        if category:
            queryset = queryset.filter(M2M_category__slug=category)
        return queryset


class ArticleDetailView(DetailView):
    template_name = "website/article.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context

