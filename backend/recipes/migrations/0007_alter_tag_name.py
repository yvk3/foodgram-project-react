# Generated by Django 3.2.2 on 2023-08-23 10:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(1, 'Название не может быть пустым')], verbose_name='Название тега'),
        ),
    ]