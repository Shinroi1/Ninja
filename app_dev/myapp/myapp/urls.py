"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/name")
def name(request):
    return {'name': "Samuel Gimena"}

@api.get("/addition")
def add_numbers(request, a: float = 8, b: float = 8):
    result = a + b
    return {'result': result}

@api.get("/subtraction")
def subtract_numbers(request, a: float = 15, b: float = 10 ):
    result = a - b
    return {'result': result}

@api.get("/multiplication")
def multiply_numbers(request, a: float = 50, b: float = 25 ):
    result = a * b
    return {'result': result}

@api.get("/division")
def divide_numbers(request, a: float = 90, b: float = 9 ):
    result = a / b
    return {'result': result}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",api.urls)
]
