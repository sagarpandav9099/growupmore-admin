from django.views.generic import TemplateView

class TicketTypeView(TemplateView):
    template_name = 'master/ticket_type.html'