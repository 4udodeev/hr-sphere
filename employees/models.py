from typing import Any

from django.db import models


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
    middlename = models.CharField('Отчество', max_length=255, null=True, blank=True)
    fullname = models.CharField('ФИО', max_length=255, null=True, blank=True)
    sex = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('Дата рождения', default='')
    phone = models.CharField('Телефон', max_length=20, null=True, blank=True)
    email = models.EmailField('Электронная почта', default='', null=True, blank=True)
    passport = models.CharField('Паспортные данные', max_length=255, null=True, blank=True)
    snils = models.CharField('СНИЛС', max_length=255, null=True, blank=True)
    address = models.TextField('Адрес проживания', null=True, blank=True)
    education = models.TextField('Образование', null=True, blank=True)
    photo = models.ImageField('Фотография', upload_to='images/photo', null=True, blank=True)

    # Данные о работнике
    login = models.CharField('Логин', max_length=255, default=code)
    password = models.CharField('Пароль', max_length=255, default=code)
    change_password = models.BooleanField('Необходимо сменить пароль', default=True)
    position_id = models.CharField('Должность', max_length=255, null=True, blank=True)
    hire_date = models.DateField('Дата приема', auto_now_add=True)
    dismiss_date = models.DateField('Дата увольнения', default='', null=True, blank=True)
    is_dismiss = models.BooleanField('Уволен', default=False, null=True, blank=True)
    is_banned = models.BooleanField('Заблокирован доступ на портал', default=False, null=True, blank=True)
    change_logs = models.JSONField('История изменений', default=dict,
                                   blank=True)  # Первое изменение должно прописываться при создании
    history_states = models.JSONField('Состояния работника', default=dict, blank=True)
    doc_info = models.TextField('doc_info', null=True, blank=True)

    def __str__(self):
        if self.middlename:
            return f"{self.lastname} {self.firstname} {self.middlename}"
        else:
            return f"{self.lastname} {self.firstname}"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def save(self):
        if self.middlename:
            self.fullname = f"{self.lastname} {self.firstname} {self.middlename}"
        else:
            self.fullname = f"{self.lastname} {self.firstname}"
        super().save(self)


class Organization(models.Model):
    """Организация"""
    display_name = models.CharField('Краткое имя', max_length=255, default='')
    fullname = models.TextField('Полное наименование', default='')
    func_managers = models.ManyToManyField(Employee, verbose_name='Функциональыне руководители', blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)

    def __str__(self):
        return self.display_name

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Subdivision(models.Model):
    """"Подразделение"""
    code = models.CharField('Код подразделения', max_length=255)
    name = models.CharField('Наименование', max_length=255)
    org_id = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация')
    parent_subdivision_id = models.ForeignKey('self', blank=True, related_name='children', on_delete=models.PROTECT,
                                              verbose_name='Родительское подразделение', null=True)
    is_active = models.BooleanField('Активное', default=True)
    start_date = models.DateField('Дата формирования', auto_now_add=True)
    finish_date = models.DateField('Дата расформирования', default='', null=True, blank=True)
    func_managers = models.ManyToManyField(Employee, verbose_name='Функциональные руководители', blank=True)
    
    doc_info = models.TextField('doc_info', null=True, blank=True)

    def __str__(self):
        return self.name

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Position(models.Model):
    """Должность"""
    code = models.CharField('Код', max_length=255, default='')
    name = models.CharField('Название', max_length=255, default='')
    is_boss = models.BooleanField('Является руководителем', default=False)
    employee = models.OneToOneField(Employee, on_delete=models.PROTECT, verbose_name='Сотрудник', null=True, blank=True)
    org_id = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация')
    subdivision_id = models.ForeignKey(Subdivision, on_delete=models.PROTECT, verbose_name='Подразделение')
    function = models.ManyToManyField(to='training_center.Function', verbose_name='Функции')
    
    doc_info = models.TextField('doc_info', null=True, blank=True)

    def __str__(self):
        return self.name

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
     
        
