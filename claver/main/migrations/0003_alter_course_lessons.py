# Generated by Django 3.2.7 on 2021-11-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_lesson_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(related_name='Course_lessons', to='main.Lesson'),
        ),
    ]