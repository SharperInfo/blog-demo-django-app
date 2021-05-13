"""URLs."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from blog_demo_django_app import views

urlpatterns = [
    path("in-case-of-emergency/", admin.site.urls),
    path("", views.Home.as_view(), name="home"),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
