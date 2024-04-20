from django.shortcuts import render
from .models import Lesson, Useful, Parsing, Image, Practice

def displayHome(request):
    lessons = Lesson.objects.all()
    practices = Practice.objects.all()
    usefuls = Useful.objects.all()
    parsings = Parsing.objects.all()

    context = {'lessons': lessons, 'usefuls': usefuls, 'practices': practices, 'parsings': parsings}
    return render(request, 'home.html', context)

def displayLesson(request, pk):
    lessons = Lesson.objects.all()
    lesson = Lesson.objects.get(id=pk)
    images = Image.objects.all()

    context = {'lessons': lessons, 'lesson': lesson, 'images': images}
    return render(request, 'lesson.html', context)

def displayPractice(request, pk):
    lessons = Lesson.objects.all()
    practice = Practice.objects.get(id=pk)
    images = Image.objects.all()

    context = {'practice': practice, 'lessons': lessons, 'images': images}
    return render(request, 'practice.html', context)