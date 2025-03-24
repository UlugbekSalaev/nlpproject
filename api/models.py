from django.db import models


class APILog(models.Model):
    METHOD_CHOICES = [
        ('translit', 'Transliteration'),
        ('stem', 'Stemming'),
        ('lemmatize', 'Lemmatization'),
        ('uzmorphanalyser', 'Morph Analysis'),
        ('postagging', 'POS Tagging'),
        ('syllables', 'Syllables'),
        ('count', 'Count Syllables'),
        ('genre_classification', 'Genre Classification'),
    ]

    method = models.CharField(max_length=50, choices=METHOD_CHOICES, verbose_name="Метод")
    request_text = models.TextField(verbose_name="Текст запроса")
    response_text = models.TextField(verbose_name="Ответ API")
    client_ip = models.GenericIPAddressField(verbose_name="IP клиента")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время запроса")

    def __str__(self):
        return f"{self.method} | {self.client_ip} | {self.timestamp}"

    class Meta:
        verbose_name = "Лог API-запроса"
        verbose_name_plural = "Логи API-запросов"
