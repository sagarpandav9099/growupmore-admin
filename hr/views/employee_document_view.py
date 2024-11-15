from django.views.generic import TemplateView

class EmployeeDocumentView(TemplateView):
    template_name = 'hr/employee_document.html'