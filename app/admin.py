from django.contrib.admin import site
from .models import *

site.register(ScoreList)
site.register(RegistrationPhase)
site.register(UserData)
site.register(Faculty)
site.register(Prodi)
site.register(Registration)
