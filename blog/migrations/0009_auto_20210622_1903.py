# Generated by Django 3.1.2 on 2021-06-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210622_1411'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
