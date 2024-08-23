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


class ResetPasswordForm(Form):
    email = EmailField(label='Email', max_length=255)
    new_password = CharField(
        label='New Password',
        widget=PasswordInput(attrs={
            'placholder': "New Password",
            'required': 'required',
            'pattern': r'(?=.*[A-Z])(?=.*[^\w\s]).{8,}',
            'title': 'Password must be at least 8 characters long, include at least one uppercase letter and one '
                     'punctuation mark.',
        })
    )
    confirm_password = CharField(
        label='Confirm Password',
        widget=PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'required': 'required',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        # Check if new password and confirmation match
        if new_password and confirm_password and new_password != confirm_password:
            self.add_error('confirm_password', "The new passwords do not match.")

        # Check if email exists
        email = cleaned_data.get("email")
        if email and not User.objects.filter(email=email).exists():
            self.add_error('email', "No user with this email exists.")

        return cleaned_data

