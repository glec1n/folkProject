from django.shortcuts import render

def displayHome(request):
    return render(request, 'home.html')
