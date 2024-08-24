from django.shortcuts import render, redirect
from .utils import *
from django.views.generic import *
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import update_session_auth_hash


class LandingPageView(TemplateView):
    template_name = get_template('landing_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['score'] = ScoreList.objects.filter(user=self.request.user)
        context['phases'] = RegistrationPhase.objects.all()
        return context

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class InputScoreView(View):
    def get(self, request):
        data = ScoreList.objects.filter(user=self.request.user).first()
        form = InputScoreForm(instance=data) if data else InputScoreForm()
        context = {
            'form': form
        }
        return render(self.request, get_template('input_nilai'), context=context)

    def post(self, request):
        data = ScoreList.objects.filter(user=self.request.user).first()
        form = InputScoreForm(self.request.POST, instance=data)
        if form.is_valid():
            is_pass = is_pass_check(form.cleaned_data)
            score_list = form.save(commit=False)
            if not data:
                score_list.user = self.request.user
            score_list.is_pass = is_pass
            score_list.save()

            return redirect('app:landing')

        context = {
            'form': form
        }
        return render(self.request, get_template('input_nilai'), context)

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ForgotPasswordView(View):
    template_name = get_template('reset_password')

    def get(self, *args, **kwargs):
        form = ResetPasswordForm()

        return render(self.request, self.template_name, {'form': form})

    def post(self, *args, **kwargs):
        form = ResetPasswordForm(self.request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            new_password = form.cleaned_data.get('new_password')

            try:
                target = User.objects.get(email=email)
                target.set_password(new_password)
                target.save()

                update_session_auth_hash(self.request, target)

                return redirect(settings.RESET_PASSWORD_DONE_URL)
            except User.DoesNotExist:
                form.add_error('email', 'An unexpected error occurred.')
        return render(self.request, self.template_name, {'form': form})


class ProfileView(DetailView):
    context_object_name = 'data'
    model = UserData
    query_pk_and_slug = False
    template_name = None

    def get_queryset(self):
        return self.model.objects.get(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CreateProfileView(CreateView):
    forms = None
    template_name = None
    model = UserData
