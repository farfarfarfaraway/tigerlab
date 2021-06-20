from django.contrib.auth.views import LoginView
from django.http import request
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import resolve_url
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from claims.models import Claim
from django.shortcuts import render,HttpResponse
from django.views.generic.base import RedirectView, TemplateView
from claims.form.applicationForm import ApplicationForm
from claims.form.LoginForm import LoginForm

# Create your views here.
class Applications(TemplateView):
    template_name = 'applications/add_application.html'
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        form = ApplicationForm()
        claim = Claim.objects.all()  
        context = {'claim':claim,'form':form}      
        return context

    def post(self,request):
        if request.method == "POST":
            form = ApplicationForm(request.POST or None)
            if form.is_valid():
                form.save()
                return render(request,'applications/list_of_applications.html',{'claim':Claim.objects.all()})
        return render(request,'applications/add_application.html',{'form':form})




class showApplications(TemplateView):
    template_name = 'applications/list_of_applications.html'
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)
        form = ApplicationForm()
        claim = Claim.objects.all()  
        context = {'claim':claim,'form':form}      
        return context


class approveApplication(RedirectView):
    url =  '/showapplications'

    def get_redirect_url(self, *args, **kwargs):
        id = kwargs['id']
        claim = Claim.objects.get(id=id)
        claim.approve = 1
        claim.save()
        return super().get_redirect_url(*args, **kwargs)



class rejectApplication(RedirectView):
    url =  '/showapplications'

    def get_redirect_url(self, *args, **kwargs):
        id = kwargs['id']
        claim = Claim.objects.get(id=id)
        claim.approve = 2
        claim.save()
        return super().get_redirect_url(*args, **kwargs)




# User login view
class UserLoginView(LoginView):
    authentication_form = LoginForm
    form_class = LoginForm
    redirect_authenticated_user = False
    template_name = 'login.html'
    

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('/showapplications')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(UserLoginView, self).form_valid(form)


class userApplications(TemplateView):
    template_name = 'applications/list_of_applications.html'
    def get_context_data(self, *args,**kwargs):
        form = ApplicationForm()
        context = super().get_context_data(**kwargs)
        claim = Claim.objects.all()
        context = {'claim':claim,'form':form}
        


        try:
            request.user.username in User
            context = {'claim':claim,'form':form}      
            return context
        except:
            return context        

    def post(self,request):
        if request.method == "POST":
            form = ApplicationForm(request.POST or None)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("start-project"))


class editApplications(View):

    def get (self,request,id):
        claim = Claim.objects.get(id=id)
        form = ApplicationForm(instance = claim)
        claim.save()
        return render(request,'applications/add_application.html',{'form':form})

    def post (self,request,id):
        if request.method == "POST":
            claim = Claim.objects.get(id = id)
            form = ApplicationForm(request.POST,instance=claim)
            if form.is_valid():
                form.save()
                return render(request,'applications/list_of_applications.html',{'claim':Claim.objects.all()})
        return HttpResponse("Errors")    
#Logout view
def LogoutView(request):
    logout(request)
    return redirect("/claim-admin")
    


