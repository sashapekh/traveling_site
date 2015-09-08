# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from lab4.Print_file import result
from .models import Products, Customer, Order
from tables import ProductTable, OrderTable , CustomerTable
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


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['ВАШ_EMAIL_ДЛЯ_ПОЛУЧЕНИЯ_СООБЩЕНИЯ']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'form.html')

    else:  # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'form.html', {'form': form})  # создание модели формы


from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)


def testpage(request):
    return render(request, 'testpage.html')


def lab4(request):
    result_dict = result()

    date = result_dict['date']
    text = result_dict['text']
    time = result_dict['time']

    return render(request, 'lab4_test.html', {'result_dict': result_dict, 'text': text, 'time': time, 'date': date})


def mysql_view(request):
    Customer_table = CustomerTable(Customer.objects.all())
    RequestConfig(request).configure(Customer_table)

    Order_table = OrderTable(Order.objects.all())
    RequestConfig(request).configure(Order_table)

    Product_table = ProductTable(Products.objects.all())
    RequestConfig(request).configure(Product_table)

    return render(request, 'mysql_test.html', {'Customer_table': Customer_table,
                                               'Order_table': Order_table,
                                               'Product_table': Product_table})