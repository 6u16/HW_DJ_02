import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator  # это наш разбивальщик контента постранично


def index(request):
    return redirect(reverse('bus_stations'))

CONTENT = []

with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        CONTENT.append(row)


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_num = int(request.GET.get('page', 1))  # будем запрашивать нужную нам страницу через параметр в запросе, ('page', 1) - 1 страница если параметр не указали
    
    paginator = Paginator(CONTENT, 10)  # (CONTENT, 10) - список элементов и 10 - столько будет элементов на странице
    
    page = paginator.get_page(page_num)
    
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)




def pagi(request):
    page_num = int(request.GET.get('page', 1))  # будем запрашивать нужную нам страницу через параметр в запросе, ('page', 1) - 1 страница если параметр не указали
    
    paginator = Paginator(CONTENT, 10)  # (CONTENT, 10) - список элементов и 10 - столько будет элементов на странице
    
    page = paginator.get_page(page_num)  # запросим http://127.0.0.1:8000/pagi/?page=7 седьмую страницу
    
    context = {
        'page': page
    }  # это словарь с параметрами для вывода в браузер(для доступа в шаблоне)
    
    return render(request, 'pagi.html', context) 