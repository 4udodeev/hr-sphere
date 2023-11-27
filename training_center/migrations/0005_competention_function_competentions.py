# Generated by Django 4.2.7 on 2023-11-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0003_alter_course_table_alter_courseresult_table_and_more'),
        ('training_center', '0004_alter_directionoftraining_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=128, null=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('doc_info', models.TextField(blank=True, null=True, verbose_name='doc_info')),
                ('courses', models.ManyToManyField(blank=True, to='elearning.course', verbose_name='Курсы')),
                ('education_methods', models.ManyToManyField(to='training_center.educationmethod', verbose_name='Учебные программы')),
                ('tests', models.ManyToManyField(blank=True, to='elearning.test', verbose_name='Тесты')),
            ],
            options={
                'verbose_name': 'Компетенция',
                'verbose_name_plural': 'Компетенции',
                'db_table': 'competentions',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='function',
            name='competentions',
            field=models.ManyToManyField(to='training_center.competention', verbose_name='Компетенции'),
        ),
    ]
