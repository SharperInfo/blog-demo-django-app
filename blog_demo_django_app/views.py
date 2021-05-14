"""Views"""

from django import urls
from django.contrib import messages
from django.views.generic import FormView, RedirectView

from blog_demo_django_app import forms


class HomeView(RedirectView):
    url = "order-meal"


class OrderMealView(FormView):
    """Order meal view."""

    template_name = "blog_demo_django_app/order-meal.html"
    form_class = forms.OrderMealForm
    success_url = urls.reverse_lazy("order-meal")

    def form_valid(self, form):
        """Process a valid form."""

        # If HTMX, just render the form.
        if "HTTP_HX_REQUEST" in self.request.META:
            return self.render_to_response(self.get_context_data(form=form))

        messages.success(self.request, "Order successfully placed!")
        return super().form_valid(form)
