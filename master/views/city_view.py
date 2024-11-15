from django.views.generic import TemplateView

class CityView(TemplateView):
    template_name = 'master/city.html'