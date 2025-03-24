from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('translit/', translit, name='translit'),
    path('uztagger/', uztagger, name='uztagger'),
    path('stem/', stem, name='stem'),
    path('lemmatize/', lemmatize, name='lemmatize'),
    path('uzmorphanalyser/', uzmorphanalyser, name='uzmorphanalyser'),
    path('syllables/', syllables, name='syllables'),
    path('linebreak/', linebreak, name='linebreak'),
    path('count/', count, name='count'),
    path('genre-classification/', genre_classification, name='genre-classification'),
    path('news/', news, name='news'),
]
