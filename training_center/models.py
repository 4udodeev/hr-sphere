from django.db import models

class EducationMethod(models.Model):
    """Учебная программа"""
    code = models.CharField('Код', max_length=255, default='')
    name = models.CharField('Учебная программа', max_length=255, default='')




class Event(models.Model):
    """Мероприятие"""
    pass

class Certificate(models.Model):
    """Сертификат о пройденном обучении"""
    pass

class EventEmployees(models.Model):
    """Каталог-связка мероприятие-работники"""
    pass


class EducationPlan(models.Model):
    """План обучения (сокращенный аналог типовой должности в WT)"""
    code = models.CharField('Код', max_length=255, default='')
    name = models.CharField('Учебный план', max_length=255, default='')
    education_methods = models.ManyToManyField(EducationMethod, verbose_name='Учебные программы', default=dict)
    # tests =
    # courses =

    def __str__(self):
        return self.name

    def __int__(self, code, name):
        self.code = code
        self.name = name
