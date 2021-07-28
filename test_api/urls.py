from django.contrib import admin
from django.urls import path
from test_api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
]
