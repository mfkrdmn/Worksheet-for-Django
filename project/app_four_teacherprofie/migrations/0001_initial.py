# Generated by Django 4.0.5 on 2022-08-16 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_one_onetoone', '0003_rename_lesson_onetoone_lesson_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_one_onetoone.teacher')),
            ],
        ),
    ]
