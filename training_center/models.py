from typing import Any
from django.db import models


from elearning.models import Course, Test



class EducationOrg(models.Model):
    """Обучающая организация"""
    display_name = models.CharField('Краткое имя', max_length=255, default='')
    fullname = models.TextField('Полное наименование', default='')
    contacts = models.CharField('Контакты', max_length=255, default='')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'education_orgs'
        verbose_name = 'Обучающая организация'
        verbose_name_plural = 'Обучающие организации'
        ordering = ['display_name']

    def __str__(self):
        return self.display_name

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class EventForm(models.Model):
    """Форма проведения обучения"""
    
    code = models.CharField('Код', max_length=255, default='', null=True, blank=True)
    name = models.CharField('Форма проведения', max_length=255, default='')
    description = models.TextField('Описание', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'event_forms'
        verbose_name = 'Форма проведения обучения'
        verbose_name_plural = 'Формы проведения обучения'
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        

class DirectionOfTraining(models.Model):
    """Вид обучения - ОТ / промбез / ГО / иностранные языки / ... / не используется"""
    
    code = models.CharField('Код', max_length=255, default='', null=True, blank=True)
    name = models.CharField('Учебная программа', max_length=255, default='')
    description = models.TextField('Описание', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'directions_of_training'
        verbose_name = 'Вид обучения'
        verbose_name_plural = 'Виды обучения'
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        

class RiskLevel(models.Model):
    """Уровень риска"""
    code = models.CharField('Код', max_length=255, default='', null=True, blank=True)
    name = models.CharField('Учебная программа', max_length=255, default='')
    description = models.TextField('Описание', null=True, blank=True)
    aftereffects_verification = models.TextField('Последствия в случае проверок', null=True, blank=True)
    aftereffects_incident = models.TextField('Последствия при НС, ЧП, ЧС', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'risk_levels'
        verbose_name = 'Уровень риска'
        verbose_name_plural = 'Уровни риска'
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        

class EducationMethod(models.Model):
    """Учебная программа"""
    
    EDUTYPES = [('1', 'Обязательное'), ('2', 'Дополнительное')]

    code = models.CharField('Код', max_length=255, default='', null=True, blank=True)
    name = models.CharField('Учебная программа', max_length=255, default='')
    education_org = models.ForeignKey(EducationOrg, verbose_name='Обучающая организация', on_delete=models.PROTECT, null=True, blank=True)
    event_form = models.ForeignKey(EventForm, verbose_name='Форма проведения', on_delete=models.PROTECT, null=True, blank=True)
    cost = models.FloatField('Стоимость', null=True, blank=True)
    duration_hours = models.IntegerField('Продолжительность в часах', null=True, blank=True)
    education_type = models.CharField('Тип обучения', max_length=255, choices=EDUTYPES, null=True, blank=True)
    direction_of_training = models.ForeignKey(DirectionOfTraining, verbose_name='Направление обучения', on_delete=models.PROTECT, null=True, blank=True)
    risk_level = models.ForeignKey(RiskLevel, verbose_name='Уровень риска', on_delete=models.PROTECT, null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'education_methods'
        verbose_name = 'Учебная программа'
        verbose_name_plural = 'Учебные программы'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Competention(models.Model):
    """Компетенция"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    education_methods = models.ManyToManyField(EducationMethod, verbose_name='Учебные программы')
    courses = models.ManyToManyField(Course, verbose_name='Курсы', blank=True)
    tests = models.ManyToManyField(Test, verbose_name='Тесты', blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'competentions'
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Function(models.Model):
    """Функция должности"""
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    competentions = models.ManyToManyField(Competention, verbose_name='Компетенции')
    education_methods = models.ManyToManyField(EducationMethod, verbose_name='Учебные программы')
    courses = models.ManyToManyField(Course, verbose_name='Курсы', blank=True)
    tests = models.ManyToManyField(Test, verbose_name='Тесты', blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'functions'
        verbose_name = 'Функция должности'
        verbose_name_plural = 'Функции должностей'
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        
