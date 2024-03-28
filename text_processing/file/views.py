import re
import math

from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Table

OBJ_PAGE = 15


def index(request):
    """
    Обработка запросов
    GET: вывод шаблона для загрузки файлов
    POST: обработка текста и вывод шаблона-результата
    """
    template = 'index.html'
    if request.POST and request.FILES.getlist('files'):
        files = request.FILES.getlist('files')
        prepared_files = text_preparation(files)
        return text_processing(files=prepared_files)
    return render(request, template)


def results(request):
    """
    Постраничный вывод результатов
    """
    table = Table.objects.all().order_by('-idf')[:50]
    paginator = Paginator(table, OBJ_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
            'page_obj': page_obj,
            'table': table,
        }
    return render(request, 'result.html', context)


def text_preparation(files):
    """
    Создание словаря: имя файла - список слов
    """
    text = {}
    for f in files:
        data = f.read().decode('utf-8').lower()
        words = re.sub(r"[^\w\s]", "", data).split()
        text[f.name] = words
    return text


def text_processing(files):
    """
    Вычисление TF, IDF для каждого документа
    """
    IDF = {}
    words_set = set()
    for words in files.values():
        words_set = words_set.union(set(words))
    for w in words_set:
        r = 0
        for words in files.values():
            if w in words:
                r += 1
        IDF[w] = round(math.log10(len(files)/r), 3)
    for f, words in files.items():
        TF = {}
        for w in words:
            count = TF.get(w, 0)*len(words)
            TF[w] = round((count + 1)/len(words), 3)
        for word, tf in TF.items():
            Table.objects.create(name_file=f, word=word, tf=tf, idf=IDF[word])
    return redirect("results")


def clear(request):
    """Очистка"""
    Table.objects.all().delete()
    return redirect("/")
