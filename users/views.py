from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import CreateUserForm
from folk.models import Lesson

def registerPage(request):
    lessons = Lesson.objects.all()
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Произошла ошибка. Проверьте верность введенных данных.')

    return render(request, 'register.html', {'form': form, 'lessons': lessons})

def loginPage(request):
    lessons = Lesson.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверный логин или пароль')
    
    context = {'lessons': lessons}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')
