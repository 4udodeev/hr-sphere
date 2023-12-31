# Generated by Django 4.2.7 on 2023-11-16 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('training_center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=128, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата договора')),
                ('number', models.CharField(max_length=255, verbose_name='Номер договора')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('finish_date', models.DateField(verbose_name='Дата окончания')),
                ('cost', models.FloatField(blank=True, null=True, verbose_name='Сумма контракта')),
                ('state', models.CharField(choices=[(1, 'Планируется'), (2, 'В процессе заключения'), (3, 'Заключен'), (4, 'Исполнен'), (5, 'Отменен')], default='Планируется', max_length=100, verbose_name='Статус')),
                ('purchase_method', models.CharField(choices=[(1, 'Единственный поставщик'), (2, 'до 500 000 руб.'), (3, 'свыше 500 000 руб.')], default='до 500 000 руб.', max_length=100, verbose_name='Тип закупки')),
                ('cathegory', models.CharField(choices=[(1, 'Доходный'), (2, 'Расходный')], default='Расходный', max_length=100, verbose_name='Категория')),
                ('purchase_stages', models.CharField(choices=[(1, 'Запрос КП'), (2, 'Утверждение ТЗ'), (3, 'Согласование НМЦ'), (4, 'Утверждение на ТК'), (5, 'Выбор поставщика на ТК'), (6, 'Согласоание договора'), (7, 'Одобрение сделки на ПК'), (8, 'Подписание договора контрагентом'), (9, 'Согласование протокола разногласий')], default='Запрос КП', max_length=100, verbose_name='Этап закупки')),
                ('doc_info', models.TextField(blank=True, null=True, verbose_name='doc_info')),
            ],
        ),
        migrations.CreateModel(
            name='ContractFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=128, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('doc_info', models.TextField(blank=True, null=True, verbose_name='doc_info')),
            ],
        ),
        migrations.CreateModel(
            name='EventFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=128, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('doc_info', models.TextField(blank=True, null=True, verbose_name='doc_info')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=128, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('number_of_seats', models.PositiveSmallIntegerField(verbose_name='Количество посадочных мест')),
                ('doc_info', models.TextField(blank=True, null=True, verbose_name='doc_info')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.region', verbose_name='Регион')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=128, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('plan_finish_date', models.DateField(blank=True, null=True, verbose_name='Плановая дата окончания')),
                ('finish_date', models.DateField(verbose_name='Дата окончания')),
                ('state', models.CharField(choices=[(1, 'ЭТАЛОН'), (2, 'Планируется'), (3, 'Проводится'), (4, 'Завершено'), (5, 'Отменено')], default='Планируется', max_length=100, verbose_name='Статус мероприятия')),
                ('duration_hours_fact', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Фактическое количество часов обучения')),
                ('max_employees', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Максимальное количество участников')),
                ('payment_status', models.CharField(choices=[(1, 'Не оплачен'), (2, 'Счет выставлен'), (3, 'Оплачен')], default='Не оплачен', max_length=100, verbose_name='Статус оплаты')),
                ('violation_of_obligations', models.TextField(blank=True, null=True, verbose_name='Нарушение обязательств контрагентом')),
                ('final_cost', models.FloatField(blank=True, null=True, verbose_name='Итоговая стоимость')),
                ('doc_info', models.TextField(blank=True, null=True, verbose_name='doc_info')),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.contract', verbose_name='Договор')),
                ('education_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='training_center.educationmethod', verbose_name='Учебная программа')),
                ('employees', models.ManyToManyField(related_name='Участники', to='employees.employee', verbose_name='Участники')),
                ('files', models.ManyToManyField(to='events.eventfile', verbose_name='Файлы')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.place', verbose_name='Место проведения')),
                ('responsible', models.ManyToManyField(related_name='Ответственные', to='employees.employee', verbose_name='Ответственные')),
                ('tutors', models.ManyToManyField(related_name='Преподаватели', to='employees.employee', verbose_name='Преподаватели')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.contracttype', verbose_name='Тип договора'),
        ),
        migrations.AddField(
            model_name='contract',
            name='education_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='training_center.educationorg', verbose_name='Учебная организация'),
        ),
        migrations.AddField(
            model_name='contract',
            name='files',
            field=models.ManyToManyField(to='events.contractfile', verbose_name='Файлы'),
        ),
        migrations.AddField(
            model_name='contract',
            name='responsible',
            field=models.ManyToManyField(to='employees.employee', verbose_name='Ответственные'),
        ),
    ]
