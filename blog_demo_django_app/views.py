"""Views"""

from django import urls
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import FormView, RedirectView

from blog_demo_django_app import forms


class HomeView(RedirectView):
    url = "order-meal"


class HTMXFormViewMixin:
    """HTMX form view mixin."""

    htmx_template_name = None

    def is_htmx_request(self):
        return "HTTP_HX_REQUEST" in self.request.META

    def get_htmx_template_names(self):
        """Get HTMX template names."""

        if self.htmx_template_name is None:
            raise ImproperlyConfigured(
                "HTMXFormMixin requires either a definition of 'htmx_template_name' or"
                " an implementation of 'get_htmx_template_names()'"
            )

        return [self.htmx_template_name]

    def get_template_names(self):
        if self.is_htmx_request():
            return self.get_htmx_template_names()

        return super().get_template_names()

    def post(self, request, *args, **kwargs):
        """Like FormView, except render form on all HTMX requests."""

        form = self.get_form()
        if form.is_valid() and not self.is_htmx_request():
            return self.form_valid(form)

        return self.form_invalid(form)


class OrderMealView(HTMXFormViewMixin, FormView):
    """Order meal view."""

    template_name = "blog_demo_django_app/order-meal.html"
    htmx_template_name = "blog_demo_django_app/_order-meal-form-content.html"
    form_class = forms.OrderMealForm
    success_url = urls.reverse_lazy("order-meal")

    def form_valid(self, form):
        messages.success(self.request, "Order successfully placed!")
        return super().form_valid(form)
