from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.main_site),
    url(r'^about/', views.about),
    url(r'tours/', views.tours),
    url(r'contact/', views.contact),
]
