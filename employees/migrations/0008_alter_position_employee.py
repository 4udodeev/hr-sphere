# Generated by Django 4.2.7 on 2023-11-24 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_alter_employee_sex_alter_position_subdivision'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='employees.employee', verbose_name='Сотрудник'),
        ),
    ]