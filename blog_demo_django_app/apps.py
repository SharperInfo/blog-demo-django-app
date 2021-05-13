"""Application configuration."""

from django.apps import AppConfig


class BlogDemoDjangoAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog_demo_django_app"
