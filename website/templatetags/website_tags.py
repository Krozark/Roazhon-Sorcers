from django import template
from django.template import Library
import urllib, hashlib,json
from django.contrib.sites.models import Site
from datetime import datetime, timedelta

from website.models import Event

register = Library()
######################### GRAVATAR ############################
class GravatarUrlNode(template.Node):
    def __init__(self, email):
        self.email = template.Variable(email)
 
    def render(self, context):
        try:
            email = self.email.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        host = Site.objects.get_current().name
 
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode("UTF-8")).hexdigest() + "?"
        gravatar_url += urllib.parse.urlencode({'s':"60"})
 
        return gravatar_url
 
@register.tag
def gravatar_url(parser, token):
    try:
        tag_name, email = token.split_contents()
 
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
 
    return GravatarUrlNode(email)

class GravatarProfileNode(template.Node):
    def __init__(self, email):
        self.email = template.Variable(email)
 
    def render(self, context):
        try:
            email = self.email.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        try :
            profile_url = "http://www.gravatar.com/" + hashlib.md5(email.lower().encode("UTF-8")).hexdigest() + ".json"
            r = urllib.request.urlopen(profile_url)
            data = r.read().decode("UTF-8")

            data = json.loads(data)["entry"][0]
            r.close()
            context["gravatar_data"] = data
        except:
            context["gravatar_data"] = None
 
        return ""
 
@register.tag
def gravatar_profile(parser, token):
    try:
        tag_name, email = token.split_contents()
 
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
 
    return GravatarProfileNode(email)


class GetEventsNode(template.Node):
    def __init__(self, parser, context_name):
        self.template_parser = parser
        self.context_name = context_name

    def render(self, context):
        context[self.context_name] = Event.objects.filter(date=None) | Event.objects.filter(date__gte= datetime.now() - timedelta(days=7))[:4]
        return ""
        
@register.tag
def GetEvents(parser, token):

    tokens = token.split_contents()
    fnctl = tokens.pop(0)

    def error():
        raise TemplateSyntaxError("GetEvents accepts the syntax: {%% GetEvents as context_name %%}")

    while True:
        if len(tokens) < 2:
            error()
        token = tokens.pop(0)
        if token == "as":
            break
    if len(tokens) != 1:
        error()
    context_name = tokens.pop()
    return GetEventsNode(parser, context_name)
