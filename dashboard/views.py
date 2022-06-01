from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# Create your views here.
class DashboardView(TemplateView):
    template_name = "dashboard/index.html"
    title = "Dashboard"

    def get(self, request):
        return render(request, self.template_name, context={'pageTitle': self.title})

class KeplerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/kepler.html"
    title = "Kepler Dashboard"

    def get(self, request):
        return render(request, self.template_name, context={'pageTitle': self.title})

class SlideoutView(TemplateView):
    template_name = "dashboard/slideout.html"

class AppearView(TemplateView):
    template_name = "dashboard/appear.html"

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

class index(TemplateView):
    template_name = 'dashboard/login.html'
    title = "Login"
    
    def dispatch(self, request, *args, **kwargs):
        return redirect('dashboard')
        
        return super(index, self).dispatch(request, *args, **kwargs)

class logon(TemplateView):
    template_name = 'dashboard/login.html'
    title = 'LogIn Page'

    def post(self, request):
        email = self.request.POST['username']
        password= self.request.POST['password']
        user = authenticate(username= email, password= password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse('Invalid Account Details')
        else:
            print('Someone tried to log on')
            print('Email', email)
            print('Password', password)
            return render(request, self.template_name, context={'pageTitle': self.title, 'errorMessage':"Invalid Login Details"})

    def get(self, request):
        return render(request, self.template_name, context={'pageTitle': self.title, 'errorMessage':""})