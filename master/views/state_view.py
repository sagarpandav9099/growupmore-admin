from django.views.generic import TemplateView

class StateView(TemplateView):
    template_name = 'master/state.html'