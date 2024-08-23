from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class ScoreList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_query_name='score', related_name='score')
    ipa_score = models.FloatField(verbose_name='Nilai IPA', default=.0,
                                  validators=[MinValueValidator(.0), MaxValueValidator(100.)])
    mtk_score = models.FloatField(verbose_name='Nilai Matematika', default=.0,
                                  validators=[MinValueValidator(.0), MaxValueValidator(100.)])
    bind_score = models.FloatField(verbose_name='Nilai Bahasa Indonesia', default=.0,
                                   validators=[MinValueValidator(.0), MaxValueValidator(100.)])
    bing_score = models.FloatField(verbose_name='Nilai Bahasa Inggris', default=.0,
                                   validators=[MinValueValidator(.0), MaxValueValidator(100.)])
    is_pass = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - IPA: {self.ipa_score}, MTK: {self.mtk_score}, B.Indo: {self.bind_score}, " \
               f"B.Ing: {self.bing_score}"

    def average_score(self):
        scores = [self.ipa_score, self.mtk_score, self.bind_score, self.bing_score]
        valid_scores = [score for score in scores if score is not None]
        if valid_scores:
            return sum(valid_scores) / len(valid_scores)
        return None
