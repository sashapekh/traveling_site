from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.main_site),
    url(r'^about/', views.about),
    url(r'tours/', views.tours),
    url(r'contact/', views.contact),
    url(r'testpage/', views.testpage),
    url(r'lab4/', views.lab4),
    url(r'mysql_test', views.mysql_view),
    url(r'test_page/', views.test_page),
    url(r'form/', views.form),
    url(r'table/', views.table_show)

]
