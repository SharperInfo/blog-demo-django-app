"""Globally available test fixtures."""

from django.test.utils import override_settings

import pytest


@pytest.fixture(scope="session", autouse=True)
def set_settings():
    """Global settings for all tests."""

    with override_settings(
        # Important test settings.
        DEBUG=False,
        PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"],
        # CELERY_BROKER="memory://",
        WHITENOISE_AUTOREFRESH=True,
        SECURE_SSL_REDIRECT=True,
        CACHES={
            "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}
        },
        # Settings to override configuration in developer environments.
        CSP_REPORT_ONLY=False,
        # AWS_ACCESS_KEY_ID=None,
        # AWS_SECRET_ACCESS_KEY=None,
    ):
        yield
