# Generated by Django 4.0.5 on 2022-08-15 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_one_onetoone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_onetoone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name_onetoone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_onetoone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_onetoone', models.CharField(max_length=50)),
                ('picture_onetoone', models.ImageField(null=True, upload_to='profile_images')),
            ],
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.AddField(
            model_name='lesson_onetoone',
            name='lesson_teacher_onetoone',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_one_onetoone.teacher_onetoone'),
        ),
    ]
