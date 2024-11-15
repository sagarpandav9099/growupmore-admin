from django.views.generic import TemplateView

class CountryView(TemplateView):
    template_name = 'master/country.html'