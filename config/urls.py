from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from folk.views import (
    displayHome,
    displayLesson,
    displayPractice,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', displayHome, name='home'),
    path('lesson/<int:pk>', displayLesson, name='displayLesson'),
    path('practice/<int:pk>', displayPractice, name='displayPractice'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)