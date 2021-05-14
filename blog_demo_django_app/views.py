"""Views"""

from django.views.generic import FormView, RedirectView

from blog_demo_django_app import forms


class HomeView(RedirectView):
    url = "order-meal"


class OrderMealView(FormView):
    template_name = "blog_demo_django_app/order-meal.html"
    form_class = forms.OrderMealForm
