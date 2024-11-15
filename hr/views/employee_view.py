from django.views.generic import TemplateView

class EmployeeView(TemplateView):
    template_name = 'hr/employee.html'