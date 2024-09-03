from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from babel.dates import format_datetime
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

gender_list = [
    ('p', 'Pria'),
    ('w', 'Wanita')
]

religion_list = [
    ('i', 'Islam'),
    ('kk', 'Kristen Katolik'),
    ('pp', 'Kristen Protestan'),
    ('b', 'Buddha'),
    ('k', 'Konghucu')
]


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='data', related_query_name='data')
    date_of_birth = models.DateField('Tanggal Lahir : ', auto_now=False, auto_now_add=False,
                                     auto_created=False)
    place_of_birth = models.CharField('Tempat Lahir : ', max_length=150)
    gender = models.CharField('Jenis Kelamin : ', choices=gender_list, max_length=2)
    religion = models.CharField('Agama : ', choices=religion_list, max_length=2)
    unique_code = models.SlugField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Data Lengkap {self.user.first_name} {self.user.last_name}"


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


class RegistrationPhase(models.Model):
    name = models.CharField(_('Nama Gelombang : '), max_length=255)
    open_on = models.DateTimeField(_('Tanggal Buka Gelombang : '), auto_now=False, auto_created=False,
                                   auto_now_add=False)
    closed_on = models.DateTimeField(_('Tanggal Penutupan Gelombang : '), auto_now=False, auto_created=False,
                                     auto_now_add=False)
    slug = models.SlugField(max_length=20, null=True, blank=True, default='')

    def __str__(self):
        return f"{self.name}, buka pada {self.time_stamp(self.open_on)}, tutup pada {self.time_stamp(self.closed_on)}"

    def time_stamp(self, data):
        formatted_date = format_datetime(data, format='EEEE d MMMM yyyy', locale='id_ID')
        formatted_time = format_datetime(data, format='hh:mm a', locale='id_ID').upper()
        return f"{formatted_date} Jam {formatted_time}"

    def closed_on_(self):
        return f"{self.time_stamp(self.closed_on)}"

    def open_on_(self):
        return f"{self.time_stamp(self.open_on)}"

    def generate_slug(self, name):
        slug = slugify(name)
        return slug[:self._meta.get_field('slug').max_length]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug(self.name)
        super().save(*args, **kwargs)


class Faculty(models.Model):
    name = models.CharField(_('Nama Fakultas '), max_length=100)

    def __str__(self):
        return self.name


class Prodi(models.Model):
    name = models.CharField(_('Nama Prodi '), max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name=_('Fakultas '))

    def __str__(self):
        return f"{self.name} - {self.faculty}"


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prodi = models.ForeignKey(Prodi, on_delete=models.CASCADE)
    phase = models.ForeignKey(RegistrationPhase, on_delete=models.CASCADE)
    address = models.TextField(_('Alamat Domisil '))

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} mendaftar pada" \
               f" gelombang {self.phase.name}, dengan prodi {self.prodi}"
