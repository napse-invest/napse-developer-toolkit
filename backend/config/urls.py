"""URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:
--------
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
from django.conf.urls import include
from django.http import HttpResponse
from django.urls import path
from django_napse.api.api_urls import main_api_router


def health_check(request):
    return HttpResponse(status=200)


urlpatterns = [
    path("api/", include(main_api_router.urls), name="api"),
    path("health-check/", health_check),
]
