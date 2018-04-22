from datetime import datetime

from django.shortcuts import render
from django.template.context import RequestContext
from django.views.generic import TemplateView, DetailView, ListView
from django.core.mail import send_mail
from django.contrib.auth.models import User

from website.models import ArticleCategory, Article, Event
from website.forms import ContactForm

class ArticleListView(ListView):
    template_name = "website/home.html"
    model = Article
    paginate_by = 5

    def get_queryset(self):
        category = self.request.GET.get("category", None)
        return self.model.get_queryset(category)


class ArticleDetailView(DetailView):
    template_name = "website/article.html"
    model = Article

    #def get_context_data(self, **kwargs):
    #    context = super(ArticleDetailView, self).get_context_data(**kwargs)
    #    return context

    #def get_queryset(self):
    #    now = datetime.now()
    #    queryset = self.model.objects.filter(publishing_date__lte=now)
    #    return queryset

def contactView(request):
    form = None
    sent = False
    if request.method == 'POST':
        form = ContactForm (request.POST)

        if form.is_valid():
            honeypot = form.cleaned_data['honeypot']
            if not honeypot:
                subject = "[Roazhon Sorcers website] " + form.cleaned_data['subject']
                email_from = form.cleaned_data['email_from']
                message = form.cleaned_data['message']
                cc_myself = form.cleaned_data['cc_myself']

                email_to = [User.objects.get(username="admin").email,]

                if cc_myself :
                    email_to.append(email_from)

                send_mail(subject, message, email_from, email_to, fail_silently=False)

            form = ContactForm()
            sent = True

    else:
        form = ContactForm()


    return render(request, "website/contact.html", {
            "form" : form,
            "sent" : sent,
        }, content_type='text/html')
