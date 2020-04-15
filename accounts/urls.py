from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url('login', views.login, name='login'),
    url('logout', views.logout, name='logout'),
]