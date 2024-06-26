"""
URL configuration for CRM_3 project.

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
from django.urls import path, re_path
from stark.service.stark import site
from django.conf.urls import include
from web.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login.login),
    path('logout/', login.logout),
    path('image/code/', login.image_code),
    re_path(r'^stark/', site.urls),
    path('rbac/', include(('rbac.urls', 'rbac'), namespace='rbac')),
]
