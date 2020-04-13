
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('search/', views.search, name='search'),
    path('export/excel/', views.export_users_xls, name='export_excel'),
    path('export/excel2/', views.export_users_xls2, name='export_excel2'),

]
