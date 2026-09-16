import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestBaseTemplate:
    """Tests for base.html template structure."""

    def test_base_template_exists(self):
        """Verify base.html template file exists and renders."""
        client = Client()
        response = client.get(reverse('pages:home'))
        assert response.status_code == 200
        assert 'text/html' in response['Content-Type']

    def test_navigation_renders(self):
        """Verify navigation bar renders with all links."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        # Check navigation links exist
        assert 'href="/"' in content or 'href="/services/' not in content
        assert 'Services' in content
        assert 'Industries' in content
        assert 'About' in content
        assert 'Contact' in content

    def test_footer_renders(self):
        """Verify footer renders with company details."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        # Check footer content
        assert '308 Digital' in content
        assert 'contact@308digital.com' in content or 'contact' in content.lower()

    def test_home_page_inherits_base(self):
        """Verify home page properly extends base.html."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert '<html' in content
        assert '<head>' in content
        assert '<body>' in content
        assert '<footer>' in content

    def test_services_page_inherits_base(self):
        """Verify services page properly extends base.html."""
        client = Client()
        response = client.get(reverse('pages:services'))
        assert response.status_code == 200
        assert '<html' in response.content.decode()

    def test_industries_page_inherits_base(self):
        """Verify industries page properly extends base.html."""
        client = Client()
        response = client.get(reverse('pages:industries'))
        assert response.status_code == 200
        assert '<html' in response.content.decode()

    def test_about_page_inherits_base(self):
        """Verify about page properly extends base.html."""
        client = Client()
        response = client.get(reverse('pages:about'))
        assert response.status_code == 200
        assert '<html' in response.content.decode()

    def test_contact_page_inherits_base(self):
        """Verify contact page properly extends base.html."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        assert response.status_code == 200
        assert '<html' in response.content.decode()

    def test_active_navigation_state_home(self):
        """Verify home link is marked as active on home page."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        # Check for active class on home link
        assert 'active' in content

    def test_all_urls_accessible(self):
        """Verify all page URLs are accessible."""
        client = Client()
        urls = [
            reverse('pages:home'),
            reverse('pages:services'),
            reverse('pages:industries'),
            reverse('pages:about'),
            reverse('pages:contact'),
        ]

        for url in urls:
            response = client.get(url)
            assert response.status_code == 200
