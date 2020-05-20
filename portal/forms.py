from django import forms
from django.contrib.auth.models import User


class FormLog(forms.Form):
    mail = forms.CharField(label='Электронная почта', widget=forms.TextInput(attrs={'placeholder': u'', 'class':"form-control"}))
    password = forms.CharField(label='Пароль',  widget=forms.PasswordInput(attrs={'placeholder': u'', 'class':"form-control"}))

    def clean_mail(self):
        mail = self.cleaned_data.get('mail')
        if mail:
            if not User.objects.filter(username=mail):
                raise forms.ValidationError('Электронная почта указана неверно')
        return mail


   # def clean_password(self):
    #    password = self.cleaned_data.get('password')
     #   if password:
      #      a = User.objects.filter(username=password)
        #    if a:
        #        raise forms.ValidationError('Пароль неверен')
         #   return password


class FormReg(forms.Form):
    name = forms.CharField(label='Имя',   widget=forms.TextInput(attrs={'class':"form-control"}))
    family = forms.CharField(label='Фамилия',  widget=forms.TextInput(attrs={'class':"form-control"}))
    mail = forms.EmailField(label='Электронная почта', widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(label='Пароль',  widget=forms.PasswordInput(attrs={'class':"form-control"}))
    password_copy = forms.CharField(label='Введите еще раз', widget=forms.PasswordInput(attrs={'class':"form-control"}))

    def clean_password_copy(self):
        password = self.cleaned_data.get('password')
        password_copy = self.cleaned_data.get('password_copy')
        if password and password_copy:
            if password != password_copy:
                raise forms.ValidationError('Пароли не одинаковые')
        return password_copy
    



    #def clean_mail(self):
     #   mail = self.cleaned_data.get('mail')
       # if mail:
        #    a = User.objects.filter(username=mail)
         #   if not a:
         #       raise forms.ValidationError('Такой пользователь уже существует в системе')
        #return mail