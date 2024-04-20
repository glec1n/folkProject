from django.shortcuts import render, redirect
from .models import Lesson, Useful, Parsing, Image, Practice, Comment

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
    comments = lesson.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            lesson=lesson,
            body=request.POST.get('body')
        )
        return redirect('displayLesson', pk=lesson.id)

    context = {'lessons': lessons, 'lesson': lesson, 'images': images, 'comments': comments}
    return render(request, 'lesson.html', context)

def displayPractice(request, pk):
    lessons = Lesson.objects.all()
    practice = Practice.objects.get(id=pk)
    images = Image.objects.all()

    context = {'practice': practice, 'lessons': lessons, 'images': images}
    return render(request, 'practice.html', context)

def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    
    return render(request, 'delete.html', {'obj': comment})