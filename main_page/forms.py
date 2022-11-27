from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

MAST_CHOICE=[('full','Full-stack developer'),('front','Frontend developer'),('back','Backend developer'),]

class ContactsForm(forms.Form):
    name = forms.CharField(max_length=32, min_length=3,)
    email = forms.EmailField()
    programming_lang = forms.CharField(max_length=128, min_length=1,)
    mast = forms.ChoiceField(choices=MAST_CHOICE)

ASK1_CHOISE=[('1','Pascal'),('2','Python'),('3','JS'),('4','HTML'),]
ASK2_CHOISE=[('5','Наследование'),('6','Абстракция'),('7','Преимущества'),('8','Все ответы правильны'),]
ASK3_CHOISE=[('9','процедурное, логическое, графическое'),('10','объектно-ориентированное;структурное,операторное'),('11','a и b правильны'),('12','Нет правильного ответа'),]
ASK4_CHOISE=[('13','python, C, java'),('14','JS, C#'),('15','python, C, паскаль'),('16','все языки'),]
ASK5_CHOISE=[('17','python, C#, R'),('18','Нету правильного ответа'),('19','CSS, HTML'),('20','a,b и c'),]
class QuizForm(forms.Form):
    pass
    # ask1 = forms.CharField(widget=forms.RadioSelect(choices=ASK1_CHOISE))
    # ask2 = forms.CharField(widget=forms.RadioSelect(choices=ASK2_CHOISE))
    # ask3 = forms.CharField(widget=forms.RadioSelect(choices=ASK3_CHOISE))
    # ask4 = forms.CharField(widget=forms.RadioSelect(choices=ASK4_CHOISE))
    # ask5 = forms.CharField(widget=forms.RadioSelect(choices=ASK5_CHOISE))