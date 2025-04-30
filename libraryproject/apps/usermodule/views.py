from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib import messages

from django.contrib.auth import logout

# Create your views here.


def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})



class CustomLoginView(LoginView):
    template_name = 'usermodule/login.html'
    next_page = reverse_lazy('list_students') 

def logout_view(request):
    logout(request)
    return redirect('login')