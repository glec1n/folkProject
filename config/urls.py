from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from folk.views import (
    displayHome,
    displayLesson,
    displayPractice,
    deleteComment,
    displayUseful,
)

from users.views import (
    registerPage,
    loginPage,
    logoutUser
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', displayHome, name='home'),
    path('lesson/<int:pk>', displayLesson, name='displayLesson'),
    path('practice/<int:pk>', displayPractice, name='displayPractice'),
    path('useful/<int:pk>', displayUseful, name='displayUseful'),
    path('register', registerPage, name='register'),
    path('login', loginPage, name='login'),
    path('logout', logoutUser, name='logout'),
    path('delete-comment/<int:pk>', deleteComment, name='delete-comment' )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)