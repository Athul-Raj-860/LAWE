"""
URL configuration for LawE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name='Login'),
    path('Signup/',views.Signup,name='Signup'),
    path('Forgot_Password/',views.Forgot_Password,name="Forgot_Password"),
    path('Home/',views.Home,name='Home'),
    path('Register/',views.Register_Case,name='Register_Case'),
    path('Logout/',views.Logout,name='Logout'),
    path('Update_User/<int:id>/',views.Update_User,name='Update_User'),
    path('Lawyer/',views.Lawyer_List,name='Lawyer_List'),
    path('Register_Case/',views.Register_Case,name='Register_Case'),
    path('Emergency_Numbers/', views.EmergencyNumbers, name='Emergency_Numbers'),
    path('BookLawyer/',views.Book_Lawyer1,name='Book_Lawyer1'),
    path('BookLawyer/<int:id>/', views.Book_Lawyer2, name='Book_Lawyer2'),
    path('Basic_Laws/',views.BasicLaws,name='Basic_Laws'),
    path('Payment/<int:Book_Id>/',views.Payment,name='Payment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
