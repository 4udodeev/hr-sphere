import datetime

from django.db import models

from training_center.models import EducationPlan


class Organization(models.Model):
    """Организация"""
    display_name = models.CharField('Краткое имя', max_length=255, default='')
    fullname = models.TextField('Полное наименование', default='')
    func_managers = models.JSONField('Функциональыне руководители', default=dict)

    def __str__(self):
        return self.display_name

    def __int__(self, display_name, fullname, func_managers):
        self.display_name = display_name
        self.fullname = fullname
        self.func_managers = func_managers


class Subdivision(models.Model):
    """"Подразделение"""
    code = models.CharField('Код подразделения', max_length=255)
    name = models.CharField('Наименование', max_length=255)
    org_id = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация')
    parent_subdivision_id = models.ForeignKey('self', blank=True, related_name='children', on_delete=models.PROTECT, verbose_name='Родительское подразделение')
    is_active = models.BooleanField('Активное', default=True)
    start_date = models.DateField('Дата формирования', auto_now_add=True)
    finish_date = models.DateField('Дата расформирования', default='')
    func_managers = models.JSONField('Функциональыне руководители', default=dict)

    def __str__(self):
        return self.name

    def __int__(self, code, name, org_id, parent_subdivision_id, is_active, start_date, finish_date, func_managers):
        self.code = code
        self.name = name
        self.org_id = org_id
        self.parent_subdivision_id = parent_subdivision_id
        self.is_active = is_active
        self.start_date = start_date
        self.finish_date = finish_date
        self.func_managers = func_managers


class Position(models.Model):
    """Должность"""
    code = models.CharField('Код', max_length=255, default='')
    name = models.CharField('Название', max_length=255, default='')
    org_id = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация')
    subdivision_id = models.ForeignKey(Subdivision, on_delete=models.PROTECT, verbose_name='Подразделение')
    education_plan = models.ForeignKey(EducationPlan, on_delete=models.PROTECT, verbose_name='Учебный план')

    def __str__(self):
        return self.name

    def __int__(self, code, name, org_id, subdivision_id):
        self.code = code
        self.name = name
        self.org_id = org_id
        self.subdivision_id = subdivision_id



class Employee(models.Model):
    """Сотрудник"""

    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина')
    )

    # Персональная информация
    code = models.CharField('Табельный номер', max_length=255)
    lastname = models.CharField('Фамилия', max_length=255)
    firstname = models.CharField('Имя', max_length=255)
    middlename = models.CharField('Отчество', max_length=255)
    fullname = models.CharField('ФИО', max_length=255)
    sex = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='')
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Электронная почта', default='')
    passport = models.CharField('Паспортные данные', max_length=255, default='')
    snils = models.CharField('СНИЛС', max_length=255, default='')
    address = models.TextField('Адрес проживания', default='')
    education = models.TextField('Образование', default='')
    photo = models.ImageField('Фотография', upload_to='images/photo')

    # Данные о работнике
    login = models.CharField('Логин', max_length=255, default=code)
    password = models.CharField('Пароль', max_length=255, default=code)
    change_password = models.BooleanField('Необходимо сменить пароль', default=True)
    position_id = models.OneToOneField(Position, on_delete=models.PROTECT, verbose_name='Должность')
    hire_date = models.DateField('Дата приема', auto_now_add=True)
    dismiss_date = models.DateField('Дата увольнения', default='')
    is_dismiss = models.BooleanField('Уволен', default=False)
    is_banned = models.BooleanField('Заблокирован доступ на портал', default=False)
    change_logs = models.JSONField('История изменений', default=dict) # Первое изменение должно прописываться при создании
    history_states = models.JSONField('Состояния работника', default=dict)

    def __str__(self):
        if self.middlename:
            return f"{self.lastname} {self.firstname} {self.middlename}"
        else:
            return f"{self.lastname} {self.firstname}"

    def __int__(
            self,
            code,
            lastname,
            firstname,
            sex,
            login,
            password,
            hire_date,
            middlename='',
    ):
        self.code = code,
        self.lastname = lastname,
        self.firstname = firstname,
        self.middlename = middlename,
        self.sex = sex,
        self.login = login,
        self.password = password,
