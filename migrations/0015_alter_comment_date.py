# Generated by Django 4.2.16 on 2024-12-10 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_comment_date_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 11, 2, 56, 57, 916815), verbose_name='Дата комментария'),
        ),
    ]
