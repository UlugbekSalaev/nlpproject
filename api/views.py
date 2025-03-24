import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UzTransliterator import UzTransliterator
from UzMorphAnalyser import UzMorphAnalyser
from uztagger import Tagger
from UzSyllable import syllables, count
import pickle
from .models import APILog


def log_api_request(method, request, response):
    client_ip = request.META.get('REMOTE_ADDR', 'Unknown')
    APILog.objects.create(
        method=method,
        request_text=str(request.data),
        response_text=str(response.data),
        client_ip=client_ip
    )


# ---------------UzTransliterator---------------
class TransliteratorView(APIView):
    def post(self, request):
        text = request.data.get('text')
        from_ = request.data.get('from_')
        to = request.data.get('to')
        if not text or not from_ or not to:
            response = Response({'error': 'Missing required parameters'}, status=status.HTTP_400_BAD_REQUEST)
            log_api_request('translit', request, response)
            return response
        obj = UzTransliterator.UzTransliterator()
        response = Response({'result': obj.transliterate(text, from_, to).replace('"', '')})
        log_api_request('translit', request, response)
        return response


# ---------------UzMorphAnalyser---------------
class MorphAnalyserView(APIView):
    def post(self, request):
        word = request.data.get('word')
        pos = request.data.get('pos', None)
        obj = UzMorphAnalyser()
        response = Response({'result': obj.analyze(word, pos)})
        log_api_request('uzmorphanalyser', request, response)
        return response


class StemView(APIView):
    def post(self, request):
        word = request.data.get('word')
        obj = UzMorphAnalyser()
        response = Response({'result': obj.stem(word)})
        log_api_request('stem', request, response)
        return response


class LemmatizeView(APIView):
    def post(self, request):
        word = request.data.get('word')
        pos = request.data.get('pos', None)
        obj = UzMorphAnalyser()
        response = Response({'result': obj.lemmatize(word, pos)})
        log_api_request('lemmatize', request, response)
        return response


# ---------------uztagger---------------
class PosTaggingView(APIView):
    def post(self, request):
        text = request.data.get('text')
        obj = Tagger()
        response = Response({'result': obj.pos_tag(text)})
        log_api_request('postagging', request, response)
        return response


# ----------------UzSyllable----------------
class SyllablesView(APIView):
    def post(self, request):
        word = request.data.get('word')
        response = Response({'result': syllables(word)})
        log_api_request('syllables', request, response)
        return response


class CountSyllablesView(APIView):
    def post(self, request):
        word = request.data.get('word')
        response = Response({'result': count(word)})
        log_api_request('count', request, response)
        return response


# ----------------Genre Classification----------------
class GenreClassificationView(APIView):
    def post(self, request):
        text = request.data.get('text')
        model_path = os.path.join(settings.STATIC_ROOT, 'models', 'trained_model100.pkl')
        vectorizer_path = os.path.join(settings.STATIC_ROOT, 'models', 'vectorizer.pkl')

        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        with open(vectorizer_path, 'rb') as file:
            vectorizer = pickle.load(file)

        text_vectorized = vectorizer.transform([text])
        predicted_genre = model.predict(text_vectorized)
        response = Response({'result': str(predicted_genre).replace("'", '').replace('[', '').replace(']', '')})
        log_api_request('genre_classification', request, response)
        return response
