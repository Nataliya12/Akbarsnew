# Generated by Django 2.2 on 2020-02-12 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameuser', models.CharField(max_length=200, verbose_name='Имя')),
                ('family', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Пользователь'), (2, 'Администратор')], default=1, verbose_name='Роль')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['nameuser'],
            },
        ),
    ]
