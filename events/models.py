from django.db import models
from typing import Any

from training_center.models import EducationMethod, EducationOrg
from employees.models import Employee
from elearning.models import CourseResult, TestResult

class ContractType(models.Model):
    """Тип договора"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'contract_types'
        verbose_name = 'Тип договора'
        verbose_name_plural = 'Типы договоров'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ContractFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    
    class Meta:
        db_table = 'contract_file'
        verbose_name = 'Файл договора'
        verbose_name_plural = 'Файлы договора'


class Contract(models.Model):
    """Договор"""
    
    STATES = [
        (1, 'Планируется'),
        (2, 'В процессе заключения'),
        (3, 'Заключен'),
        (4, 'Исполнен'),
        (5, 'Отменен'),
    ]
    
    PURCHASE_METHODS = [
        (1, 'Единственный поставщик'),
        (2, 'до 500 000 руб.'),
        (3, 'свыше 500 000 руб.'),
    ]
    
    PURCHASE_STAGES = [
        (1, 'Запрос КП'),
        (2, 'Утверждение ТЗ'),
        (3, 'Согласование НМЦ'),
        (4, 'Утверждение на ТК'),
        (5, 'Выбор поставщика на ТК'),
        (6, 'Согласоание договора'),
        (7, 'Одобрение сделки на ПК'),
        (8, 'Подписание договора контрагентом'),
        (9, 'Согласование протокола разногласий'),
    ]
    
    CATHEGORYS = [
        (1, 'Доходный'),
        (2, 'Расходный')
    ]
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    education_org = models.ForeignKey(EducationOrg, verbose_name='Учебная организация', on_delete=models.PROTECT)
    date = models.DateField('Дата договора')
    number = models.CharField('Номер договора', max_length=255)
    contract_type = models.ForeignKey(ContractType, verbose_name='Тип договора', on_delete=models.PROTECT)
    start_date = models.DateField('Дата начала')
    finish_date = models.DateField('Дата окончания')
    cost = models.FloatField('Сумма контракта', null=True, blank=True)
    files = models.ManyToManyField(ContractFile, verbose_name='Файлы')
    state = models.CharField('Статус', max_length=100, choices=STATES, default='Планируется')
    responsible = models.ManyToManyField(Employee, verbose_name='Ответственные')
    purchase_method = models.CharField('Тип закупки', max_length=100, choices=PURCHASE_METHODS, default='до 500 000 руб.')
    cathegory = models.CharField('Категория', max_length=100, choices=CATHEGORYS, default='Расходный')
    purchase_stages = models.CharField('Этап закупки', max_length=100, choices=PURCHASE_STAGES, default='Запрос КП')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'contracts'
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Region(models.Model):
    """Регион места проведения обучения"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'region'
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Place(models.Model):
    """Место проведения"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.PROTECT, null=True, blank=True)
    address = models.TextField('Адрес', null=True, blank=True)
    number_of_seats = models.PositiveSmallIntegerField('Количество посадочных мест')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'places'
        verbose_name = 'Место проведения'
        verbose_name_plural = 'Места проведения'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class EventFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    
    class Meta:
        db_table = 'event_file'
        verbose_name = 'Файл мероприятия'
        verbose_name_plural = 'файлы мероприятия'


class Event(models.Model):
    """Мероприятие"""
    
    STATES = [
        (1, 'ЭТАЛОН'),
        (2, 'Планируется'),
        (3, 'Проводится'),
        (4, 'Завершено'),
        (5, 'Отменено'),
    ]
    
    PAYMENT_STATUSES = [
        (1, 'Не оплачен'),
        (2, 'Счет выставлен'),
        (3, 'Оплачен'),
    ]
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    education_method = models.ForeignKey(EducationMethod, verbose_name='Учебная программа', on_delete=models.PROTECT, null=True, blank=True)
    start_date = models.DateField('Дата начала')
    plan_finish_date = models.DateField('Плановая дата окончания', null=True, blank=True)
    finish_date = models.DateField('Дата окончания')
    state = models.CharField('Статус мероприятия', max_length=100, choices=STATES, default='Планируется')
    duration_hours_fact = models.PositiveSmallIntegerField('Фактическое количество часов обучения', null=True, blank=True)
    max_employees = models.PositiveSmallIntegerField('Максимальное количество участников', null=True, blank=True)
    contract = models.ForeignKey(Contract, verbose_name='Договор', on_delete=models.PROTECT, null=True, blank=True)
    payment_status = models.CharField('Статус оплаты', max_length=100, choices=PAYMENT_STATUSES, default='Не оплачен')
    violation_of_obligations = models.TextField('Нарушение обязательств контрагентом', null=True, blank=True)
    final_cost = models.FloatField('Итоговая стоимость', null=True, blank=True)
    responsible = models.ManyToManyField(Employee, verbose_name='Ответственные', related_name='Ответственные')
    tutors = models.ManyToManyField(Employee, verbose_name='Преподаватели', related_name='Преподаватели')
    employees = models.ManyToManyField(Employee, verbose_name='Участники', related_name='Участники')
    place = models.ForeignKey(Place, verbose_name='Место проведения', on_delete=models.PROTECT, null=True, blank=True)
    files = models.ManyToManyField(EventFile, verbose_name='Файлы')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'events'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    
    
class TypeOfCertificate(models.Model):
    """Тип сертификата"""
    
    code = models.CharField('Код', max_length=255, default='', null=True, blank=True)
    name = models.CharField('Тип сертификата', max_length=255, default='')
    duration_years = models.PositiveIntegerField('Срок действия в годах', null=True, blank=True)
    forever = models.BooleanField('Бессрочный', default=False)
    cost = models.FloatField('Стоимость', default='', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'type_of_certificates'
        verbose_name = 'Тип сертификата'
        verbose_name_plural = 'Типы сертификатов'
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CertificateFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    
    class Meta:
        db_table = 'certificate_file'
        verbose_name = 'Файл сертификата'
        verbose_name_plural = 'Файлы сертификатов'


class Certificate(models.Model):
    """Сертификат"""
    
    serial = models.CharField('Серия', max_length=255, default='', null=True, blank=True)
    number = models.CharField('Номер', max_length=255, default='', null=True, blank=True)
    type_of_certificate = models.ForeignKey(TypeOfCertificate, verbose_name='Тип сертификата', on_delete=models.PROTECT, null=True, blank=True)
    desctription = models.TextField('Описание', null=True, blank=True)
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.PROTECT)
    event = models.ForeignKey(Event, verbose_name='Мероприятие', on_delete=models.PROTECT, null=True, blank=True)
    course = models.ForeignKey(CourseResult, verbose_name='Электронный курс', on_delete=models.PROTECT, null=True, blank=True)
    test = models.ForeignKey(TestResult, verbose_name='Тест', on_delete=models.PROTECT, null=True, blank=True)
    delivery_date = models.DateField('Дата выдачи', auto_now_add=False)
    expire_date = models.DateField('Срок действия', auto_now_add=False, null=True, blank=True)
    valid = models.BooleanField('Действилтелен', default=True)
    files=models.ManyToManyField(CertificateFile, verbose_name='Файлы')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'certificates'
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
        ordering = ['employee']

    def __str__(self):
        return self.employee
    
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
    
    class Meta:
        db_table = 'poll_entryes'
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PollQuestion(models.Model):
    """Вопрос опроса"""
    
    CHOICE = [
        (1, 'Единственный выбор'),
        (2, 'Множественный выбор'),
        (3, 'Ранжирование'),
        (4, 'Сравнение'),
        (5, 'Текстовый ввод'),        
    ]
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    q_type = models.CharField('Тип вопроса', max_length=100, choices=CHOICE, default='Тектовый ввод')
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    weight = models.SmallIntegerField('Вес вопроса')
    entries = models.ManyToManyField(PollEntry, verbose_name='Варианты ответов')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'poll_questions'
        verbose_name = 'Вопрос опроса'
        verbose_name_plural = 'Вопросы опросов'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Poll(models.Model):
    """Опрос"""
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    questions = models.ManyToManyField(PollQuestion, verbose_name='Djghjcs')
    access = models.TextField('Доступ')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PollResult(models.Model):
    """Результат прохождения опроса сотрудником"""
    
    
    STATES = [
        (1, 'Назначен'),
        (2, 'В процессе'),
        (3, 'Пройден'),
    ]
    
    code = models.CharField('Код', max_length=128, null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', null=True, blank=True)
    poll = models.ForeignKey(Poll, verbose_name='Опрос', on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, verbose_name='Сотрудник', on_delete=models.PROTECT)
    event = models.ForeignKey(Event, verbose_name='Мероприятие', on_delete=models.PROTECT, null=True, blank=True)
    appointment_date = models.DateField('Дата прохождения опроса', auto_now_add=True)
    score = models.FloatField('Итоговый балл', null=True, blank=True)
    state = models.CharField('Статус опроса', max_length=100, choices=STATES, default='Назначен')
    poll_details = models.TextField('Подробные результаты опроса')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
    class Meta:
        db_table = 'poll_results'
        verbose_name = 'Результат опроса'
        verbose_name_plural = 'Результаты опросов'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)