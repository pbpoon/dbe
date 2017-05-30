from django.shortcuts import render
from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm, ProfileEditForm, UserEditForm
from .models import Profile
from django.contrib import messages


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        kwargs['section'] = 'dashboard'
        return super(DashboardView, self).get_context_data(**kwargs)


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        profile = Profile.objects.create(user=new_user)
        return render(self.request, 'account/register_done.html', {'new_user': new_user})


class EditView(LoginRequiredMixin, View):
    template_name = 'account/edit.html'

    def get(self, request):
        user_form = UserEditForm(instance=self.request.user)
        profile_form = ProfileEditForm(instance=self.request.user)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(self.request, self.template_name, context)

    def post(self, request):
        user_form = UserEditForm(instance=self.request.user, data=self.request.POST)
        profile_form = ProfileEditForm(instance=self.request.user, data=self.request.POST, files=self.request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, '成功更新资料')
        else:
            messages.error(request, '资料修改格式有误')
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(self.request, self.template_name, context)