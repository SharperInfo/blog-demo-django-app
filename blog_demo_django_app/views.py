"""Views"""

from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "blog_demo_django_app/home.html"
