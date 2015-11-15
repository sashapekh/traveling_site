# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from lab4.Print_file import result
from django_tables2 import RequestConfig
# Create your views here.


def main_site(request):
    return render(request, 'main.html', {})


def about(request):
    return render(request, 'about.html', {})


def tours(request):
    return render(request, 'tour.html')


def contact(request):
    return render(request, 'contact.html', {})

def testpage(request):
    return render(request, 'testpage.html')


def lab4(request):
    result_dict = result()

    date = result_dict['date']
    text = result_dict['text']
    time = result_dict['time']

    return render(request, 'lab4_test.html', {'result_dict': result_dict, 'text': text, 'time': time, 'date': date})


def mysql_view(request):
    return render(request, 'mysql_test.html', {})


def test_page(request):
    res = result()
    text = res['text']
    return render(request, 'test_page.html', {'text': text})


def form(request):
    return render(request, 'forms.html')


def table_show(request):
    return render(request, 'table.html')