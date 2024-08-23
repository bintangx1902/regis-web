from django.forms import *
from .models import *


class InputScoreForm(ModelForm):
    class Meta:
        model = ScoreList
        fields = ['ipa_score', 'mtk_score', 'bind_score', 'bing_score']

    ipa_score = FloatField(widget=NumberInput(attrs={'max': 100, 'placeholder': 0.0}))
    mtk_score = FloatField(widget=NumberInput(attrs={'max': 100, 'placeholder': 0.0}))
    bind_score = FloatField(widget=NumberInput(attrs={'max': 100, 'placeholder': 0.0}))
    bing_score = FloatField(widget=NumberInput(attrs={'max': 100, 'placeholder': 0.0}))
