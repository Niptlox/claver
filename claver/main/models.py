from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    class Status(models.IntegerChoices):
        ADMIN = 1
        VISITOR = 13
        TEACHER = 11
        STUDENT = 12

    status = models.IntegerField(choices=Status.choices, default=Status.VISITOR)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Class(models.Model):
    title = models.CharField("имя класса", max_length=200)
    students = models.ManyToManyField(Profile, related_name="Class_students")
    teachers = models.ManyToManyField(Profile, related_name="Class_teachers")

    description = models.TextField("Описание класса", default="...", max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"


class Task(models.Model):
    title = models.CharField("название задания", max_length=200)
    authors = models.ManyToManyField(Profile, related_name="Task_authors")
    students = models.ManyToManyField(Profile, related_name="Task_students")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class Lesson(models.Model):
    title = models.CharField("название урока", max_length=200)
    students = models.ManyToManyField(Profile, related_name="Lesson_students")
    teachers = models.ManyToManyField(Profile, related_name="Lesson_teachers")
    tasks = models.ManyToManyField(Task, related_name="Lesson_tasks")
    classes = models.ManyToManyField(Class, related_name="Lesson_classes")

    description = models.TextField("Описание урока", default="...", max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Course(models.Model):
    title = models.CharField("название курса", max_length=200)
    students = models.ManyToManyField(Profile, related_name="Course_students")
    teachers = models.ManyToManyField(Profile, related_name="Course_teachers")
    lessons = models.ManyToManyField(Lesson, related_name="Course_lessons")
    classes = models.ManyToManyField(Class, related_name="Course_classes")
    description = models.TextField("описание курса", default="...", max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
