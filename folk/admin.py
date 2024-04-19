from django.contrib import admin

from folk.models import (
    Lesson,
    Useful,
    Parsing,
    Image,
)

admin.site.register(Lesson)
admin.site.register(Useful)
admin.site.register(Parsing)
admin.site.register(Image)