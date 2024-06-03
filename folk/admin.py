from django.contrib import admin

from folk.models import (
    Lesson,
    Useful,
    Parsing,
    Image,
    Practice,
    Comment,
    CommentUseful,
)

admin.site.register(Lesson)
admin.site.register(Useful)
admin.site.register(Parsing)
admin.site.register(Image)
admin.site.register(Practice)
admin.site.register(Comment)
admin.site.register(CommentUseful)