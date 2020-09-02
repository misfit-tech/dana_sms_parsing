from django.urls import path
from .views import SMSParsing


urlpatterns = [
    path('sms-parsing/', SMSParsing.as_view(), name='sms_parsing'),
]
