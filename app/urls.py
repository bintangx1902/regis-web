from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('input-nilai', InputScoreView.as_view(), name='score-input'),
    path('registration/<slug>', RegistrationPhaseView.as_view(), name='registration-phase'),
    path('reset-password', ForgotPasswordView.as_view(), name='reset-password'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('profile/create', CreateProfileView.as_view(), name='profile-create'),
    path('profile/update/<slug>', UpdateProfileView.as_view(), name='profile-update')
]
