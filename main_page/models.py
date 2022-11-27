from django.db import models
from django.contrib.auth.models import User

# usr_id, name, email, programming_lang, mast
class UserInfo(models.Model):
    usr_id = models.BigIntegerField(verbose_name='id пользователь')
    name = models.TextField(verbose_name='Имя/Ник пользователя')
    email = models.TextField(verbose_name='Почта пользователя')
    programming_lang = models.TextField(verbose_name='Знает языки')
    mast = models.TextField(verbose_name='Сфера разработки')
    
    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'

class Quiz(models.Model):
    question_id = models.IntegerField(verbose_name='Айди вопроса')
    question_text = models.TextField(verbose_name="текст вопроса")
    opt1 = models.TextField(verbose_name="ответ1")
    opt2 = models.TextField(verbose_name="ответ2")
    opt3 = models.TextField(verbose_name="ответ3")
    opt4 = models.TextField(verbose_name="ответ4")
    questioner_name = models.TextField(verbose_name="имя")

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'