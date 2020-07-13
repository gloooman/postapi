from django.urls import path, include

from .v1 import routers

app_name = 'blog-api'

urlpatterns = [
    path('v1/', include(routers)),
]


