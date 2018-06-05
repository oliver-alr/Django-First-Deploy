from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'polls/home.html')

def about(request):
    return render(request, 'polls/about.html')

def news(request):
    return render(request, 'polls/news.html')

def register(request):
    return render(request, 'polls/register.html')

def base(request):
    return render(request, 'polls/base.html')
