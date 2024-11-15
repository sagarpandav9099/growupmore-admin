# master's url.py

from django.urls import path
from .views import campaign_type_view, country_view, state_view, city_view,bank_view, department_view, designation_view, social_status_view, faq_category_view
from .views import communication_type_view, event_type_view, marketing_type_view, offer_type_view, promotion_type_view,ticket_type_view                      

urlpatterns = [
    path('countries/', country_view.CountryView.as_view(), name='country'),
    path('states/', state_view.StateView.as_view(), name='state'),
    path('cities/', city_view.CityView.as_view(), name='city'),
    path('banks/', bank_view.BankView.as_view(), name='bank'),
    path('departments/', department_view.DepartmentView.as_view(), name='department'),
    path('designations/', designation_view.DesignationView.as_view(), name='designation'),
    path('social_status/', social_status_view.SocialStatusView.as_view(), name='social_status'),
    path('faq_categories/', faq_category_view.FaqCategoryView.as_view(), name='faq_category'),
    path('campaign_types/', campaign_type_view.CampaignTypeView.as_view(), name='campaign-type'),
    path('communication_types/', communication_type_view.CommunicationTypeView.as_view(), name='communication-type'),
    path('event_types/', event_type_view.EventTypeView.as_view(), name='event-type'),
    path('marketing_types/', marketing_type_view.MarketingTypeView.as_view(), name='marketing-type'),
    path('offer_types/', offer_type_view.OfferTypeView.as_view(), name='offer-type'),
    path('promotion_types/', promotion_type_view.PromotionTypeView.as_view(), name='promotion-type'),
    path('ticket_types/', ticket_type_view.TicketTypeView.as_view(), name='ticket-type'),
    
]



