from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    TransliteratorView, MorphAnalyserView, StemView, LemmatizeView,
    PosTaggingView, SyllablesView, CountSyllablesView, GenreClassificationView
)

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Документация API для морфологического анализа",
        terms_of_service="",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('translit/', TransliteratorView.as_view(), name='translit-api'),
    path('stem/', StemView.as_view(), name='stem-api'),
    path('lemmatize/', LemmatizeView.as_view(), name='lemmatize-api'),
    path('uzmorphanalyser/', MorphAnalyserView.as_view(), name='uzmorphanalyser-api'),
    path('postagging/', PosTaggingView.as_view(), name='uztagger-api'),
    path('syllables/', SyllablesView.as_view(), name='syllables-api'),
    path('count/', CountSyllablesView.as_view(), name='count-api'),
    path('genre-classification/', GenreClassificationView.as_view(), name='genre-classification-api'),

    # Swagger UI
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
