from django.shortcuts import render

# Create your views here.


def main_site(request):
    return render(request, 'main.html', {})


def about(request):
    return render(request, 'about.html', {})