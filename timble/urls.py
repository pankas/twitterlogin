"""timble URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from main import views
from login import views as views1
# from allauth.account.views import confirm_email, login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^home', include('main.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^', views.home, name='home'),
    # url(r'^users/', include('login.urls')),
    # url(r'^accounts/', include('allauth.urls')),
    # url(r'^logout/$', logout, name='account_logout'),
    # url(r'^signup/$', login, name='account_signup'),
    # url(r'^signup/', views1.SignUp.as_view(), name='signup'),
    # url(r'^login/', include('login.urls')),
    
]
