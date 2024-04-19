from django.shortcuts import render
from .models import Lesson, Useful, Parsing, Image

def displayHome(request):
    lessons = Lesson.objects.all()
    usefuls = Useful.objects.all()
    parsings = Parsing.objects.all()

    context = {'lessons': lessons, 'usefuls': usefuls, 'parsings': parsings}
    return render(request, 'home.html', context)

def displayLesson(request, pk):
    lessons = Lesson.objects.all()
    lesson = Lesson.objects.get(id=pk)
    images = Image.objects.all()

    context = {'lessons': lessons, 'lesson': lesson, 'images': images}
    return render(request, 'lesson.html', context)