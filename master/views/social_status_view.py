from django.views.generic import TemplateView

class SocialStatusView(TemplateView):
    template_name = 'master/social_status.html'