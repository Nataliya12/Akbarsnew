# Generated by Django 2.1.5 on 2020-04-15 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_answer_answerhistory_namequestions_test_testhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, verbose_name='Наименование вопроса')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Test')),
            ],
            options={
                'verbose_name': 'Название вопросов',
                'verbose_name_plural': 'Название вопросов',
            },
        ),
        migrations.RemoveField(
            model_name='namequestions',
            name='modeltest',
        ),
        migrations.RenameField(
            model_name='answerhistory',
            old_name='modeltestirovanieuser',
            new_name='testhistory',
        ),
        migrations.RenameField(
            model_name='testhistory',
            old_name='modeltest',
            new_name='test',
        ),
        migrations.AlterField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Questions'),
        ),
        migrations.AlterField(
            model_name='answerhistory',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Questions'),
        ),
        migrations.DeleteModel(
            name='NameQuestions',
        ),
    ]
