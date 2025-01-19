from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница'
        }
    return render(request,'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def relevance(request):
    return render(request, 'main/relevance.html')

def geography(request):
    return render(request, 'main/geography.html')

def skills(request):
    return render(request, 'main/skills.html')