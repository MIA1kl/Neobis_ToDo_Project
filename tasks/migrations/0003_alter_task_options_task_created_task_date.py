# Generated by Django 4.2 on 2023-04-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_delete_taskitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateField(default='2023-04-17'),
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-04-17'),
        ),
    ]
