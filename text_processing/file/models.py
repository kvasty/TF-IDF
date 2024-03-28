from django.db import models


class Table(models.Model):
    """
    Модель результата
    """
    name_file = models.CharField(max_length=100)
    word = models.CharField(max_length=50)
    tf = models.FloatField()
    idf = models.FloatField()
