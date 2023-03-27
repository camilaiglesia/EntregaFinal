"""Tercera_pre_entrega_Iglesia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from Tercera_pre_entrega_Iglesia import settings
from account.views import login_account


urlpatterns = [
    path('', login_account, name= "accountLogin"),
    path('admin/', admin.site.urls),
    path('coder/', include('AppCoder.urls')),  #incluyo las urls de la aplicacion
    path('account/', include('account.urls'))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
