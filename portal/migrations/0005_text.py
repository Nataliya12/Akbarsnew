# Generated by Django 2.1.5 on 2020-05-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20200416_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new1', models.TextField(blank=True, default='')),
            ],
        ),
    ]