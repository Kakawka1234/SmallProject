# Generated by Django 5.2 on 2025-04-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'Новий'), ('in_progress', 'В процесі'), ('completed', 'Виконано')], default='new', max_length=20),
        ),
    ]
