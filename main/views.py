from django.shortcuts import render


def index(request):
    return render(request, 'main.html')


def translit(request):
    return render(request, 'translit.html')


def uztagger(request):
    return render(request, 'uztagger.html')


def stem(request):
    return render(request, 'stem.html')


def lemmatize(request):
    return render(request, 'lemmatize.html')


def uzmorphanalyser(request):
    return render(request, 'uzmorphanalyser.html')


def syllables(request):
    return render(request, 'syllables.html')


def linebreak(request):
    return render(request, 'linebreak.html')


def count(request):
    return render(request, 'count.html')


def genre_classification(request):
    return render(request, 'genre_classification.html')


def news(request):
    return render(request, 'news.html')
