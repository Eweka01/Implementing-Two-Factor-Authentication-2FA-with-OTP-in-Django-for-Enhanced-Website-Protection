from django.contrib import admin
from django.urls import path

# Comment out or remove the OTPAdminSite override temporarily
# admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
]
