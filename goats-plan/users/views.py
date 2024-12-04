from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView

from users.forms import RegisterForm


# Create your views here.

class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        return render(request, self.template_name, {'form': form})


# Override the default LoginView in order to redirect to corresponding page based on user's role
class CustomLoginView(LoginView):
    def get_redirect_url(self):
        # Default to the URL set in LOGIN_REDIRECT_URL if no role-based redirection is found
        redirect_url = super().get_redirect_url()

        if self.request.user.role == 'developer':
            return '/planner/developer/'
        elif self.request.user.role == 'project_manager':
            return '/planner/project_manager/'

        return redirect_url  # Fallback to default URL
