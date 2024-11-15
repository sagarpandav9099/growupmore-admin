from django.views.generic import TemplateView

class EmployeeBankView(TemplateView):
    template_name = 'hr/employee_bank.html'