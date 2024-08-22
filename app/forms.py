from django.forms import Form, ModelForm
from .models import *


class InputScoreForm(ModelForm):
    class Meta:
        model = ScoreList
        fields = ['ipa_score', 'mtk_score', 'bind_score', 'bing_score']
