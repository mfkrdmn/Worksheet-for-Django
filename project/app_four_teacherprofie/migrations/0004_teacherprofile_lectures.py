# Generated by Django 4.0.5 on 2022-08-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_four_teacherprofie', '0003_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='lectures',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
