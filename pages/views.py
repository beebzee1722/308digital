import json
import re
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class ServicesView(TemplateView):
    template_name = 'pages/services.html'


class IndustriesView(TemplateView):
    template_name = 'pages/industries.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


@require_http_methods(['POST'])
def contact_submit(request):
    """Handle contact form submission via AJAX."""
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        # Validation
        errors = {}
        if not name:
            errors['name'] = 'Name is required'
        if not email:
            errors['email'] = 'Email is required'
        elif not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
            errors['email'] = 'Please enter a valid email address'
        if not message:
            errors['message'] = 'Message is required'

        if errors:
            return JsonResponse({
                'status': 'error',
                'message': 'Validation failed',
                'errors': errors
            }, status=400)

        # Send email
        subject = f'New Contact Form Submission from {name}'
        body = f'From: {name}\nEmail: {email}\n\nMessage:\n{message}'

        try:
            send_mail(
                subject,
                body,
                email,
                ['contact@308digital.com'],
                fail_silently=False,
            )
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': 'Failed to send email. Please try again later.'
            }, status=500)

        return JsonResponse({
            'status': 'success',
            'message': 'Thank you for reaching out! We\'ll get back to you soon.'
        })

    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid request format'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'An error occurred. Please try again.'
        }, status=500)
