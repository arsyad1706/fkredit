# Generated by Django 4.1.1 on 2022-09-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_form_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='angsuran',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]