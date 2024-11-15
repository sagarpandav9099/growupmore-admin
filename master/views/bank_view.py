from django.views.generic import TemplateView

class BankView(TemplateView):
    template_name = 'master/bank.html'