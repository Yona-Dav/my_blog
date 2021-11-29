from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import MyAuthentificationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = MyAuthentificationForm


@login_required
def test_page(request):
    return render(request, 'accounts/test.html')

