from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserForm, ProfileForm
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UserRegisterView(CreateView):
    model      = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url   = reverse_lazy('post:list')

class UserLoginView(LoginView):
    template_name   = 'user/login.html'

class UserLogoutView(LogoutView):
    template_name   = 'user/logout.html'

class UserProfileView(LoginRequiredMixin, TemplateView):
    # login_url           = reverse_lazy('user:login')
    # redirect_field_name = reverse_lazy('user:profile')
    user_form_class     = UserForm
    profile_form_class  = ProfileForm 
    template_name       = 'user/profile.html'

    def post(self, request):
        user_form       = self.user_form_class(request.POST, instance=request.user)
        profile_form    = self.profile_form_class(request.POST, request.FILES, instance=request.user.profile)

        context         = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        if user_form.is_valid():
            self.form_save(user_form)
        if profile_form.is_valid():
            self.form_save(profile_form)

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        return obj

    def get(self, request, *args, **kwargs):
        user_form = self.user_form_class(instance=request.user)
        profile_form = self.profile_form_class(instance=request.user.profile)

        context = self.get_context_data(user_form=user_form,profile_form=profile_form)

        return self.render_to_response(context)
