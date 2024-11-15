# master's url.py

from django.urls import path
from .views import employee_view,employee_contact_view, branch_view, employee_document_view, employee_bank_view
urlpatterns = [
    path('employees/', employee_view.EmployeeView.as_view(), name='employee'),
    path('employee_contacts/', employee_contact_view.EmployeeContactView.as_view(), name='employee_contact'),
    path('employee_documents/', employee_document_view.EmployeeDocumentView.as_view(), name='employee_document'),
    path('employee_banks/', employee_bank_view.EmployeeBankView.as_view(), name='employee_bank'),
    path('branches/', branch_view.BranchView.as_view(), name='branch'),
   
]



