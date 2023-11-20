from django.db import models
from typing import Any

from employees.models import Employee


class Course(models.Model):
    """Электронный курс"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    url = models.URLField('Ссылка на курс', max_length=200)
    max_score = models.FloatField('Максимальный балл', null=True, blank=True)
    check_score = models.FloatField('Проходной балл', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CourseResult(models.Model):
    """Результат прохождения электронного курса сотрудником"""
    
    STATES = [
        (1, 'Назначен'),
        (2, 'В процессе'),
        (3, 'Не пройден'),
        (4, 'Пройден'),
    ]
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    course = models.ForeignKey(Course, verbose_name='Электронный курс', on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.PROTECT)
    appointment_date = models.DateField('Дата назначения', auto_now_add=True)
    start_learning_date = models.DateField('Дата начала обучения', null=True, blank=True)
    finish_learning_date = models.DateField('Дата окончания обучения', null=True, blank=True)
    score = models.FloatField('Итоговый балл', null=True, blank=True)
    state = models.CharField('Статус курса', max_length=100, choices=STATES, default='Назначен')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TestEntry(models.Model):
    """Вариант ответа на вопрос"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    weight = models.SmallIntegerField('Вес ответа')
    true = models.BooleanField('Правильный ответ', default=False)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TestQuestion(models.Model):
    """Вопрос теста"""
    
    CHOICE = [
        (1, 'Единственный выбор'),
        (2, 'Множественный выбор'),
        (3, 'Ранжирование'),
        (4, 'Сравнение')        
    ]
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    q_type = models.CharField('Тип вопроса', max_length=100, choices=CHOICE, default='Единственный выбор')
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    weight = models.SmallIntegerField('Вес вопроса')
    entries = models.ManyToManyField(TestEntry, verbose_name='Варианты ответов')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Test(models.Model):
    """Электронный Тест"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    max_score = models.FloatField('Максимальный балл', null=True, blank=True)
    check_score = models.FloatField('Проходной балл', null=True, blank=True)
    questions = models.ManyToManyField(TestQuestion, verbose_name='Djghjcs')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class TestResult(models.Model):
    """Результат прохождения теста сотрудником"""
    
    STATES = [
        (1, 'Назначен'),
        (2, 'В процессе'),
        (3, 'Не пройден'),
        (4, 'Пройден'),
    ]
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    test = models.ForeignKey(Test, verbose_name='Электронный тест', on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.PROTECT)
    appointment_date = models.DateField('Дата назначения', auto_now_add=True)
    start_learning_date = models.DateField('Дата начала обучения', null=True, blank=True)
    finish_learning_date = models.DateField('Дата окончания обучения', null=True, blank=True)
    score = models.FloatField('Итоговый балл', null=True, blank=True)
    state = models.CharField('Статус теста', max_length=100, choices=STATES, default='Назначен')
    test_details = models.TextField('Подробные результаты теста')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PollEntry(models.Model):
    """Вариант ответа на вопрос"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    weight = models.SmallIntegerField('Вес ответа')
    true = models.BooleanField('Правильный ответ', default=False)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

