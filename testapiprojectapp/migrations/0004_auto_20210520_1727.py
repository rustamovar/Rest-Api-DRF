# Generated by Django 3.1.7 on 2021-05-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapiprojectapp', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rating',
            field=models.CharField(choices=[('excellent', 100), ('average', 70), ('bad', 50)], default='average', max_length=50),
        ),
    ]