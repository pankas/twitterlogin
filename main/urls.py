from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r"^", views.home, name="home"),
    url(r'^users/', include('login.urls')),
    # url(r'^users/', include('django.contrib.auth.urls')), #remove this when using allauth

]