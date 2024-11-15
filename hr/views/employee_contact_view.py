from django.views.generic import TemplateView

class EmployeeContactView(TemplateView):
    template_name = 'hr/employee_contact.html'