# Generated by Django 2.1.2 on 2019-02-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0005_auto_20190206_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='portfolio_site',
            field=models.URLField(blank=True),
        ),
    ]
