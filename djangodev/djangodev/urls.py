"""djangodev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import *
from django.views.generic.base import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redirect/', data_flair),
    path('dataflair/', index),
    #path('djangotutor/', tutorial.as_view())
    path('djangotutor/', RedirectView.as_view(url = 'https://data-flair.training/blogs/category/django/')),
    path('inf2', inf2),
    path('inf1', inf1),
    # mine test
    path('detail/<int:question_id>/', detail, name='detail'), # in browser http://localhost:8000/detail/[angka]/
    path('setcookie', setcookie),
    path('getcookie', showcookie),
    path('deleteco', delete_cookie), # instead of this, use this path path('deleteco/', delete_cookie)
]
