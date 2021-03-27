from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path('',views.home, name="Home"),
    path('contact/',views.contact, name='contact'),
    path('about/' ,views.about, name='about'),
    path('terms/',views.terms , name="terms"),
    path('desclimer/',views.desclimer , name='desc'),
    path('police/',views.police , name='privacy'),
    path(r'^ads\.txt$', views.authorized_digital_sellers_view, name='authorized_digital_sellers'),

]