# Generated by Django 4.2.16 on 2024-10-26 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 10, 26, 13, 21, 36, 945326), verbose_name='Дата комментария'),
        ),
    ]
