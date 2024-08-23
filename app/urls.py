from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('input-nilai', InputScoreView.as_view(), name='score-input'),

    path('reset-password', ForgotPasswordView.as_view(), name='reset-password'),
]