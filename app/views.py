from django.shortcuts import render, redirect
from .utils import *
from django.views.generic import *
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings


class LandingPageView(TemplateView):
    template_name = get_template('landing_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['score'] = ScoreList.objects.filter(user=self.request.user)
        return context

    @method_decorator(login_required(login_url=settings.LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class InputScoreView(View):
    def get(self, *args, **kwargs):
        form = InputScoreForm()
        context = {
            'form': form
        }
        return render(self.request, get_template('input_nilai'), context=context)

    def post(self, *args, **kwargs):
        form = InputScoreForm(self.request.POST)
        if form.is_valid():
            is_pass = is_pass_check(form.cleaned_data)

            # Save the form data
            score_list = form.save(commit=False)
            score_list.user = self.request.user
            score_list.is_pass = is_pass
            score_list.save()

            return redirect('some_success_url')

        context = {
            'form': form
        }
        return render(self.request, 'input_nilai.html', context)
