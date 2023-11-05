from django.db import models


class EducationOrg(models.Model):
    """Обучающая организация"""
    display_name = models.CharField('Краткое имя', max_length=255, default='')
    fullname = models.TextField('Полное наименование', default='')
    contacts = models.CharField('Контакты', max_length=255, default='')

    def __str__(self):
        return self.display_name

    def __int__(self, display_name, fullname):
        self.display_name = display_name
        self.fullname = fullname


class EducationMethod(models.Model):
    """Учебная программа"""

    code = models.CharField('Код', max_length=255, default='')
    name = models.CharField('Учебная программа', max_length=255, default='')
    education_org_id = models.ForeignKey(EducationOrg, verbose_name='Обучающая организация', on_delete=models.PROTECT, null=True, blank=True)
    # event_form = models.TextField('Форма проведения', choices=EVENT_FORMS, default='Лекция')

    def __str__(self):
        return self.name

    def __int__(self, code, name, education_org_id):
        self.code = code
        self.name = name
        self.education_org_id = education_org_id


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
    # tests = ???
    # courses = ???

    def __str__(self):
        return self.name

    def __int__(self, code, name):
        self.code = code
        self.name = name
