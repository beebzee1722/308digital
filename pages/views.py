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
