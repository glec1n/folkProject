from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from folk.views import (
    displayHome,
    displayLesson,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', displayHome, name='home'),
    path('lesson/<int:pk>', displayLesson, name='displayLesson')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)