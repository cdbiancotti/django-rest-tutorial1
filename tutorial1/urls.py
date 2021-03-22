
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('quickstart/', include('quickstart.urls')),
    path('tutorial1/', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
