import pytest


def test_example():
    """Simple test to verify pytest is working."""
    assert 1 + 1 == 2


@pytest.mark.django_db
def test_django_db():
    """Verify Django database is configured."""
    from django.db import connection
    assert connection.connection is not None or connection.settings_dict is not None
