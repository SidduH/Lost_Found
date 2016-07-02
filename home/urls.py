from django.conf.urls import url

from . import views
app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),  # Default path
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'(?P<user_id>[0-9]+)', views.detail, name='detail'),
]
