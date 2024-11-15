from django.views.generic import TemplateView

class FaqCategoryView(TemplateView):
    template_name = 'master/faq_category.html'