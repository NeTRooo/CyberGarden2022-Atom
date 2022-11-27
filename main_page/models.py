from django.db import models
from django.contrib.auth.models import User

# usr_id, name, email, programming_lang, mast


class UserInfo(models.Model):
    usr_id = models.BigIntegerField(verbose_name='id пользователь')
    name = models.TextField(verbose_name='Имя/Ник пользователя')
    email = models.TextField(verbose_name='Почта пользователя')
    programming_lang = models.TextField(verbose_name='Знает языки')
    mast = models.TextField(verbose_name='Сфера разработки')
    start_time = models.IntegerField(verbose_name='Время начала')
    end_time = models.IntegerField(verbose_name='Время конца')
    best_time = models.IntegerField(verbose_name='Лучшее время')
    score = models.IntegerField(verbose_name='кол-во очков за тест')

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'

class Quiz(models.Model):
    question_id = models.IntegerField(verbose_name='Айд и вопроса')
    question_text = models.TextField(verbose_name="текст вопроса")
    opt1 = models.TextField(verbose_name="ответ1")
    opt2 = models.TextField(verbose_name="ответ2")
    opt3 = models.TextField(verbose_name="ответ3")
    opt4 = models.TextField(verbose_name="ответ4")
    questioner_name = models.TextField(verbose_name="имя")
    right_answ = models.TextField(verbose_name="верный ответ")

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'