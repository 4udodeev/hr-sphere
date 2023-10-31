import datetime

from django.db import models

from training_center.models import EducationPlan


def correct_fullname(lastname, firstname, middlename=''):
    if middlename == '':
        return f"{lastname} {firstname} {middlename}"
    else:
        return f"{lastname} {firstname}"


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
    middlename = models.CharField('Отчество', max_length=255, null=True)
    fullname = models.CharField('ФИО', max_length=255, default=correct_fullname(lastname, firstname, middlename))
    sex = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='', null=True)
    phone = models.CharField('Телефон', max_length=20, null=True)
    email = models.EmailField('Электронная почта', default='', null=True)
    passport = models.CharField('Паспортные данные', max_length=255, default='', null=True)
    snils = models.CharField('СНИЛС', max_length=255, default='', null=True)
    address = models.TextField('Адрес проживания', default='', null=True)
    education = models.TextField('Образование', default='', null=True)
    photo = models.ImageField('Фотография', upload_to='images/photo', null=True)

    # Данные о работнике
    login = models.CharField('Логин', max_length=255, default=code)
    password = models.CharField('Пароль', max_length=255, default=code)
    change_password = models.BooleanField('Необходимо сменить пароль', default=True)
    position = models.CharField('Должность', max_length=255, default='')
    hire_date = models.DateField('Дата приема', auto_now_add=True)
    dismiss_date = models.DateField('Дата увольнения', default='', null=True)
    is_dismiss = models.BooleanField('Уволен', default=False)
    is_banned = models.BooleanField('Заблокирован доступ на портал', default=False)
    change_logs = models.JSONField('История изменений',
                                   default=dict, null=True)  # Первое изменение должно прописываться при создании
    history_states = models.JSONField('Состояния работника', default=dict, null=True)

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



class Organization(models.Model):
    """Организация"""
    display_name = models.CharField('Краткое имя', max_length=255, default='')
    fullname = models.TextField('Полное наименование', default='')
    func_managers = models.ManyToManyField(Employee, verbose_name='Руководители', null=True)

    def __str__(self):
        return self.display_name

    def __int__(self, display_name, fullname):
        self.display_name = display_name
        self.fullname = fullname


class Subdivision(models.Model):
    """"Подразделение"""
    code = models.CharField('Код подразделения', max_length=255)
    name = models.CharField('Наименование', max_length=255)
    org_id = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация')
    parent_subdivision_id = models.ForeignKey('self', blank=True, related_name='children', on_delete=models.PROTECT,
                                              verbose_name='Родительское подразделение')
    is_active = models.BooleanField('Активное', default=True)
    start_date = models.DateField('Дата формирования', auto_now_add=True)
    finish_date = models.DateField('Дата расформирования', default='', null=True)
    func_managers = models.ManyToManyField(Employee, verbose_name='Руководители', null=True)

    def __str__(self):
        return self.name

    def __int__(self, code, name, org_id, parent_subdivision_id, is_active, start_date):
        self.code = code
        self.name = name
        self.org_id = org_id
        self.parent_subdivision_id = parent_subdivision_id
        self.is_active = is_active
        self.start_date = start_date


class Position(models.Model):
    """Должность"""
    code = models.CharField('Код', max_length=255, default='')
    name = models.CharField('Название', max_length=255, default='')
    org_id = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация')
    subdivision_id = models.ForeignKey(Subdivision, on_delete=models.PROTECT, verbose_name='Подразделение')
    education_plan = models.ForeignKey(EducationPlan, on_delete=models.PROTECT, verbose_name='Учебный план')
    employee_id = models.OneToOneField(Employee, verbose_name='Сотрудник')

    def __str__(self):
        return self.name

    def __int__(self, code, name, org_id, subdivision_id):
        self.code = code
        self.name = name
        self.org_id = org_id
        self.subdivision_id = subdivision_id
