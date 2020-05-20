from django.db import models
from django.contrib.auth.models import User


#Профиль пользователя
class UserProfile(models.Model):
    ROLE_CHOICES = (
        (1, u'Пользователь'),
        (2, u'Администратор'),
    )
    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete=models.CASCADE)
    nameuser = models.CharField(max_length=200,verbose_name = 'Имя')
    family = models.CharField(max_length=200,verbose_name = 'Фамилия')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, verbose_name = 'Роль', default=ROLE_CHOICES[0][0])
    def __str__(self):
        return '%s %s' % (self.nameuser, self.family)
    class Meta:
        ordering = ["nameuser"]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

#Тест
class Test(models.Model):
    name = models.CharField(max_length=250,verbose_name='Название')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тесты'
        verbose_name_plural = 'Тесты'
        
#Вопрос       
class Questions(models.Model):
    test = models.ForeignKey(Test, null = True, on_delete=models.CASCADE)
    name = models.TextField(verbose_name='Наименование вопроса',blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'
        
#Ответ
class Answer(models.Model):
    questions = models.ForeignKey(Questions, null = True, on_delete=models.CASCADE)
    otvet = models.TextField(verbose_name='Ответ', blank=True, null = True)
    status = models.BooleanField(verbose_name = 'Верный ответ', default = None, blank=True)
    def __str__(self):
        return self.otvet
    class Meta:
        verbose_name = 'Ответы на вопросы'
        verbose_name_plural = 'Ответы на вопросы'


#История прохождения тестирования пользователями
class TestHistory(models.Model):
    userid = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, null = True, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name = 'Пройденный тест', default = False, blank=True)
    result = models.IntegerField(verbose_name='Полученный балл', null = True, blank=True )
    class Meta:
        verbose_name = 'История прохождения тестирования пользователями'
        verbose_name_plural = 'История прохождения тестирования пользователями'

#История ответов пользователей
class AnswerHistory(models.Model):
    testhistory = models.ForeignKey(TestHistory, null = True, on_delete=models.CASCADE)
    questions = models.ForeignKey(Questions, null = True, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='Ответ', blank=True)
    result = models.IntegerField(verbose_name='Полученый балл', null = True, blank=True )
    status_answer = models.BooleanField(verbose_name = 'Предоставленный ответ', default = False)
    class Meta:
        verbose_name = 'История ответов пользователей'
        verbose_name_plural = 'История ответов пользователей'