"""
Definition of forms.
"""

from django import forms
from .models import Comment, Blog
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class CTFForm(forms.Form):
    name = forms.CharField(label="Ваше имя", min_length="2", max_length=32)
    city = forms.CharField(label="Ваш город", min_length="2", max_length=32)
    gender = forms.ChoiceField(label="Ваш пол",
                                choices=(("1", "Мужской"),
                                ("2", "Женский")), 
                                initial=1)
    about_ctf = forms.ChoiceField(label="Знаете ли вы о CTF:",
                                    choices=(("1", "Нет, не знал"),
                                    ("2", "Знаю о их существований"),
                                    ("3", "Знаю о их существований, участовал в них"),
                                    ("4", "Постоянно играю в CTF")),
                                    initial=1)
    surctf = forms.ChoiceField(label="Хотели ли вы поучаствовать в CTF?",
                                    choices=(("1", "Нет, не хочу участвовать"),
                                            ("2", "Да, хочу участвовать"),
                                            ("3", "Не уверен")),
                                            initial=3)
    message = forms.CharField(label="Коротко о себе",
                               widget=forms.Textarea(attrs={'rows': 12, 'cols': 20}))
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        label = {'text':'Комментарий'}


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': 'Заголовок', 'description':'Краткое содержание', 'content':'Полное содержание', 'image':'Картинка'}