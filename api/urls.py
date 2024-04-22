from django.urls import path
from .views import NewsletterView,ContactView,VoluteerView

urlpatterns = [
    path('newletter/', NewsletterView.as_view()),
    path('contact/', ContactView.as_view()),
    path('voluteer/', VoluteerView.as_view()),
]