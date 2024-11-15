from django.views.generic import TemplateView

class EventTypeView(TemplateView):
    template_name = 'master/event_type.html'