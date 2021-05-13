"""Test URLs are configured consistently."""

from django import urls


def test_end_in_slash():
    """
    Test that URLs end in a slash.

    One of Django's design philosophies is to normalize URLs to a definitive version
    which end in a slash.
    https://docs.djangoproject.com/en/stable/misc/design-philosophies/#definitive-urls
    """

    def assert_url_patterns_end_in_slash(url_patterns):
        for url_pattern in url_patterns:
            str_pattern = str(url_pattern.pattern)
            assert (
                str_pattern.endswith("/")
                or str_pattern.endswith("/$")
                or "." in str_pattern
                or str_pattern in ["", "^$"]
            )

            if hasattr(url_pattern, "url_patterns"):
                assert_url_patterns_end_in_slash(url_pattern.url_patterns)

    assert_url_patterns_end_in_slash(urls.get_resolver().url_patterns)
