# Generated by Django 2.1.5 on 2020-02-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_businessinsiderheadline_seekingalphaheadline_wiredheadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thevergeheadline',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
