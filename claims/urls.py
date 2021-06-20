"""RMSsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from claims.views import Applications,approveApplication,rejectApplication,showApplications,UserLoginView, LogoutView,userApplications,editApplications
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', Applications.as_view(),name="start-project"),
    path('claim-admin', UserLoginView.as_view(),name="start-project"),
    path('logout', LogoutView,name="start-project"),
    path('showapplications', showApplications.as_view(),name="start-project"),
    path('userapplications', userApplications.as_view(),name="start-project"), 
    path('addapplications', Applications.as_view(),name="Add-application"),
    path('approve/<int:id>',approveApplication.as_view(),name="Approve-Application"),
    path('reject/<int:id>',rejectApplication.as_view(),name="reject-Application"),
    path('edit/<int:id>',editApplications.as_view(),name="edit-Application"),
    

]
