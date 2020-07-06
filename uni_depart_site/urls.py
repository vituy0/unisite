from django.contrib import admin
from django.urls import path, include, re_path
from uni_depart_site import urls
from uni_depart_site.views import *
app_name = 'uni_depart_site'

urlpatterns = [
    
#    path('search/', )
    path('list/', TestList.as_view(), name='info_list'),
    path('detail/<int:pk>/', UniInfoView.as_view(), name='uni_list'),
    path('department/detail/<int:pk>/', DepartDetail.as_view(), name='depart_detail'),
    path('search/', Search.as_view(), name='search'),
    
]
