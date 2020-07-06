"""unisite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from uni_depart_site import urls
from unisite.views import SiteMain, MainDepartStatus, Button_Event, Tableau
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SiteMain.as_view(), name='main'),
    path('university/', include('uni_depart_site.urls')),
    path('depart/', MainDepartStatus.as_view(), name="depart_status"), 
    path('api/button_event/', Button_Event.as_view(), name="button_event"),
    path('tableau/',Tableau.as_view(), name="tableau"),

]
