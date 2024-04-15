from django.contrib import admin
from django.urls import path

from folk.views import (
    displayHome,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', displayHome, name='home'),
]
