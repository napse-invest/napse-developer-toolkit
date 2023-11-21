"""URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples
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
from django.urls import path
from django_napse.api.api_urls import main_api_router

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response


# @api_view(["GET"])
# @permission_classes([])
# def health(request):
#     """Health check."""
#     return Response(status=200, data={"status": "ok"})


urlpatterns = [
    # path("health/", health, name="health"),
    path("api/", include(main_api_router.urls), name="api"),
]
