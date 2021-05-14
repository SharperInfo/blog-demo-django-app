"""URLs."""

from django.conf import settings
from django.urls import include, path

from blog_demo_django_app import views

urlpatterns = [
    path("order-meal/", views.OrderMealView.as_view(), name="order-meal"),
    path("", views.HomeView.as_view(), name="home"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
