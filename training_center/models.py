from typing import Any
from django.db import models
from employees.models import Employee


class EducationOrg(models.Model):
    """Обучающая организация"""
    display_name = models.CharField('Краткое имя', max_length=255, default='')
    fullname = models.TextField('Полное наименование', default='')
    contacts = models.CharField('Контакты', max_length=255, default='')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)

    def __str__(self):
        return self.display_name

    def __int__(self, display_name, fullname):
        self.display_name = display_name
        self.fullname = fullname

class EventForm(models.Model):
    """Форма проведения обучения"""
    
    code = models.CharField('Код', max_length=255, default='', null=True, blank=True)
    name = models.CharField('Учебная программа', max_length=255, default='')
    description = models.TextField('Описание', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)
    
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
    
    def __str__(self) -> str:
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
    
    def __str__(self) -> str:
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CertificateFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")


class Certificate(models.Model):
    """Сертификат"""
    
    serial = models.CharField('Серия', max_length=255, default='', null=True, blank=True)
    number = models.CharField('Номер', max_length=255, default='', null=True, blank=True)
    type_of_certificate = models.ForeignKey(TypeOfCertificate,'Тип сертификата', on_delete=models.PROTECT, default='')
    desctription = models.TextField('Описание', null=True, blank=True)
    employee = models.ForeignKey(Employee, 'Сотрудник', on_delete=models.PROTECT)
    # event = models.ForeignKey(Event, 'Мероприятие', on_delete=models.PROTECT, null=True, blank=True)
    # course = models.ForeignKey(Course, 'Электронный курс', on_delete=models.PROTECT, null=True, blank=True)
    # test = models.ForeignKey(Test, 'Тест', on_delete=models.PROTECT, null=True, blank=True)
    delivery_date = models.DateField('Дата выдачи', auto_now_add=False)
    expire_date = models.DateField('Срок действия', auto_now_add=False, null=True, blank=True)
    valid = models.BooleanField('Действилтелен', default=True)
    files=models.ManyToManyField(CertificateFile, verbose_name='Файлы', null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)

    def __str__(self):
        return self.employee
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class EducationMethod(models.Model):
    """Учебная программа"""
    
    EDUTYPES = ('Обязательное', 'Дополнительное')

    code = models.CharField('Код', max_length=255, default='', null=True, blank=True)
    name = models.CharField('Учебная программа', max_length=255, default='')
    education_org = models.ForeignKey(EducationOrg, verbose_name='Обучающая организация', on_delete=models.PROTECT, null=True, blank=True)
    event_form = models.ForeignKey('Форма проведения', on_delete=models.PROTECT, null=True, blank=True)
    cost = models.FloatField('Стоимость', null=True, blank=True)
    duration_hours = models.IntegerField('Продолжительность в часах', null=True, blank=True)
    education_type = models.CharField('Тип обучения', max_length=255, choices=EDUTYPES, null=True, blank=True)
    direction_of_training = models.ForeignKey(DirectionOfTraining, verbose_name='Направление обучения', on_delete=models.PROTECT, null=True, blank=True)
    risk_level = models.ForeignKey(RiskLevel, verbose_name='Уровень риска', on_delete=models.PROTECT, null=True, blank=True)
    type_of_certificate = models.ForeignKey(TypeOfCertificate, verbose_name='Тип сертификата', on_delete=models.PROTECT, null=True, blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
