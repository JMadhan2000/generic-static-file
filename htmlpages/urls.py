"""
URL configuration for htmlpages project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('madhan/',madhan,name='madhan'),
    path('madhan_name_spinning/',madhan_name_spinning,name='madhan_name_spinning'),
    path('animation/',animation,name='animation'),
    path('sematic/',sematic,name='sematic'),
    path('media/',media,name='media'),
    path('rotate/',rotate,name='rotate'),
    path('landing_pages/',landing_pages,name='landing_pages'),
    path('grid_system/',grid_system,name='grid_system'),
    path('indian_cricketres/',indian_cricketres,name='indian_cricketres'),
    path('form/',form,name='form'),
]
