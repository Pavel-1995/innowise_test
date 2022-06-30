"""innowise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include

from rest_framework import routers

from support.views import *  # TicketApiView,

router = routers.DefaultRouter()
router.register(r"ticket", TicketViewSet)

router_2 = routers.SimpleRouter()
router_2.register(r"message", MessageViewSet)


urlpatterns = [
    # Instead of page not foud
    path("", index),

    path("admin/", admin.site.urls),

    # JWTAuthentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Tickets and messages apps
    path("api/", include(router.urls), name="list"),
    path("api/", include(router_2.urls)),
]









]
