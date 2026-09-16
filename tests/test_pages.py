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


@pytest.mark.django_db
class TestHomePage:
    """Tests for home page content and sections."""

    def test_home_page_hero_section(self):
        """Verify hero section renders with headline and subheading."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert 'Transform Your Business with AI' in content
        assert 'Enterprise-grade AI solutions' in content

    def test_home_page_services_teaser(self):
        """Verify 'What we do' section shows 3 services."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert 'What We Do' in content
        assert 'AI Strategy & Consulting' in content
        assert 'Intelligent Automation' in content
        assert 'Data Analytics & Business Intelligence' in content
        # Count that service teasers link to services page
        assert content.count('href="/services/"') >= 3

    def test_home_page_industries_teaser(self):
        """Verify industries teaser section is present."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert 'Industries We Serve' in content
        assert 'Financial Services' in content
        assert 'Insurance' in content
        assert 'Healthcare' in content
        assert 'href="/industries/"' in content

    def test_home_page_why_choose_us(self):
        """Verify why-choose-us section displays value propositions."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert 'Why Choose 308 Digital' in content
        assert 'Expertise in AI & Automation' in content
        assert 'Proven Track Record' in content
        assert 'Custom Solutions' in content
        assert 'End-to-End Support' in content
        assert 'Ongoing Partnership' in content

    def test_home_page_closing_cta(self):
        """Verify closing CTA section is present."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert 'Ready to Transform Your Business' in content
        assert 'Get in Touch' in content
        assert 'href="/contact/"' in content

    def test_home_page_links_to_services(self):
        """Verify home page links to services page."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert 'href="/services/"' in content

    def test_home_page_links_to_industries(self):
        """Verify home page links to industries page."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert 'href="/industries/"' in content

    def test_home_page_links_to_contact(self):
        """Verify home page links to contact page."""
        client = Client()
        response = client.get(reverse('pages:home'))
        content = response.content.decode()

        assert 'href="/contact/"' in content

@pytest.mark.django_db
class TestServicesPage:
    """Tests for services page content."""

    def test_services_page_header(self):
        """Verify services page header is present."""
        client = Client()
        response = client.get(reverse('pages:services'))
        content = response.content.decode()
        
        assert 'Our Services' in content
        assert 'Comprehensive AI and automation solutions' in content

    def test_all_six_services_displayed(self):
        """Verify all 6 services are displayed on the page."""
        client = Client()
        response = client.get(reverse('pages:services'))
        content = response.content.decode()
        
        services = [
            'AI Strategy & Consulting',
            'Intelligent Automation',
            'Data Analytics & Business Intelligence',
            'Finance & Insurance Solutions',
            'Custom AI Solutions',
            'Digital Transformation Services',
        ]
        
        for service in services:
            assert service in content, f"Service '{service}' not found on page"

    def test_services_have_descriptions(self):
        """Verify each service has a description."""
        client = Client()
        response = client.get(reverse('pages:services'))
        content_lower = response.content.decode().lower()

        # Check for detailed descriptions
        assert 'comprehensive ai strategy' in content_lower
        assert 'intelligent automation' in content_lower
        assert 'advanced analytics' in content_lower
        assert 'fraud detection' in content_lower
        assert 'bespoke ai' in content_lower
        assert 'digital transformation' in content_lower

    def test_services_page_responsive(self):
        """Verify services page renders valid HTML."""
        client = Client()
        response = client.get(reverse('pages:services'))
        content = response.content.decode()
        
        # Check for responsive grid structure
        assert 'services-grid' in content
        assert '<h3>' in content


@pytest.mark.django_db
class TestIndustriesPage:
    """Tests for industries page content."""

    def test_industries_page_header(self):
        """Verify industries page header is present."""
        client = Client()
        response = client.get(reverse('pages:industries'))
        content = response.content.decode()
        
        assert 'Industries We Serve' in content
        assert 'AI solutions tailored' in content

    def test_all_five_industries_displayed(self):
        """Verify all 5 industries are displayed on the page."""
        client = Client()
        response = client.get(reverse('pages:industries'))
        content = response.content.decode()
        
        industries = [
            'Financial Services',
            'Insurance',
            'Healthcare',
            'Retail & E-commerce',
            'Public Sector & Enterprise',
        ]
        
        for industry in industries:
            assert industry in content, f"Industry '{industry}' not found on page"

    def test_industries_have_descriptions(self):
        """Verify each industry has a description."""
        client = Client()
        response = client.get(reverse('pages:industries'))
        content_lower = response.content.decode().lower()
        
        # Check for industry-specific descriptions
        assert 'financial' in content_lower
        assert 'insurance' in content_lower
        assert 'healthcare' in content_lower
        assert 'retail' in content_lower or 'e-commerce' in content_lower
        assert 'public sector' in content_lower or 'enterprise' in content_lower

    def test_industries_page_responsive(self):
        """Verify industries page renders valid HTML."""
        client = Client()
        response = client.get(reverse('pages:industries'))
        content = response.content.decode()
        
        # Check for responsive grid structure
        assert 'industries-grid' in content
        assert '<h3>' in content


@pytest.mark.django_db
class TestAboutPage:
    """Tests for about page content."""

    def test_about_page_has_mission(self):
        """Verify mission statement section is present."""
        client = Client()
        response = client.get(reverse('pages:about'))
        content = response.content.decode()
        
        assert 'Our Mission' in content
        assert 'empower organizations' in content.lower()

    def test_about_page_has_vision(self):
        """Verify vision statement section is present."""
        client = Client()
        response = client.get(reverse('pages:about'))
        content = response.content.decode()
        
        assert 'Our Vision' in content
        assert 'trusted leader' in content.lower()

    def test_about_page_has_all_five_value_props(self):
        """Verify all 5 value propositions are displayed."""
        client = Client()
        response = client.get(reverse('pages:about'))
        content = response.content.decode()
        
        value_props = [
            'Expertise in AI & Automation',
            'Proven Track Record',
            'Custom Solutions',
            'End-to-End Support',
            'Ongoing Partnership',
        ]
        
        for prop in value_props:
            assert prop in content, f"Value prop '{prop}' not found on page"

    def test_value_props_have_descriptions(self):
        """Verify each value proposition has a description."""
        client = Client()
        response = client.get(reverse('pages:about'))
        content_lower = response.content.decode().lower()
        
        # Check for key descriptive phrases
        assert 'deep knowledge' in content_lower
        assert 'enterprise clients' in content_lower
        assert 'tailor' in content_lower
        assert 'strategy' in content_lower
        assert 'partnership' in content_lower

    def test_about_page_structure(self):
        """Verify about page has proper structure."""
        client = Client()
        response = client.get(reverse('pages:about'))
        content = response.content.decode()
        
        # Check sections are present
        assert '<h2>' in content
        assert 'Why Choose 308 Digital' in content


@pytest.mark.django_db
class TestContactPage:
    """Tests for contact page structure and form."""

    def test_contact_page_has_form(self):
        """Verify contact page has a form element."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert '<form' in content
        assert 'id="contact-form"' in content

    def test_contact_form_has_name_field(self):
        """Verify form has name input field."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert 'name="name"' in content
        assert 'type="text"' in content or 'id="name"' in content

    def test_contact_form_has_email_field(self):
        """Verify form has email input field."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert 'name="email"' in content
        assert 'type="email"' in content or 'id="email"' in content

    def test_contact_form_has_message_field(self):
        """Verify form has message textarea field."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert 'name="message"' in content
        assert '<textarea' in content

    def test_contact_form_has_submit_button(self):
        """Verify form has submit button."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert 'type="submit"' in content or 'submit' in content.lower()

    def test_contact_page_has_success_placeholder(self):
        """Verify page has success message placeholder."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert 'id="success-message"' in content
        assert 'success-message' in content.lower()

    def test_contact_page_has_error_placeholder(self):
        """Verify page has error message placeholder."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert 'id="error-message"' in content
        assert 'error-message' in content.lower()

    def test_contact_page_has_company_details(self):
        """Verify page displays company contact details."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert 'contact@308digital.com' in content
        assert 'Phone' in content or '(555)' in content

    def test_contact_page_structure(self):
        """Verify contact page renders valid HTML."""
        client = Client()
        response = client.get(reverse('pages:contact'))
        content = response.content.decode()
        
        assert '<html' in content
        assert '<form' in content
        assert 'Get In Touch' in content
